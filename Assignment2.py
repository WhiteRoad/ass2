#!/usr/bin/env python
# coding: utf-8

# In[28]:


import re #module to provide for breaking strings into substrings, and replacing and extracting characters

def tokenize(string): #tokenize used in function is a lexical scanner for source code
    return re.compile('\w+').findall(string) #just reading for string function

from collections import Counter #a kind of dictionary that allows us to count the number of immutable objects

def probability(string): #part of code that considering string file by splitting and merging whole text
    text = tokenize(string.lower())
    word = Counter(''.join(text)) 
    return (dict(word))  

input = "Information" #actually it is our input, btw we tried to do it through txt file, but there was errmsg about not iterable int 
characters = probability(input) #considering all characters

for l in characters: #loop for probiding probability for each character
    print(l,characters[l]/sum(characters.values())) #output result


# In[ ]:





# In[ ]:





# In[ ]:




