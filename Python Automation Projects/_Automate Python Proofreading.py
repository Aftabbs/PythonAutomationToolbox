#!/usr/bin/env python
# coding: utf-8

# How to Automate Python Proofreading
# The first on the list is proofreading. Whenever you want to eliminate grammar and spelling mistakes from your writing, you can try this project that uses the Lmproof module.

# In[ ]:


# Python Proofreading
# pip install lmproof
import lmproof
def proofread(text):
    proofread = lmproof.load("en")
    correction = proofread.proofread(text)
    print("Original: {}".format(text))
    print("Correction: {}".format(correction))
    
proofread("Your Text")


# First, you'll need to install the lmproof library for this automation. Then you can use the function proofread() which takes in text as a parameter. The function runs and prints the original text that was passed into the function as well as the corrected text. You can use it to quickly proofread an essay or a short article.
