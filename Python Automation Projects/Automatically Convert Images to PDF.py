#!/usr/bin/env python
# coding: utf-8

# Automatically Convert Images to PDF
# This is a very common task that you may perform often. You may want to convert a single image or multiple images into a PDF.
# 
# How to convert a single image to a PDF:

# In[ ]:


import os
import img2pdf
with open("output.pdf", "wb") as file:
   file.write(img2pdf.convert([i for i in os.listdir('path to image') if i.endswith(".jpg")]))


# How to convert multiple images to PDF:

# In[ ]:


from fpdf import FPDF
Pdf = FPDF()

list_of_images = ["wall.jpg", "nature.jpg","cat.jpg"]
for i in list_of_images:
   Pdf.add_page()
   Pdf.image(i,x,y,w,h)
   Pdf.output("result.pdf", "F")


# Here we're using the image2pdf library in Python to convert our image to a PDF. We can also convert multiple images to PDFs with just a few lines of code.
