#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 14:53:57 2018

@author: loewi
"""
from urllib import request
from bs4 import BeautifulSoup 
import re
import json
'''
实时更新，大概一周刷一次就ok了
'''

#拿到动态的电影名+电影ID放入json
#将动态的电影名写入txt 

def get_movie_id():    
    url = "https://movie.douban.com/"
    req = request.Request( url )
    html = request.urlopen( req ).read().decode("utf-8")
    soup = BeautifulSoup(html, 'html.parser')    
    #data = re.findall('class="ui-slide-item".*data-title="(.*)"\sdata-release="(.*)"\sdata-rate="(.*)"\sdata-star=.*data-trailer="(.*)"\sdata-ticket=.*data-duration="(.*)"\sdata-region="(.*)"\sdata-director="(.*)"\sdata-actors="(.*)"\sdata-intro',html)
#    print(data_contents)
    
    contents = soup.find_all('li', class_ ='ui-slide-item')   
    urls = soup.find_all('a', onclick = "moreurl(this, {from:'mv_a_tl'})") 
    
    data_title_list = []
    for data_title in contents:
        cleaned_data_title = data_title.get('data-title')
        if cleaned_data_title == None: continue
        clean_data_title = cleaned_data_title.split()
#        print(clean_data_title[0])
        data_title_list.append(clean_data_title[0])
    
#    print(*data_title_list, sep = '\n')
    
        
    id_list = []    
#    url_list = []
    for url in urls:    
        cleaned_url= url.get('href')
#        print(cleaned_url)
#        url_list.append(cleaned_url)
#    print(url_list)  
        id_ = re.findall('.*subject/(.*)/',cleaned_url)
        id_list.append(id_[0])
#    print(id_list)        
        
        
    dictionary = dict(zip(data_title_list, id_list))
#    print(dictionary)

    f = open( "movie_id.json", "w", encoding = "utf-8" )
    json.dump( dictionary, f, ensure_ascii = False, indent = 2 )
    f.close()
    
    file = open('all_movie_names.txt','w')
    for titles in data_title_list:        
        file.write(titles+'\n') 
    file.close()

 #%%
 
#x = ['西虹市首富', '狄仁杰之四大天王', '摩天营救', '我不是药神', '邪不压正', '神奇马戏团之动物饼干 Magical Circus : Animal Crackers', '新大头儿子和小头爸爸3：俄罗斯奇遇记', '侏罗纪世界2 Jurassic World: Fallen Kingdom', '动物世界', '汪星卧底 Show Dogs', '北方一片苍茫', '萌学园：寻找盘古', '超人总动员2 Incredibles 2', '淘气大侦探 Sherlock Gnomes', '细思极恐']
#
#file = open('all_movie_names.txt','w')
#for titles in x:        
#    file.write(titles+'\n') 
#file.close()

 
 
 
