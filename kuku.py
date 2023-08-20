import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'lily' in command: 
                command = command.replace('lily', '')
                print(command)
    except:
        pass
    return command


def run_lily():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing'+ song)
        pywhatkit.playonyt(song)
    elif  'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is' + time)
    elif 'who is'  in command:
        person = command.replace('who is','')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'what is'  in command:
        person = command.replace('who is','')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)    
    elif 'when'  in command:
        person = command.replace('who is','')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'how'  in command:
        person = command.replace('who is','')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info) 
    elif 'date' in command:
        talk("sorry i am ai i can't")      
    elif 'are you single' in command:
        talk('no i am in relationship with wifi')
    elif 'do you have boyfriend' in command:
        talk("my boyfriend is wifi") 
    elif 'joke' in command: 
        talk(pyjokes.get_joke())   
        print(pyjokes.get_joke)
    elif 'u are beautyfull' in command:
        talk('thank you')  
    elif 'u are so cute' in command:
        talk('thank you')  
    elif 'u are great' in command:
        talk('thank you')            
    else :
        talk('plz say it again') 

run_lily()      
     