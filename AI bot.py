  
import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('Your_App_ID')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-2].id)

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

greetMe()

speak('Hello Sir, I am your AI assistant shuklassistant ')
speak('consider me as your friend :) or a voice based OS')
speak('How may I help you?')


def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query
        

if __name__ == '__main__':

    while True:
    
        query = myCommand();
        query = query.lower()
        
        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'homework help' in query:
            speak('okay')
            webbrowser.open('www.brainly.in')

        elif 'open microsoft' in query:
            speak('okay')
            os.startfile('C:\Program Files\Microsoft Office\Office12')

        elif 'microsoft office' in query:
            speak('okay')
            os.startfile('C:\Program Files\Microsoft Office\Office12')
            
        elif 'open amazon' in query:
            speak('okay')
            webbrowser.open('www.amazon.com')


        elif 'can you cook' in query:
            speak('sorry sir I dont know and I dont even know that I should be happy about this or not....')
            speak('but i can make you learn Indian cooking')
            speak('Say yes if u are interested')

        elif 'yes' in query:
            speak('I dint actually expected such responce')
            speak('okay as you say')
            webbrowser.open('www.sanjeevkapoor.com')

        elif 'blog' in query:
            speak('okay')
            webbrowser.open('rkshani.blogspot.com')
            webbrowser.open('licpensionerscalicut.blogspot.com')
            
        elif 'covid status' in query:
            speak('covid status in India')
            webbrowser.open('www.covid19india.org')

        elif 'latest news' in query:
            webbrowser.open('www.bbcnews.com')

        elif 'python codes' in query:
            speak('Opening python codes')
            os.startfile('E:\Python Codes')

        elif 'C plus plus codes' in query:
            speak('Opening C++ codes')
            os.startfile('E:\c++ programs')            
            
        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("shreyanshshukla2020@gmail.com", '13feb2007@')
                    server.sendmail('shreyanshshukla2020@gmail.com', "sciencehelperamgebra@gmail.com", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')


        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            sys.exit()
            
           
        elif 'hello' in query:
            speak('Hello Sir')

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()
                                    
        elif 'play music' in query:
            os.startfile('E:\Videos')                  
            speak(' here  is your music! and few comedy videos Enjoy!')
            

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=3)
                    speak('Got it.')
                    speak('wikipedia says - ')
                    speak(results)
        
            except:
                webbrowser.open('www.google.com')
        
        speak('Next Command! Sir!')

        icon_path='E:\Robot'
