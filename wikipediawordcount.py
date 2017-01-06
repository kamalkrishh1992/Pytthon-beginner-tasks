# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 10:56:02 2017

@author: Admin
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 07:57:28 2017

@author: Admin
"""
import os

#read file
file = open('india.txt', 'r')
f1=file.read()
f2=f1

#total count of words
sum=0
for word in f1:
    sum=sum+1
print(sum)

# remove punctuation and numbers from the string            
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~1234567890'''
no_punct = ""
for char in f1:
   if char not in punctuations:
       no_punct = no_punct + char
f=no_punct

#create a list of words
f1=f.split()


#removing prepostions ,articles
f2=["An","an","a","the","and","in","by","th","at","with","its","for","The","He","he","to","she","they","of","Of","on","as","it","is","was","were","are","am"]
f3=[]
for i in f1:
    if i not in f2:
        f3.append(i)


s=set(f3)        
f4=list(s)
 


#count by words

m=[]
for i in f4:
    a=0    
    for j in f3:
        if i==j:
            a=a+1
        else:
            a=a
    m.append(a)    
    
#making a dictionary
x = dict(zip(f4, m))