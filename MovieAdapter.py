#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 14:53:57 2018

@author: loewi
"""

from urllib import request
from bs4 import BeautifulSoup
from chatterbot.logic import LogicAdapter
import chatterbot
from tokenise import maximum_matching
import json

class CityMovieLogicAdapter( LogicAdapter ):
    """
    transform city_name into city_pinyin
    go back to the citymovie website and get all playing movies of that city
    
    """
    
#    def __init__( self, **kwargs ):
#        super( CityMovieLogicAdapter, self ).__init__( **kwargs )
#
#        self.cities = json.load( open("city_pinyin.json", "r", encoding="utf-8")  )
    def __init__( self, **kwargs ):
        super( CityMovieLogicAdapter, self ).__init__( **kwargs )
        self.cities = json.load( open("city_pinyin.json", "r", encoding="utf-8")  )
        self.phrases = []
        for line in open("all_city_names.txt", encoding = "utf-8"): self.phrases.append( line.split()[0] )       
        
#    def can_process(self, statement):
        #找寻关键词
#        str_statement = str(statement)       
#        #token       
#        phrases = []
#        for line in open("all_city_names.txt", encoding = "utf-8"): phrases.append( line.split()[0] )       
#        rst_statement = maximum_matching(sentence = str_statement ,  phrases = phrases) 
#        for pieces in rst_statement:
#            if pieces in phrases:
#                return True
##        return False（之前删了）
    def can_process(self, statement):
        for _ in self.phrases: # 这里的 self.phrases 是在 init 里面读取的。
            if statement.text.find(_) >= 0: 
                return True
        return False # 确定了找不到的时候会 return False        

    
    def __get_movies( self, city_pinyin ):
          
        url = 'https://movie.douban.com/cinema/nowplaying/%s' %city_pinyin
        req = request.Request( url )
        html_content = request.urlopen( req ).read().decode("utf-8")
        #    print(html_content)
        soup = BeautifulSoup(html_content, 'html.parser') 
        movie_title_list=[]
        for title in soup.find_all('li'):
            movie_title = title.get('data-title')       
            if movie_title == None:continue
            else:
                movie_title_list.append(movie_title)
                    
        rst = ''
        for index, movies in enumerate(movie_title_list[:5]):
            index += 1
            rst += str(index)+' '+movies + '\n' 
        rst0 = "您所在的城市正在上映的电影有这些~\n" + rst + "【偷偷地说】人家不是很智能啦～您想看哪部？发我电影名字，我帮您查查～～"
                  
        return rst0
    
    
    def process( self, statement ):#input statment
        
        #debug statement<class 'chatterbot.conversation.Statement'>变成 <class 'str'>
        str_statement = str(statement)
        
        #token

        phrases = []
        for line in open("all_city_names.txt", encoding = "utf-8"): phrases.append( line.split()[0] )       
        rst_statement = maximum_matching(sentence = str_statement ,  phrases = phrases) 
        city_name_list = [i for i in rst_statement if i in phrases]      
            
        city_name = city_name_list[0]
            #statement contains no acurate movie name
    
        rst_statement = chatterbot.conversation.Statement('')          
            

        city_pinyin = self.cities[city_name]
        rst_statement.text = self.__get_movies(city_pinyin)


        rst_statement.confidence = 1.0
      
        return rst_statement

class MovieInfoLogicAdapter( LogicAdapter ):
    
#    def __init__( self, **kwargs ):
#        super( MovieInfoLogicAdapter, self ).__init__( **kwargs )
#        self.movies = json.load( open("movie_id.json", "r", encoding="utf-8")  )
    def __init__( self, **kwargs ):
        super( MovieInfoLogicAdapter, self ).__init__( **kwargs )
        self.movies = json.load( open("movie_id.json", "r", encoding="utf-8")  )
        self.phrases = []
        for line in open("all_movie_names.txt", encoding = "utf-8"): self.phrases.append( line.split()[0] )          
#    def can_process(self, statement):
#        
#        """
#        token, if find the keyword, return True 
#        """
#        str_statement = str(statement)       
#        #token       
#        phrases = []
#        for line in open("all_movie_names.txt", encoding = "utf-8"): phrases.append( line.split()[0] )       
#        rst_statement = maximum_matching(sentence = str_statement ,  phrases = phrases) 
#        for pieces in rst_statement:
#            return(pieces in phrases)
    def can_process(self, statement):
        for _ in self.phrases: # 这里的 self.phrases 是在 init 里面读取的。
            if statement.text.find(_) >= 0: return True #用txt文件里的名字去用户输入的文字找匹配的
            #str.find(str, beg=0, end=len(string))//Index if found and -1 otherwise.
        return False # 确定了找不到的时候会 return False
            
    def __get_movieinfo( self, movie_id ):
        """
        return a string featuring this movie
        """
        url = "https://movie.douban.com/subject/%d" % int(movie_id)
    #    print(url)
        req = request.Request( url )
        html_content = request.urlopen( req ).read().decode("utf-8")
    #    print(html_content)
        soup = BeautifulSoup(html_content, 'html.parser')    
        for rate in soup.find_all('strong', property="v:average"):
            if rate.text == '':
                rst_text = '暂无评分 '
            else:
                rst_text = '评分:'+rate.text+'分 '
        for info in soup.find_all('span', property="v:summary"):
            rst_intro_text = '简介:'+info.text.replace(' ','').replace('\n','').replace('\u3000','')
        rst_link_text = '详情请点击:'+url        
        rst = rst_text + rst_intro_text  + rst_link_text
        
        return rst       
      
    
    def process( self, statement ):#input statment
                
        """
        token, using movie_name to get movie_id
        then go back to __get_movieinfo to get features of the movie
        """
        #debug statement<class 'chatterbot.conversation.Statement'>变成 <class 'str'>
        str_statement = str(statement)
        
        #token

        phrases = []
        for line in open("all_movie_names.txt", encoding = "utf-8"): phrases.append( line.split()[0] )       
        rst_statement = maximum_matching(sentence = str_statement ,  phrases = phrases) 
   
        movie_name_list = [i for i in rst_statement if i in phrases]      
        movie_name = movie_name_list[0]
        
            
        rst_statement = chatterbot.conversation.Statement('')           

        movie_id = self.movies[ movie_name ]
        rst_statement.text = self.__get_movieinfo( movie_id )


     
        rst_statement.confidence = 1.0
      
        return rst_statement

    

    

if __name__ == "__main__":
    print("I am running")
    
    r = chatterbot.ChatBot( "Kala", 
                           storage_adapter='chatterbot.storage.SQLStorageAdapter',
                           database="db_test",
                             logic_adapters = [
                                     { 'import_path' : 'MovieAdapter.CityMovieLogicAdapter'  },
                                     { 'import_path' : 'MovieAdapter.MovieInfoLogicAdapter'  }
                                     ],
                                     read_only = True
                                     )

    
    print( r.get_response('我在南京') )

    print( r.get_response('邪不压正好不好看') )
 
    print( r.get_response('我去，南京有啥电影') )

    print( r.get_response('给我讲讲神奇马戏团之动物饼干') )
    


#%%

#    print( r.get_response('我想看12adf神奇马戏团之动物饼干') )#还是“我想看12adf神奇马戏团之动物饼干”
#
#phrases = []
#for line in open("all_movie_names.txt", encoding = "utf-8"): phrases.append( line.split()[0] )       
#rst_statement = maximum_matching(sentence = '我想看12adf神奇马戏团之动物饼干' ,  phrases = phrases) 
#   
#movie_name_list = [i for i in rst_statement if i in phrases]      
#movie_name = movie_name_list[0]             
#print(movie_name)         #神奇马戏团之动物饼干              
#
#phrases = []
#for line in open("all_movie_names.txt", encoding = "utf-8"): phrases.append( line.split()[0] )       
#rst_statement = maximum_matching(sentence = '我想看12adf神奇马戏团之动物饼干' ,  phrases = phrases) 
#for pieces in rst_statement:
#    if pieces in phrases:
#        print(pieces in phrases) #True
##这俩都没问题啊
#%%
    






