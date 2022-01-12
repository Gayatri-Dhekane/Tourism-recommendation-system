#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv('topp100.csv')


# In[3]:


df.head()


# In[4]:


df['No of ratings'] = df['No of ratings'].str.replace(',', '')
df['No of ratings']=df['No of ratings'].astype(int)


# In[5]:


df.info()


# In[6]:


df.columns


# In[7]:


df["average rating"].fillna(4.5, inplace=True)
#sub2['income'].fillna((sub2['income'].mean()), inplace=True)


# ![image.png](attachment:image.png)
# ###  v  =  no. of ratings
# ###  m = minimum no. of ratings required
# ###  R = average ratings
# ###  C = mean of all ratings
# 

# In[8]:


def quizbased_recommender(df, percentile=0.8):
    #Ask for user preferences
    print("Place Type 1")
    Type_1 = input()
   
    print("Place Type 2")
    Type_2 = input()
    
    print("Place Type 3")
    Type_3 = input()
    
    
    #Filter based on the condition
   
    T1 = df.loc[df['type'].str.contains(Type_1, case=False)] 
    T2 = df.loc[df['type'].str.contains(Type_2, case=False)] 
    T3 = df.loc[df['type'].str.contains(Type_3, case=False)]
    T4=T1.append(T2)
    quiz=T4.append(T3)
    quiz.drop_duplicates()
    
    C = quiz['average rating'].mean()
    m = quiz['No of ratings'].quantile(percentile)
  
    #Only consider places that have higher than m votes. Save this in a new dataframe q_quiz
    q_quiz = quiz.copy().loc[quiz['No of ratings'] >= m]
    #Calculate score using the IMDB formula
    q_quiz['score'] = q_quiz.apply(lambda x:(x['No of ratings']/(x['No of ratings']+m) * x['average rating'])+ (m/(m+x['No of ratings']) * C),axis=1)
    #Sort place in descending order of their scores
    q_quiz = q_quiz.sort_values('score', ascending=False)
    return q_quiz  


# # Recommended for you....

# In[11]:


quizbased_recommender(df)


# In[ ]:




