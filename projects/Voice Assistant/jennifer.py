import pyttsx3
import wolframalpha
import random
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import smtplib
import pywhatkit
from urllib.request import urlopen
from ecapture import ecapture as ec

# configuring our voice assistant
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
assName =("Jennifer")

# defining the speak function
def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning Sir !")

	elif hour>= 12 and hour<18:
		speak("Good Afternoon Sir !")

	else:
		speak("Good Evening Sir !")

	speak("I am your Voice Assistant")
	speak(assName)
	speak("How can i Help you, Sir")

# this function takes user command 
# and converts it to an executable query
def takeCommand():
	
	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language ='en-in')
		print(f"User said: {query}\n")

	except Exception as e:
		print(e)
		print("Unable to Recognize your voice.")
		return "None"
	
	return query

# function to send email to someone
def sendEmail(to, content):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	
	# Enable low security in gmail
	server.login('peakyblinder.mayank@gmail.com', 'Whysoserious?')
	server.sendmail('peakyblinder.mayank@gmail.com', to, content)
	server.close()

# driver program
if __name__ == '__main__':
    clear = lambda: os.system('cls')
     
    # This Function will clean any
    # command before execution of this python file
    clear()
    wishMe()

    while True:
         
        query = takeCommand().lower()
         
        # All the commands said by user will be
        # stored here in 'query' and will be
        # converted to lower case for easily
        # recognition of command
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
 
        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")
 
        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")
 
        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")  
 
        elif 'play music' in query or 'play song' in query:
            speak("Here you go with music")
            music_dir = "D:\\Songs\\Hindi_Songs"
            songs = os.listdir(music_dir)
            print(songs)   
            song = random.randint(0,6)
            os.startfile(os.path.join(music_dir, songs[song]))
 
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")   
            print(f"Sir, the time is {strTime}")
            speak(f"Sir, the time is {strTime}")
        
        elif 'how are you' in query:
            print("I am fine, Thank you")
            speak("I am fine, Thank you")
            print("How are you, Sir")
            speak("How are you, Sir")
        
        elif 'good' in query or 'fine' in query:
            print("Nice to hear that, What can I help you with?")
            speak("Nice to hear that, What can I help you with?")
        
        elif "who are you" in query or 'What is your name' in query:
            speak("My friends call me")
            speak(assName)
            print("My friends call me", assName)

        elif 'who made you' in query or 'who created you' in query:
            print("Two gentlemen named Mayank and Dev Krishna created me")
            speak("Two gentlemen named Mayank and Dev Krishna created me")
             
        elif 'joke' in query or 'tell a joke' in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)
        
        elif 'calculate' in query:
             
            app_id = "53RRWR-3PG84VJEX7"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)
        
        elif 'send email' in query:
            dict = {'ayush': 'ayushcoolz10@gmail.com', 'dev krishna': 'devkroy2001@gmail.com', 'k m sir': 'profkm4u@gmail.com','mayank':'mayanksharma5104@gmail.com'}
            try:
                speak("whom should i send")
                person = takeCommand().lower()
                to = dict[person]   
                speak("What should I say?")
                content = takeCommand()
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")
        
        elif 'exit' in query or 'quit' in query:
            print("Thanks for giving me your time sir")
            speak("Thanks for giving me your time sir")
            exit()

        elif 'play' in query:
            song = query.replace('play','')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'search' in query or 'google' in query:  
            query = query.replace("search", "")
            query = query.replace("google", "")
            webbrowser.open(query)

        elif  'what is' in query or 'who is' in query:
             
            # Use the same API key
            # that we have generated earlier
            app_id = "53RRWR-3PG84VJEX7"
            client = wolframalpha.Client(app_id)
            res = client.query(query)
             
            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results")

        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Jennifer_Cam", "img.jpg")
            speak("Photo taken")

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jennifer.txt', 'w')
            file.write(note)
            speak("Note taken")
         
        elif "show note" in query:
            speak("Showing Notes")
            file = open("jennifer.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")

        else:
            print("I didn't get you there, can you please repeat that")
            speak("I didn't get you there, can you please repeat that")
 


 
