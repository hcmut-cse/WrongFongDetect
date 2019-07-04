#!/usr/bin/env python
# coding: utf-8

# In[74]:


import numpy as np
from PyPDF2 import PdfFileReader
import PyPDF2

def isHaveWrongFont(filename):
    WrongEncodeFont = 0
    file = open(filename, "rb")
    source = PdfFileReader(file)
    numPages = source.getNumPages()
    
    for p in range(numPages):
        page = source.getPage(p)
    
        #print("Page: ")
        #print(page)
        
        Resources = page['/Resources'].getObject()
        
        #print("Resources: ")
        #print(Resources)
        
        # print(type(Resources))
            
        Font = Resources['/Font'].getObject()
        
        #print("Font: ")
        #print(Font)
        
        for font in Font:
            listFont = Font[font].getObject()
            #print(listFont)
            if('/Encoding' in listFont):
                Encode = listFont['/Encoding'].getObject()
                if (Encode == '/Identity-H'):
                    WrongEncodeFont = 1
                
    return WrongEncodeFont


# In[75]:


# filename = 'tiengviet2.pdf'


# In[76]:


# print(isHaveWrongFont(filename))


# In[77]:


import glob

path="*.pdf"
files=glob.glob(path)


# In[78]:


for filename in files:
        # file = os.listdir()
        # file = list(filter(lambda ef: ef[0] != "." and ef[-3:] == "pdf", file))
        # Covert PDF to string by page
        print("==============================================================")
        print("Filename:" , filename)
        
        if(isHaveWrongFont(filename) == 0):
            print("Khong co Font Encoding sai")
        else:
            print("Co Font Encoding sai")


# In[ ]:




