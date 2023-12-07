#!/usr/bin/env python
# coding: utf-8

# How to Automate Playing Random Music
# While working, many devs love listening to music. So for music lovers (like me), this script randomly picks a song from a folder containing songs and plays it with the help of the OS and random modules in Python.

# In[ ]:


import random, os
music_dir = 'E:\\music diretory'
songs = os.listdir(music_dir)

song = random.randint(0,len(songs))

# Prints The Song Name
print(songs[song])  

os.startfile(os.path.join(music_dir, songs[0])) 


# The code goes to the music directory containing all the songs you want to play, and puts them all in a list. Then it randomly plays each song one after the other. The os.startfile plays the song.
