
# Import the required module for text 
# to speech conversion
from gtts import gTTS
import librosa
import time
  
# This module is imported so that we can 
# play the converted audio
import os
  
with open("comments.txt","r") as f:
    for line in f:
        # The text that you want to convert to audio
        mytext = line[:len(line)-1]
        
        # Language in which you want to convert
        language = 'en'
        
        # Passing the text and language to the engine, 
        # here we have marked slow=False. Which tells 
        # the module that the converted audio should 
        # have a high speed
        myobj = gTTS(text=mytext, lang=language, slow=False)
        
        # Saving the converted audio in a mp3 file named
        # welcome 
        myobj.save("welcome.mp3")
        
        # Playing the converted file
        os.system("welcome.mp3")

        duration = librosa.get_duration(filename='welcome.mp3')
        time.slep(duration)