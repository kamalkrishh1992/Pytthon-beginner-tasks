# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 07:53:18 2016

@author: Admin
"""
            
            
import pandas 
f1 = pandas.read_excel(open('doc1.xlsx','rb'), sheetname='Sheet2')           
f2 = pandas.read_excel(open('doc2.xlsx','rb'), sheetname='Sheet1')

n1list=[]
i=0
while i < 32:
  n1list.append(f1['ContactName'][i])              
  #print(f1['ContactName'][i])
  i+=1                
  
a1list=[]
i=0
while i < 32:
  a1list.append(f1['Address'][i])              
  #print(f1['Address'][i])
  i+=1   

n2list=[]
i=0
while i < 32:
  n2list.append(f2['ContactName'][i])              
  #print(f2['ContactName'][i])
  i+=1                
  
a2list=[]
i=0
while i < 32:
  a2list.append(f2['Address'][i])              
  #//print(f2['Address'][i])#
  i+=1   
  

    
    
list = pandas.DataFrame(
    {'Name1': n1list,
     'Address1': a1list,
     'Name2': n2list,
     'Address2': a2list,
    })

table = pandas.DataFrame(list) 
writer = pandas.ExcelWriter('Scores3.xlsx')
table.to_excel(writer, 'Scores 1')
writer.save()
                 

   


  
mat=[]
i=0 
while i<len(n1list):
  name1=n1list[i].split()
  j=0  
  #print (name1)
  while j<len(n2list):
            name2=n2list[j].split()
            #print (name2)
            k=0
            match=0
            while k<(len(name1)):
             l=0
             while l<(len(name2)):
                #print (name1[k])
               if name1[k]==name2[l]:
                  match=match+1
                  #print (name1[k],name2[l],match)
                  l=l+1
               else:
                  match=match
                  #print (name1[k],name2[l],match)                 
                  l=l+1
             k=k+1
            mat.append(match)
            j=j+1            
            #print(j)
        #mat.append(match)
        #print (k)
  #mat.append(match)
  #print (match)       
  i=i+1
  #print(i)       
  
amat=[]
i=0 
while i<len(a1list):
  add1=a1list[i].split()
  j=0  
  #print (name1)
  while j<len(a2list):
            add2=a2list[j].split()
            #print (name2)
            k=0
            match=0
            while k<(len(add1)):
             l=0
             while l<(len(add2)):
                #print (name1[k])
               if add1[k]==add2[l]:
                  match=match+1
                  #print (name1[k],name2[l],match)
                  l=l+1
               else:
                  match=match
                  #print (name1[k],name2[l],match)                 
                  l=l+1
             k=k+1
            amat.append(match)
            j=j+1            
            #print(j)
        #mat.append(match)
        #print (k)
  #mat.append(match)
  #print (match)       
  i=i+1
  #print(i)       
  
i=0
namelist1=[]
namelist2=[]
while i<len(n2list):
  name2=n1list[i].split()
  j=0  
  #print (name1)
  while j<len(n1list):
     name1=n2list[j].split()
     namelist1.append(name1)
     namelist2.append(name2)
     j=j+1
  i=i+1    
  
i=0
alist1=[]
alist2=[]
while i<len(a2list):
  add2=a1list[i].split()
  j=0  
  #print (name1)
  while j<len(a1list):
     add1=a2list[j].split()
     alist1.append(add1)
     alist2.append(add2)
     j=j+1
  i=i+1   
  

AP=[]  
i=0    
while i<1024:
    ap=mat[i]/len(alist2[i])
    AP.append(round(ap*100,-1))
    i=i+1    
    
NP=[]
i=0    
while i<1024:
    np=mat[i]/len(namelist2[i])
    NP.append(round(np*100,-1))
    i=i+1

listnew2 = pandas.DataFrame(
    {'Name1': namelist1,
     'Address1': alist1,
     'Name2': namelist2,
     'Address2': alist2,
     'NameMatchcount' :mat,
     'AddMatchcount' :amat,
     'Namepercent' :NP,
     'Addpercent' :AP,
    })
    
    
table = pandas.DataFrame(listnew2) 
writer = pandas.ExcelWriter('Scores30.xlsx')
table.to_excel(writer, 'Scores 1')
writer.save()
                     
    