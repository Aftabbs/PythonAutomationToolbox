#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Automatic Photo Compressor
You can also decrease the size of a picture by compressing it – while still keeping its quality.


# In[ ]:


import PIL
from PIL import Image
from tkinter.filedialog import *

fl=askopenfilenames()
img = Image.open(fl[0])
img.save("output.jpg", "JPEG", optimize = True, quality = 10)


# You can use the PIL (Python Imaging Library) to manipulate images, add filters, blurring, sharpening, smoothing, edge detection, compressing images and doing a lot to images.
