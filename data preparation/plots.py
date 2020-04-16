#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib as plt

df = pd.read_csv('u.data', sep = '\t') 
df.columns = ['user','movie','rate','timestamp']
df = df.drop(['timestamp'], axis = 1)


# In[2]:


df = df.pivot(index='user', columns='movie', values='rate')   
df.head()


# In[3]:


means = df.mean(axis=1)
means.head()


# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')
mean_plot = means.plot.hist(bins=20 )
mean_plot.set_xlabel("User's rating mean")
mean_plot.set_ylabel("Number of users")


# In[5]:


stds = df.std(axis=1)
mean_plot = stds.plot.hist(bins=20 )
mean_plot.set_xlabel("User's rating std")
mean_plot.set_ylabel("Number of users")


# In[6]:


df= df.sub(df.mean(axis=1),axis=0)
df.head()


# In[7]:


df.fillna(value=0, inplace= True)
df.head()


# In[8]:


df = df.add(abs(df.min().min()))
df.head()


# In[9]:


users_one_hot = pd.get_dummies(df.index)
users_one_hot.head()
