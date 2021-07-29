# Shloka Recommendation System

Shloka Recommendation System recommends shlokass similar to the shloka user likes.

The details of the movies(Id, Shloka, Word-meaning, Translation, Purport, etc) are fetched from the data collected from https://vedabase.io/en/ .
<!-- 
Check out the live demo: https://mrswsa.herokuapp.com/

Link to youtube demo: https://www.youtube.com/watch?v=dhVePtyECFw -->
<!-- 
# Note

> #### Use this URL - https://the-movie-buff.herokuapp.com/ - in case if you see application error in the above mentioned URL -->

<!-- ## The Movie Cinema

I've developed a similar application called "The Movie Cinema" which supports all language movies. But the only thing that differs from this application is that I've used the TMDB's recommendation engine in "The Movie Cinema". The recommendation part developed by me in this application doesn't support for multi-language movies as it consumes 200% of RAM (even after deploying it to Heroku) for generating Count Vectorizer matrix for all the 700,000+ movies in the TMDB. 

Link to "The Movie Cinema" application: https://the-movie-cinema.herokuapp.com/

Don't worry if the movie that you are looking for is not auto-suggested. Just type the movie name and click on "enter". You will be good to go eventhough if you made some typo errors.

Source Code: https://github.com/agrawalanshul053/Website-final/edit/main/templates/Recommendation-System/ -->
<!-- 
## Featured in Krish's Live Session on YouTube

[![krish youtube](https://github.com/kishan0725/AJAX-Movie-Recommendation-System-with-Sentiment-Analysis/blob/master/static/krish-naik.PNG)](https://www.youtube.com/watch?v=A_78fGgQMjM)

## How to get the API key?

Create an account in https://www.themoviedb.org/, click on the `API` link from the left hand sidebar in your account settings and fill all the details to apply for API key. If you are asked for the website URL, just give "NA" if you don't have one. You will see the API key in your `API` sidebar once your request is approved. -->

## How to run the project?

1. Clone or download this repository to your local machine.
2. Go to the folder Website-final\templates\Recommendation-System in the directory where you have cloned or downloaded repository.
<!-- 2. Install all the libraries mentioned in the [requirements.txt](https://github.com/kishan0725/Movie-Recommendation-System-with-Sentiment-Analysis/blob/master/requirements.txt) file with the command `pip install -r requirements.txt` -->
<!-- 3. Get your API key from https://www.themoviedb.org/. (Refer the above section on how to get the API key)
3. Replace YOUR_API_KEY in **both** the places (line no. 15 and 29) of `static/recommend.js` file and hit save. -->
3. Open your terminal/command prompt from your project directory and run the file `main.py` by executing the command `python main.py`.
4. Go to your browser and type `http://127.0.0.1:5000/` in the address bar.
5. Hurray! That's it.

<!-- ## Architecture

![IMG-20210306-WA0012](https://user-images.githubusercontent.com/36665975/110212434-597bb700-7ec1-11eb-9ffa-7ac319e33123.jpg)

## Similarity Score : 

   How does it decide which item is most similar to the item user likes? Here we use the similarity scores.
   
   It is a numerical value ranges between zero to one which helps to determine how much two items are similar to each other on a scale of zero to one. This similarity score is obtained measuring the similarity between the text details of both of the items. So, similarity score is the measure of similarity between given text details of two items. This can be done by cosine-similarity.
   
## How Cosine Similarity works?
  Cosine similarity is a metric used to measure how similar the documents are irrespective of their size. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance (due to the size of the document), chances are they may still be oriented closer together. The smaller the angle, higher the cosine similarity.
  
  ![image](https://user-images.githubusercontent.com/36665975/70401457-a7530680-1a55-11ea-9158-97d4e8515ca4.png)

  
More about Cosine Similarity : [Understanding the Math behind Cosine Similarity](https://www.machinelearningplus.com/nlp/cosine-similarity/)

### Sources of the datasets 

1. [IMDB 5000 Movie Dataset](https://www.kaggle.com/carolzhangdc/imdb-5000-movie-dataset)
2. [The Movies Dataset](https://www.kaggle.com/rounakbanik/the-movies-dataset)
3. [List of movies in 2018](https://en.wikipedia.org/wiki/List_of_American_films_of_2018)
4. [List of movies in 2019](https://en.wikipedia.org/wiki/List_of_American_films_of_2019)
5. [List of movies in 2020](https://en.wikipedia.org/wiki/List_of_American_films_of_2020) -->

