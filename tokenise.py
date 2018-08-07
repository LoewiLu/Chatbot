#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 17:17:51 2018

@author: loewi
"""

import re


def maximum_matching( sentence, phrases):

    sentence = re.sub("\s*", "", sentence)# remove whitespaces
    result = []
    
    i = 0
    
    while i < len( sentence ):
        max_len_idx = i
        for j in range( i, len(sentence) ): 
            if sentence[i:j+1] in phrases:
                max_len_idx = j

        result.append( sentence[ i:max_len_idx+1 ] )
        i = max_len_idx + 1
    
    return result

def remove_stopwords( tokens, stopwords ):


    result = []
    for seg in tokens:
        if seg not in stopwords:
            result.append( seg )
            
#ALTERNATIVE: using remove fuction instead:
            
#    result = tokens        
#    for seg in tokens:
#        if seg in stopwords:
#            result.remove( seg )
            
    return result

    
def test1():
#    print( maximum_matching(sentence = "今天天气真是好啊",   phrases = ["今天","今", "天","天气","真是"] ) )
#    print( maximum_matching(sentence = "今天天气真是好啊",   phrases = ["今天", "天气","真是"] ) )
#    print( maximum_matching(sentence = "",   phrases = ["今天","今", "天","天气","真是"] ) )

#    print( maximum_matching(sentence = "莎拉波娃现在居住在美国东南部的佛罗里达",   
#                            phrases = ["莎拉波娃", "莎拉", "现在", "居住","美国","东南部", "佛罗里达"] ) )
    
#    print( maximum_matching(sentence = "莎拉波娃现在居住在美国东南部的佛罗里达",   
#                            phrases = ["川普", "莎拉", "现在", "居住","美国","东南部", "佛罗里达"] ) )
    
    phrases = []
    for line in open("all_movie_names.txt", encoding = "utf-8"): phrases.append( line.split()[0] ) 
    statement = "啊，我不是药神将啥的"       
    rst_statement = maximum_matching(sentence = statement ,  phrases = phrases)     
    print(rst_statement)
    movie_name = [i for i in rst_statement if i in phrases]      
    print (movie_name[0])
#    phrases = []
#    for line in open("all_city_names.txt", encoding = "utf-8"): phrases.append( line.split()[0] ) 
#    statement = "我草， 我在天津"    
#    
#    rst_statement = maximum_matching(sentence = statement ,  phrases = phrases)     
#    print(rst_statement)    
#    for pieces in rst_statement:
#        if pieces in phrases:
#            print(pieces)
            
            #    print( maximum_matching(sentence = "我马上要去美国总领事馆办理签证",  phrases = phrases) )           
#    print( maximum_matching(sentence = "大吉大利，今晚吃鸡",  phrases = phrases) )       
#    print( maximum_matching(sentence = """
#                            新华社纽约9月30日电 财经观察：金融科技重塑传统华尔街
#
#　　新华社记者王乃水
#
#　　以人工智能为代表的金融科技，正在华尔街的传统金融业务中扮演着越来越重要的角色，由其驱动的量化交易、智能顾投等金融新业态，也越来越受到华尔街机构和投资者的青睐。
#  """,  phrases = phrases) ) 
    
    
def test2():
    print( remove_stopwords( tokens = ["今天","天气","真是","好", "啊"],  stopwords = [ "好", "啊"] )  )
    print( remove_stopwords( tokens = ['莎拉波娃', '现在', '居住', '在', '美国', '东南部', '的', '佛罗里达'],  
                            stopwords = [ "在", "是", "之", "的", "好", "啊"] )  )
    print( remove_stopwords( tokens = ['Hello', '大家', '在', '美丽',  '的', '佛罗里达'],  
                            stopwords = [ "在", "是", "之", "的", "好", "啊"] )  )

if __name__ == "__main__":
    test1()
#    print("#"*60)    
#    test2()


             
                          

    
    
"""Sample output
['今天', '天气', '真是', '好', '啊']
['今天', '天气', '真是', '好', '啊']
[]
['莎拉波娃', '现在', '居住', '在', '美国', '东南部', '的', '佛罗里达']
['莎拉', '波', '娃', '现在', '居住', '在', '美国', '东南部', '的', '佛罗里达']
['我', '马上', '要', '去', '美国', '总领事馆', '办理', '签证']
['大吉大利', '，', '今晚', '吃', '鸡']
['新华社', '纽约', '9', '月', '3', '0', '日电', '财经', '观察', '：', '金融', '科技', '重塑', '传统', '华尔街', '新华社', '记者', '王', '乃', '水', '以', '人工智能', '为', '代表', '的', '金融', '科技', '，', '正在', '华尔街', '的', '传统', '金融业', '务', '中', '扮演', '着', '越来越', '重要', '的', '角色', '，', '由其', '驱动', '的', '量化', '交易', '、', '智能', '顾', '投', '等', '金融', '新业', '态', '，', '也', '越来越', '受到', '华尔街', '机构', '和', '投资者', '的', '青睐', '。']
############################################################
['今天', '天气', '真是']
['莎拉波娃', '现在', '居住', '美国', '东南部', '佛罗里达']
['Hello', '大家', '美丽', '佛罗里达']
"""
    
