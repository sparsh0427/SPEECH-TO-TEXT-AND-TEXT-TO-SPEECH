import win32com.client as wincl
import webbrowser
import speech_recognition as sr
import time

r=sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("SPEAK ANYTHING=:")
    audio=r.listen(source)
    try:
        print("YOU SAID=",r.recognize_google(audio))
    except:
        print("sorry not able to recognize you")


if("hello" in r.recognize_google(audio)):
    speak=wincl.Dispatch('SAPI.SpVoice')
    print("REPLY:HI SPARSH HOW ARE YOU")
    speak.speak("HI SPARSH HOW ARE YOU. what do you want me to do for you")

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("SPEAK ANYTHING=:")
    audio=r.listen(source)
    try:
        print("YOU SAID=",r.recognize_google(audio))
    except:
        print("sorry not able to recognize you")
    
if('open YouTube' in r.recognize_google(audio)):
    speak=wincl.Dispatch('SAPI.SpVoice')
    print("REPLY:OK")
    speak.speak("OK, OPENING YOUTUBE")    
    webbrowser.open_new_tab('www.youtube.com')

time.sleep(7)
    
speak=wincl.Dispatch('SAPI.SpVoice')
print("REPLY:OK")
speak.speak("WANT ME TO DO ANYTHING ELSE?") 

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("SPEAK ANYTHING=:")
    audio=r.listen(source)
    try:
        print("YOU SAID=",r.recognize_google(audio))
    except:
        print("sorry not able to recognize you")
        
if('yes' in r.recognize_google(audio)):
    speak=wincl.Dispatch('SAPI.SpVoice')
    print("REPLY:OK")
    speak.speak("OK, TELL ME I AM LISTENING")    

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("SPEAK ANYTHING=:")
    audio=r.listen(source)
    try:
        print("YOU SAID=",r.recognize_google(audio))
    except:
        print("sorry not able to recognize you")
        
if('joke' in r.recognize_google(audio)):
    speak=wincl.Dispatch('SAPI.SpVoice')
    print("REPLY:OK")
    speak.speak("hahahahahahahah")    

        