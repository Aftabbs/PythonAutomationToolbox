#!/usr/bin/env python
# coding: utf-8

# Internet Speed Tester
# The OOKLA speed test API allows you to check the ping and internet speed. In addition to measuring the ping, this little automated project will measure the download and upload speeds.

# In[2]:


pip install speedtest-cli


# In[3]:


# Internet Speed tester
# pip install speedtest-cli
import speedtest as st

# Set Best Server
server = st.Speedtest()
server.get_best_server()

# Test Download Speed
down = server.download()
down = down / 1000000
print(f"Download Speed: {down} Mb/s")

# Test Upload Speed
up = server.upload()
up = up / 1000000
print(f"Upload Speed: {up} Mb/s")

# Test Ping
ping = server.results.ping
print(f"Ping Speed: {ping}")


# Although there are alternatives like fast.com, with this script you can quickly check for the internet speed using a Python script.
