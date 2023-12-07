#!/usr/bin/env python
# coding: utf-8

# Automatic Text to Speech
# We will make use of the Google Text to Speech API for this script. The API is up to date and works with many languages, pitches, and voices, that you can select from.

# In[ ]:


from pygame import mixer
from gtts import gTTS

def main():
   tts = gTTS('Like This Article')
   tts.save('output.mp3')
   mixer.init()
   mixer.music.load('output.mp3')
   mixer.music.play()
   
if __name__ == "__main__":
   main()


# In[ ]:




