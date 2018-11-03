## MovieDB Chatbot

### Welcome to Loewi's GetMovieNow.

Hi, I'm Bot Loewi. Here is what I can do:

* Tell me your current location.  
I will show you the top 5 PLAYING NOW movies.

* Tell me your fav among the five.    
U will get the movie's RATING, INFO & LINK for more information.

* If you are interested in me, maybe we can have a little weird *CHAT* together.

##### This is what I look like when I'm on Terminal：

<center>
<img src="https://github.com/LoewiLu/Chatbot/blob/master/img/LoewiProject%20Screen%20Shot%201.png" width="25%" />
</center>

##### This is what I look like when I'm on Wechat：

<center>
    <img src="https://github.com/LoewiLu/Chatbot/blob/master/img/Screen%20Shot%202018-08-01%20at%2010.21.39%20PM.png" width="25%"/>
</center>

**How to run me?** 

- Run the code by using `main.py`

- Components explanation：

	`MovieAdapter.py` includes two [LogicAdapters](https://chatterbot.readthedocs.io/en/stable/logic/)
	
	`tokenise.py` is for tokenization and maximum matching
	
	`get_movie.py` dumps `moive_id.json` and writes `all_movie_names.txt`
	
	`get_city_name_pinyin.py`(deleted) dumps `city_pinyin.json` and writes `all_city_names.txt`
	
	`wechat_load.py` using data from your own Wechat dumps yml files,(private/deleted)
	
	`myCorpus` is for all yml files
