#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Get SMILES of nitrosamines

import cirpy

data1 = []
with open("names.txt") as file:
    data = file.readlines()
      
    for molecule in data:
        name   = molecule.rstrip("\n\r")
        SMILES = cirpy.resolve(name, 'smiles')
        data1.append([name, SMILES])
        print (name, SMILES)


# In[3]:


data1


# In[5]:


import pandas as pd
df = pd.DataFrame(data1, columns=["nameNitrosamine","SMILES"])
print(df)


# In[8]:


df.to_csv('nitrosNamesSMILES.csv')


# In[ ]:




