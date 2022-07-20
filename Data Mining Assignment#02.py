#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns


# In[2]:


data = pd.read_csv('ds_salaries.csv')


# In[3]:


data.head()


# In[4]:


data.tail()


# In[5]:


data.describe()


# In[6]:


data.shape


# In[7]:


data.isnull().sum()


# In[8]:


data.nunique


# In[9]:


corelation = data.corr()


# In[14]:


sns.heatmap(corelation, xticklabels=corelation.columns, yticklabels=corelation.columns ,annot=True)


# In[15]:


sns.pairplot(data)


# In[12]:


sns.catplot(x='salary', kind='box', data=data)


# In[13]:


sns.catplot(x='salary_in_usd', kind='box', data=data)

