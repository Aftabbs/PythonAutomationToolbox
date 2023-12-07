#!/usr/bin/env python
# coding: utf-8

# In[5]:


pip install --upgrade pytube


# In[21]:


import pytube


# In[2]:


link = input('Youtube Video URL')
video_download = pytube.YouTube(link)
video_download.streams.first().download()
print('Video Downloaded', link)


# In[22]:


from pytube import YouTube
import pytube.exceptions


# In[6]:


from pytube import YouTube
import pytube.exceptions

try:
    link = input('Youtube Video URL: ')
    video_download = YouTube(link)
    custom_path =  r'C:\Users\Admin\Desktop\videodownloads'
    custom_filename = 'my_video.mp4'
    
    custom_full_path = custom_path + custom_filename
    
    video_download.streams.get_highest_resolution().download(output_path=custom_path, filename=custom_filename)
    
    print('Video Downloaded to:', custom_full_path)
except pytube.exceptions.PytubeError as e:
    print('An error occurred:', e)
except Exception as e:
    print('An unexpected error occurred:', e)


# # Low resolution

# In[ ]:


try:
    link = input('Youtube Video URL: ')
    video_download = YouTube(link)
    custom_path =  r'C:\Users\Admin\Desktop\videodownloads'
    custom_filename = 'my_video.mp4'
    
    custom_full_path = custom_path + custom_filename
    
    video_download.streams.get_lowest_resolution().download(output_path=custom_path, filename=custom_filename)
    
    print('Video Downloaded to:', custom_full_path)
except pytube.exceptions.PytubeError as e:
    print('An error occurred:', e)
except Exception as e:
    print('An unexpected error occurred:', e)


# # Mp4  to audio mp3

# In[23]:


try:
    link = input('Youtube Video URL: ')
    video_download = YouTube(link)
    custom_path =  r'C:\Users\Admin\Desktop\Mp3downloads'
    custom_filename = 'Kanye West - Cant Tell Me Nothing.mp3'
    
    custom_full_path = custom_path + custom_filename
    
    video_download.streams.get_audio_only().download(output_path=custom_path, filename=custom_filename)
    
    print('Audio Downloaded to:', custom_full_path)
except pytube.exceptions.PytubeError as e:
    print('An error occurred:', e)
except Exception as e:
    print('An unexpected error occurred:', e)


# # Custom Res -  Video resolution i.e. "720p", "480p", "360p", "240p", "144p"

# In[ ]:


try:
    link = input('Youtube Video URL: ')
    video_download = YouTube(link)
    custom_path =  r'C:\Users\Admin\Desktop\videodownloads'
    custom_filename = 'my_video.mp4'
    
    custom_full_path = custom_path + custom_filename
    
    video_download.streams.get_by_resolution().download(output_path=custom_path, filename=custom_filename)
    
    print('Video Downloaded to:', custom_full_path)
except pytube.exceptions.PytubeError as e:
    print('An error occurred:', e)
except Exception as e:
    print('An unexpected error occurred:', e)

