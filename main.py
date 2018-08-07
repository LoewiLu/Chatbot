import sys, time
import os
import chatterbot
from get_movie import get_movie_id
from termcolor import colored, cprint
from multiprocessing import Process, Lock

name = "Loewi_proto"
db_fname = "db222"
my_adapters =[ { 'import_path': 'MovieAdapter.MovieInfoLogicAdapter' },
              { 'import_path': 'MovieAdapter.CityMovieLogicAdapter'}, 
              "chatterbot.logic.BestMatch"  ]



if not os.path.exists( db_fname ):
    # 如果不存在 DB 文件，则新建一个 bot 并重新训练
    chatbot = chatterbot.ChatBot(  name, 
                           storage_adapter='chatterbot.storage.SQLStorageAdapter',
                           database= db_fname,
                           logic_adapters = my_adapters ,
                           read_only = False
    )
    chatbot.set_trainer( chatterbot.trainers.ChatterBotCorpusTrainer )
#    chatbot.train( "chatterbot.corpus.english" )
#    chatbot.train( "chatterbot.corpus.chinese" )
    
    chatbot.train( "myCorpus" )
    chatbot.set_trainer( chatterbot.trainers.ListTrainer )
    chatbot.train([
                "你好",
                "Hello",
                "哈喽",
                "Do you need help？"
                "我可以根据您所在城市推荐电影",
                
            ])        

#%% 此时肯定有 DB 文件了，直接 重新 load 数据库
chatbot = chatterbot.ChatBot(name, 
                       storage_adapter ='chatterbot.storage.SQLStorageAdapter',
                       database = db_fname,
                       logic_adapters = my_adapters,
                       read_only = True
)



#%%
#while True:
#    x = input( "TYPING: " ).strip()
#    if x == "quit" or x == "exit": break
#    print( chatbot.get_response(x) )
def blink_once():
     sys.stdout.write('\r       ')
     time.sleep(0.3)
     sys.stdout.write('\rTYPING：')
     time.sleep(0.3)

def blink(number):
     for x in range(0,number):
         blink_once()

if __name__ == '__main__':
    print('欢迎光临Loewi影讯小店～输入您所在【城市名】获取上映电影排行～',end='\n')
    get_movie_id()
    print('还有瞎聊吹水等功能',end=' ')
    print('如要退出，请输入quit',end='\n')
    
    while True:
        x = input( "请讲: " ).strip()
        if x == "quit" or x == "exit": break
    
        cprint(chatbot.get_response(x), 'magenta', attrs=['bold'])
    
#    response = chatbot.get_response(x)
#    def f(l,i):
#        l.acquire()
#        text = colored(response, 'grey')
#        i = '【记住，我不是人】'
#        print(text,i)
#        l.release()
#
#
#    lock = Lock()    
#    Process(target=f, args=(lock, blink(3))).start()
