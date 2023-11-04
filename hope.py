import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
from PyDictionary import PyDictionary
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[33].id)
# You can change this number to your voice preference, this is the one that I liked the most -yarnav
dictionary = PyDictionary()
note_list = []
wsp_list = []


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
            if command.startswith('hope'):
                # You can change the word hope for any name you like -yarnav
                command = command.replace('hope', '', 1)  # Remove "hope" only once -yarnav
            else:
                talk("Please repeat yourself, I couldn't understand")
                command = ""
                # Reset command if "hope" is not detected -yarnav
    except:
        command = ""
    return command


def run_hope():
    command = take_command()
    print(command)
    if 'play' in command:
        # This allows you to play a song on youtube -yarnav
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'introduce yourself' in command:
        talk('Hello there, my name is hope and i am the virtual assistant of Yarnav')
    elif 'say hi to' in command:
        name = command.replace('say hi to', '')
        talk('Hello' + name + ' nice to meet you')
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        talk('Currently its' + time)
    elif 'search' in command:
        search = command.replace('search', '')
        info = wikipedia.summary(search, 3)
        print(info)
        talk(info)
    elif 'date' in command:
        date = datetime.datetime.now().strftime('%d/%m/%y')
        talk('today is' + date)
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
    elif 'send message' in command:
        with sr.Microphone() as source:
            print('Who will be the receiver?')
            voice = listener.listen(source)
            contact = listener.recognize_google(voice)
            contact = contact.lower()
            contact = str(contact)
            if 'mom' in contact:
                wsp_list.append('')
                # Here you can write a phone number, make sure to add +... -yarnav
                reciever = wsp_list[0]
                reciever = str(reciever)
                print("saved")
                with sr.Microphone() as source:
                    print('What is the message?')
                    voice = listener.listen(source)
                    message = listener.recognize_google(voice)
                    message = message.lower()
                    message = str(message)
                    wsp_list.append(message)
                    print("saved")
                    with sr.Microphone() as source:
                        print('send message?')
                        voice = listener.listen(source)
                        send = listener.recognize_google(voice)
                        send = send.lower()
                        send = str(send)
                        if 'yes' in send:
                            hour = datetime.datetime.now().strftime('%H')
                            hour = int(hour)
                            wsp_list.append(hour)
                            minute = datetime.datetime.now().strftime('%M')
                            minute = int(minute)
                            minute = minute+1
                            wsp_list.append(minute)
                            pywhatkit.sendwhatmsg(reciever, message, hour, minute)
                        elif 'no' in send:
                            wsp_list.clear()
                            talk('message deleted')

            else:
                talk("I'm sorry, this person is not on your contacts")
                pass

while True:
    run_hope()
