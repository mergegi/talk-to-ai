import pyttsx3

'''
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
volume = engine.getProperty('volume')   
print (volume)                          
engine.setProperty('volume',3.0)
engine.runAndWait()
'''



# speak out 'text' with rate as 'rate' and volume as 'volm' 
def speak(text, rate=125, volm=1): 
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', rate)
    engine.setProperty('vollume', volm)
    engine.say(text)
    engine.runAndWait()
    
speak("hello allison, the uwu girl", 100, 0.5)