# The Outcasts of Hollywood

The datastory is available here: julia-walti.github.io/Ada_Project_Site

## Abstract

The movie industry today is a caucasian man’s world but things are changing. There has been a debate in recent years whether cultural minorities have been invisibilized in occidental cultural works, especially in American cinema. Moreover, with the rise of the MeToo movement and feminism in general, the place of women in this industry has also been debated. Indeed, both these groups are often portrayed as stereotypical secondary characters and most successful movies are often not portraying stories about these groups. Also, they are noticeably absent from the crews. [1][2][3]


Hence, the place of minorities and women in movies will be studied in this project. This will be done in terms of presence, representation and success by looking at actors, characters and crew members. With this, a timeline of the integration of these groups in the industry will be created, with which a time-series analysis will be performed.
It must be noted that the dataset used goes to the year 2013, and as many changes have been put in place since then, some might be missed as they happened recently. Moreover, during this project, gender will be looked as binary as it represented this way in the dataset.


## Research questions

1.  Are the genre of a movie and the ethnicity of the lead role correlated?
    Are the genre of a movie and the gender of the lead role correlated?

2. How does the proportion of movies with women in the crew change with time ?

3. Is there a noticeable difference in revenue for movies that portray some particular ethnicities/genre ? Is there a noticeable difference in revenue for movies including women in the crew ?
4. What are the most recurrent semantic field associated with each gender and for people of color ?



## Proposed additional datasets

- [ImdB crew dataset](https://datasets.imdbws.com/). We need to deal with the fact that it does not contain movies released before 1980.

- [Directors' and writers' gender](https://github.com/taubergm/HollywoodGenderData/blob/master/all_directors_gender.csv)

- [Main actors and budget dataset](https://www.kaggle.com/datasets/danielgrijalvas/movies)


## Methods
1. Genders and ethnicities of the actors
    1. Movie revenue distribution in main character database versus cmu movies <br>
      Performing independent Student test to evaluate any bias on the revenue before merging the CMU data with the main characters data on the revenue.
    2. Genre distribution in cmu database versus main character database <br>
      Performing independent Student test to evaluate any bias on the genre distribution before merging the CMU data with the main characters data on the revenue.
    3. Are movies genres and gender of the lead role related? <br>
      Showing the raw distributions of lead roles for male/female first. Then compute the difference between the real distribution of lead roles and a uniform distribution of roles. Chi-squared test are computed to confirm the biases in the lead roles.
    4. Adding the ethnicity of actors <br>
      The ethnicities were retrieved with a query on the freebase ids. <br>
      Showing the raw distributions of lead roles for ethnicities first. Then compute the difference between the real distribution of lead roles and a uniform distribution of roles. Chi-squared test are computed to confirm the biases in the lead roles.
2. Gender of the crew
    1. Data preprocessing <br>
      Retrieval of movies with women as director or/and writer.
    2. Are the proportions of movies with women in the crew or created by men different ? <br>
      Computation of proportions.
    3. Does the proportion of movies with women in the crew change with time ? <br>
      Plotting time series of proportions.

3. Revenue comparisons
    1. In terms of the gender of the main actor <br>
      First, a naive Matt-Whitney U test is performed to compare revenue for each gender as lead role. Then, we perform the same test after matching movies using propensity scores to mitigate the effect of confounding variables.
    2. In terms of the gender of the crew <br>
      First, a naive Matt-Whitney U test is performed to compare revenue for each gender as part of the crew. Then, we perform the same test after matching movies using propensity scores to mitigate the effect of confounding variables.
4. NLP <br>
  The NLP processed summaries are parsed. First, all the mentionings of the characters are retrieved thanks to coreference resolution. We filter out all the coreferences with does not involve PERSON entities (characters). Once all the characters' mentionings are found, the interesting dependencies (amod, appos, nsubj…) involving the characters found are retrieved [4].



## Proposed timeline

- until 09/11: Choice of the topic and definition of the research questions, redaction of the abstract, skeleton of the methods
- 09/11: Division of tasks
- 09/11 to 18/11: Redaction of the notebooks and finish the readme
- 18/11: Hand in of milestone 2
- 18/11 to 02/12: Gather all useful data for computing the results, as well as convert the data into useful form.
- 02/12 to 15/12:  Finish results of all research questions and summarize them in graph or text.
- 15/12 to 23/12:  Discuss the results of research questions with the whole team and make a conclusive analysis of said results. Summarize the analysis on the website page.
- 23/12: Hand in of milestone 3  


## Organization within the team

- Esha: Analysis of actor casting and plotting
- Julia: Conception of the website and analysis of crew data
- Pierre: Parsing of the NLP XMLs and redaction of README
- Léo: Post-processing and plotting of the NLP results

## Sources

[1] [The History And Future Of Women In Film](https://womensmediacenter.com/fbomb/the-history-and-future-of-women-in-film)

[2] [Female Representation In Movies Has Barely Changed In A Decade, But There's A Way We Can Fix It](https://www.bustle.com/p/female-representation-in-movies-has-barely-changed-in-a-decade-but-theres-a-way-we-can-fix-it-9940849)

[3] [Minority Recognition In Film: Where Is The Diversity ?](https://impakter.com/minority-recognition-in-film-where-is-the-diversity/)

[4] [Marneffe, M.D., & Manning, C.D. (2010). Stanford typed dependencies manual.](https://www.semanticscholar.org/paper/The-Stanford-Typed-Dependencies-Representation-Marneffe-Manning/f66821598f4db7a6a2f54a6a4ae43e391649f4c1)
