# Text-to-Sound module
# Heeft als input text en levert een sound middels pyttsx3. De stemgeluiden worden door Windows geproduceerd.
#
# pip install pyttsx3
import pyttsx3
import sys

def SoundText(text):
  engine.say(text)
  engine.runAndWait()


engine = pyttsx3.init()                    # initialiseer pyttsx3
voices = engine.getProperty('voices')      # vraag de huidige stem op 
engine.setProperty('voice', voices[0].id)  # zet de stem, 1 for man 0 for vrouw

rate = engine.getProperty('rate')          # vraag de huidige snelhied van spreken op
engine.setProperty('rate', 150)            # zet de snelheid van spreken

stoptekst = "goodbye and hope to see you again"
starttekst = "Enter the text you want to hear, or QUIT to stop"

print(starttekst)
SoundText(starttekst)

while True:
  text = input('> ')
  if text.upper() == 'QUIT':
    SoundText(stoptekst)
    sys.exit()
  else:
    print(text)
    SoundText(text)
    

