import os
import curses
import urllib.request
import urllib.parse
import requests
import re
import subprocess
import wikipedia
import pytz
from pprint import pprint
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from datetime import datetime
from regions import cvb

Norman = ChatBot(
    "Norman",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri="sqlite:///database.sqlite3.norman",
    logic_apapter=[
    "chatterbot.logic.TimeLogicAdapter",
    "chatterbot.logic.MathematicalEvaluation",
    "chatterbot.logic.BestMatch"]
)

def weather_data(query):
	res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&appid=572d93171b72994ef6363b5648a60746&units=metric');
	return res.json()

def print_weather(result,city):
	print('\n'+"{}'s temperature: {} °C ".format(city,result['main']['temp']))
	print("Wind speed: {} m/s".format(result['wind']['speed']))
	print("Description: {}".format(result['weather'][0]['description']))
	print("Weather: {}".format(result['weather'][0]['main'])+'\n')

def main(city):
	try:
	  query='q='+city;
	  w_data=weather_data(query);
	  print_weather(w_data, city.capitalize())

	except:
	  print('City name not found...')

def NewsFromBBC(): 
    main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=4dbc17e007ab436fb66416009dfb59a8"
    open_bbc_page = requests.get(main_url).json() 
    article = open_bbc_page["articles"] 
    results = [] 

    for ar in article: 
        results.append(ar["title"]) 
          
    for i in range(5): 
        print(i + 1, results[i])  


print('Bot: Hello I am a chatbot. Type help to see what you can use me for.')

while True:
    command = input('You: ').lower()
    if 'help' in command:
        print(
            """I am a bot and these are the commands you can use for me:
                    "!Play (song)" - Plays your (song) from youtube
                    "Tell me about ..." - Gets you information about ... from wikipedia
                    "What is the weather in (city)" - Tells you the weather in (city) 
                    "What is the time in (city)" - Tells you the weather in (city)
                    "News" - Get todays news from BBC
                    "Hello" - Start a conversation with me
                    "Help" - Shows a list of what you can use me for
                    "Bye" - Quit program""")

    elif '!play' in command:
        reg_ex = re.search('!play (.*)', command)
        if reg_ex:
            query_string = urllib.parse.urlencode({"search_query" : reg_ex.group(1)})
            html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
            search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())

            url = "http://www.youtube.com/watch?v=" + search_results[0]
            os.startfile(url)
            print('Bot: Here you go')

    elif 'tell me about' in command:
        reg_ex = re.search('tell me about (.*)', command)
        try:
            if reg_ex:
                topic = reg_ex.group(1)
                ny = wikipedia.page(topic)
                print('\n', repr(ny.content[:500].encode('utf-8'))[2:-1])
                print('\nBot: This is what I could find on', '"'+topic+'"')
        except Exception:
            print('\nBot: I could not find anything on', '"'+topic+'"')
    
    elif 'what is the weather in' in command:
        reg_ex = re.search('what is the weather in (.*)', command)
        if reg_ex:
            main(reg_ex.group(1))
            print('Bot: Here you go')

    elif 'what is the time in' in command:
        reg_ex = re.search('what is the time in (.*)', command)
        a = command.capitalize()
        if reg_ex:
            for i in cvb:
                try:
                    print('\n','Bot: The current time in', a, 'is:', datetime.now(pytz.timezone(i+a)).strftime("%Y-%m-%d %H:%M:%S"))
                    break
                except:
                    pass
    
    elif 'news' in command:
        NewsFromBBC()
        print('\nBot: These are the top news today')

    elif 'bye' in command:
        quit('Bot: See you later')

    else:
        try:
            Norman_input = Norman.get_response(command)
            print('Bot:', Norman_input)
        except(KeyboardInterrupt, EOFError, SystemExit): 
            break






# # ALLT NEDAN BORDE FUNGERA MEN JAG HAR INGET LJUD PÅ DATORN OCH KUNDE DÄRFÖR INTE FÅ MIN AI ATT PRATA ELLER FÖRSTÅ ANVÄNDARE.

# # Ett sätt att känna omvandla text till speech. Kan användas för att få AI:n att prata med användaren.
# import pyttsx3

# engine = pyttsx3.init()
# eng_voice = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

# engine.setProperty('voice', en_voice_id)
# engine.say('Hello')

# engine.runAndWait()






# # Ett sätt att känna av vad en användare säger och omvandla det till text så att det går att svara.

# import speech_recognition as sr  
                                                                
# r = sr.Recognizer()   

# with sr.Microphone() as source:                                                                       
#     print("Speak:")                                                                                   
#     audio = r.listen(source) 

# print("I think you said", r.recognize_google(audio))