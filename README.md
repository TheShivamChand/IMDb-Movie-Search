# IMDb-Movies-R2D2
This project was made as an assignment for R2D2. This was made with python using Flask.

## Prerequisites
1. Flask
2. MongoDB

### Scrapping the IMDb Website
For scrapping the IMDb website, I used BeautifulSoup. I fetched the top 1000 movies from the website and saved all the required columns as separate lists. After that, I made a dictionary and combined all those lists.

After that, I stored all the data in the collection to a database.
As per the question, I fetched all the data from the database and put it on the javascript array. From that, I generated all the suggestions as per the key pressed by the user on the keyboard. I used the concept of Longest Common Subsequence(LCS) to match the input string with the names of the movies. The suggestions are generated upto 5 as per the given constraints in the descripton. The major observation was to retrieve the data from the database and integrate it with javascript and rendering it through HTML.

### Movie Search
Just type the character in the input and the suggestion would appear as per they are valid. Then select the particular movie and click on the search button and you would get the details of that movie.

### ID Search
Just type the ID in the input and the suggestion would appear as per they are valid. Then select the particular ID and click on the search button and you would get the details of that movie related to that id and also you would get the JSON response which should have been returned by an API. The URL is same as the documentation of yours i.e., /movies/&lt;movie_id&gt;

The screenshots of the same can be seen from the link attached: https://drive.google.com/open?id=1Bl8yZ2mOFuT_F76IIPKWm8TWS7lTsOgn
