#!/usr/bin/env python
# coding: utf-8

# Automatic PDF to CSV Converter
# Sometimes you'll need to convert pdf data to CSV (comma separated value) data so you can use it for further analysis. In those cases, this script can come in handy.

# In[ ]:


import tabula

filename = input("Enter File Path: ")
df = tabula.read_pdf(filename, encoding='utf-8', spreadsheet=True, pages='1')

df.to_csv('output.csv')


# You'll need to install the tabula library using pip in order to run this code. After installation you can pass the file into your project.
# 
# The library comes with a function read_pdf() which takes the file and reads it. You finish the automation by using the to_csv() function to convert the output into CSV.
