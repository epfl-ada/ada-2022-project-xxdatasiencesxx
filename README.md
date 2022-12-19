# The Outcasts of Hollywood

The datastory is available here: julia-walti.github.io/Ada_Project_Site

## Abstract

The movie industry today is a caucasian man’s world but things are changing. There has been a debate in recent years whether cultural minorities have been invisibilized in occidental cultural works, especially in American cinema. Moreover, with the rise of the MeToo movement and feminism in general, the place of women in this industry has also been debated. Indeed, both these groups are often portrayed as stereotypical secondary characters and most successful movies are often not portraying stories about these groups. Also, they are noticeably absent from the crews. [1][2][3]


Hence, the place of minorities and women in movies will be studied in this project. This will be done in terms of presence, representation and success by looking at actors, characters and crew members. With this, a timeline of the integration of these groups in the industry will be created, with which a time-series analysis will be performed.
It must be noted that the dataset used goes to the year 2013, and as many changes have been put in place since then, some might be missed as they happened recently. Moreover, during this project, gender will be looked as binary as it represented this way in the dataset. 


## Research questions

1. Is there a difference in the role distribution for different ethnicities/genders time-wise? 
2. What are the most recurrent adjectives, verbs (actions) for each ethnicity/genre character ? Does it change in time? Can we draw the stereotyped character for each ethnicity in Hollywood ?
3. Are movies genres and ethnicity/gender related?
4. Is there a noticeable difference in revenue for movies that portray some particular ethnicities/genre? Is there a noticeable difference in revenue for movies created by women ?
5. Does the proportion of movies with women in the crew change with time ?


## Proposed additional datasets

- [ImdB crew dataset](https://datasets.imdbws.com/)

- [Directors' and writers' gender](https://github.com/taubergm/HollywoodGenderData/blob/master/all_directors_gender.csv)

- [Main actors and budget dataset](https://www.kaggle.com/datasets/danielgrijalvas/movies)


## Methods

1. Identify role: A dataset containing the main role in movies was found. The issue with this dataset is that it does not contain movies released before 1980. Another approach would be using the NLP processed plot and count the number of times a character is cited in the plot. Therefore a ranking (most cited to less cited) can be applied assuming the main role is the most cited character in the Wikipedia plot.
2. Stereotypes in summaries: The NLP processed plots are parsed. First all the characters are retrieved thanks to named-entity recognition. Once all the characters are found, the interesting dependencies (amod, appos, nsubj…) involving the characters found are retrieved [4].  Pronouns are also used to describe a character and only using dependencies on names will be a loss of information. Therefore, coreferences will be used to assign pronouns to corresponding characters.
3. Relationship between movie genre and ethnicity/genre of actors grouping the data based on the variables (i.e. ethnicity of director and grossing) and performing statistical tests 
4. Change in revenue: First, we will simply look at the raw difference between movies directed/written by women or by men. Then, if we want to study a real bias only based on color/gender, it is hard to do since there are a lot of covariates that can explain the differences. One of the principal ones is that the biggest productions are not directed by minorities, and big productions lead to big revenues. To mitigate this, we will use a budget feature to use in a matching procedure. We can also do a linear regression to see the effect of each feature on the revenue and look at the importance of the gender/ethnicity of actors/directors/writers.
5. Proportions with time First, we need to merge crew info with crew gender info and movie dataset. Then we can look at the number of movies directed by women and men each year and perform a t-test to evaluate the difference of the distribution. 


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

- Questions 3, 4 and 5: Esha and Julia 
- Coding of the site: Esha and Julia 
- Questions 1 and 2: Pierre and Léo will work on the NLP 
- Analysis of the result and the texts of the site will be done by the whole team 

## Sources

[1] [The History And Future Of Women In Film](https://womensmediacenter.com/fbomb/the-history-and-future-of-women-in-film)

[2] [Female Representation In Movies Has Barely Changed In A Decade, But There's A Way We Can Fix It](https://www.bustle.com/p/female-representation-in-movies-has-barely-changed-in-a-decade-but-theres-a-way-we-can-fix-it-9940849)

[3] [Minority Recognition In Film: Where Is The Diversity ?](https://impakter.com/minority-recognition-in-film-where-is-the-diversity/)

[4] [Marneffe, M.D., & Manning, C.D. (2010). Stanford typed dependencies manual.](https://www.semanticscholar.org/paper/The-Stanford-Typed-Dependencies-Representation-Marneffe-Manning/f66821598f4db7a6a2f54a6a4ae43e391649f4c1)






