
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import gzip
import glob, os
from tqdm.auto import tqdm
tqdm.pandas()



def xml_parsing(pathname):
    #This will be the fataframe containing all characters descriptions
    descriptions=pd.DataFrame(columns=['wiki_id', 'character', 'mentioning',
                                       'sentence_position', 'word_position', 'descriptions'])
    #Looping through all files in folder
    for filename in tqdm(glob.glob(pathname+'/*.xml.gz')):
            with gzip.open(filename, 'r') as f:

                # Reading the data inside the xml file to a variable under the name data
                data = f.read()

                #Get wiki id by getting the basename and removing the extension
                wikid = os.path.basename(filename)[0:-7]

                # Passing the stored data inside the beautifulsoup parser
                soup = BeautifulSoup(data, "xml")

                #DataFrame of all coreferences of the movie
                coreferences = pd.DataFrame(columns=['wiki_id', 'character', 'mentioning',
                                       'sentence_position', 'word_position', 'descriptions'])

                #Find all entities with coreferences
                entities = soup.find_all("coreference")
                entities = entities[1:]

                for entity in entities:
                    #Find every time this entity is mentioned
                    mentions = entity.find_all("mention")

                    #Find the representative aka the original mention of entity
                    rep = entity.find("mention", {'representative':True})

                    #Get sentence and word position of this representative
                    sent_pos = int(rep.sentence.text)
                    word_pos = int(rep.head.text)

                    #Search for the word using positions
                    sent = soup.find('sentence', {'id':sent_pos})
                    word = sent.find('token', {'id':word_pos})

                    #If the word is a person (character) create a full name variable
                    if word.NER.text == 'PERSON':
                        person = word
                        full_name = person.word.text
                    else: #Else the representative is not a character
                        continue #skip this entity

                    #Finding the words before (e.g Dr. Prof.) that are part of the full name
                    word_before = person.previous_sibling.previous_sibling

                    if word_before is not None:

                        #Loop while the words before are compounds of the proper noun
                        while word_before.POS.text == 'NNP':
                            full_name = word_before.word.text+' ' +full_name
                            word_before = word_before.previous_sibling.previous_sibling
                            if word_before is None:
                                break

                    #Finding the words after (last name)
                    word_after = person.next_sibling.next_sibling
                    if word_after is not None:

                        #Loop while the words after are compounds of the proper noun
                        while word_after.POS.text=='NNP':
                            full_name = full_name+ ' ' + word_after.word.text
                            word_after = word_after.next_sibling.next_sibling
                            if word_after is None:
                                break


                    #Loop through the other mentioning of the representative
                    for mention in mentions:

                        #Get sentence and word position of mention
                        sent_pos = int(mention.sentence.text)
                        word_pos = int(mention.head.text)

                        #Retrieve the word
                        sent = soup.find('sentence', {'id':sent_pos})
                        word = sent.find('token', {'id':word_pos}).word.text

                        #Create the tuple for this mention and append it to the coreferences dataframe
                        add_tuple = pd.DataFrame([[wikid, full_name, word,sent_pos,word_pos]], columns=['wiki_id', 'character', 'mentioning',
                                                       'sentence_position', 'word_position'])

                        coreferences = pd.concat([coreferences, add_tuple])


                #Find all dependencies in the plot. Creates a list of dependencies
                #each element is a sentence
                deps = soup.find_all("collapsed-ccprocessed-dependencies")

                #Enumerate all the coreferences of the plot to find their dependencies
                for i, (char, sent_pos,token_pos) in enumerate(coreferences[['character', 'sentence_position', 'word_position']].values):

                    #List for character as dependent
                    char_as_dep = set()
                    #List for character as governor
                    char_as_gov = set()

                    #Get the right sentence
                    sentence = deps[sent_pos-1]

                    #With token position of the coreference, find its relationship with other words

                    #As dependent first
                    dependent = sentence.find_all('dependent', {'idx':token_pos})
                    for dep in dependent:
                        relation = dep.parent

                        #We search for the relation types of our interest
                        if relation['type'] == 'nsubj' or relation['type'] == 'appos' \
                                or relation['type'] == 'nsubjpass' :
                            #We could directly retrieve the word in this dependence section
                            #but we rather have the lemmatized token
                            word_pos = relation.governor['idx']
                            sent = soup.find('sentence', {'id':sent_pos})
                            word = sent.find('token', {'id':int(word_pos)})
                            char_as_dep.update({word.lemma.text})

                    #As governor
                    governor = sentence.find_all('governor', {'idx':token_pos})
                    for gov in governor:
                        relation = gov.parent
                        if relation['type'] == 'rcmod' or relation['type'] == 'amod':
                            word_pos = relation.dependent['idx']
                            sent = soup.find('sentence', {'id':sent_pos})
                            word = sent.find('token', {'id':int(word_pos)})
                            char_as_gov.update({word.lemma.text})

                    #Add the descriptions to the coreferences tuple
                    char_as_dep.update(char_as_gov)
                    coreferences['descriptions'].iloc[i] = char_as_dep

                #Append the coreferences of the movie to the global DataFrame
                descriptions=pd.concat([descriptions, coreferences])


    #Some duplicates happen. We drop them but need to stringify because sets are not hashable.
    descriptions = descriptions[~descriptions.astype(str).duplicated(keep='first')]

    descriptions = descriptions.groupby(['wiki_id', 'character'])['descriptions'].apply(list).reset_index(name='descriptions')

    descriptions['descriptions']=descriptions['descriptions'].apply(lambda x: [val for sublist in x for val in sublist])

    #descriptions.to_csv('descriptions.csv')

    return descriptions
