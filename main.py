import speech_recognition
import pyttsx3
import pyaudio
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener= speech_recognition.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with speech_recognition.Microphone() as source:
            print("listening......")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if "alexa" in command:
               command= command.replace("alexa",'')

    except:
        pass
    return command

def run_alexa():
    command=take_command()
    print(command)
    if "play" in command:
        video= command.replace('play','')
        talk('playing'+video)
        print('--->playing'+video)
        pywhatkit.playonyt(video)
    elif 'time' in command:
        time=datetime.datetime.now().strftime("%I:%M %p")
        talk(time)
        print("--->"+time)
    elif "your name" in command:

        talk('My name is alexa')

    elif "my name" in command:

        talk('Your name is arshad pasha')


    elif "how are you" in command:

        talk('Thanks for asking, i am good')


    elif 'joke' in command:
        joke=pyjokes.get_joke()
        print("--->"+joke)
        talk(joke)

    elif "who" or 'what' in command:
        if 'who is' in command:
            person=command.replace("who is",'')
            info=wikipedia.summary(person, sentences=1,auto_suggest=False)
            print("--->" + info)
            talk(info)

        elif 'what is' in command:
            thing=command.replace("what is",'')
            info1= wikipedia.summary(thing, sentences=1,auto_suggest=False)
            print("--->" + info1)
            talk(info1)

    else:
        talk('sorry.....')

while True:
    run_alexa()

