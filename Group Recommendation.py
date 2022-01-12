#!/usr/bin/env python
# coding: utf-8

# # Group Recommender

# In[80]:


import pandas as pd
import numpy as np

#Import data 
df = pd.read_csv('group.csv')

#Print the top data
df.head()


# In[81]:


#combine 3 cols for calculating similarity
df['combcol'] = df[['grp_name', 'grp_type','state']].agg(' '.join, axis=1)
df.head()


# In[82]:


group_joined = [0 , 4 , 5]  # list which contains id of groups that user have joined.
print(len(group_joined))
user_profile='sam temple Ahmadnagar' #input user preferences


# In[83]:


#Import TfIdfVectorizer from the scikit-learn library
from sklearn.feature_extraction.text import TfidfVectorizer
# Import linear_kernel to compute the dot product
from sklearn.metrics.pairwise import linear_kernel


# In[84]:


# Function that takes in user profile(title) as input and gives recommendations 

def content_recommender(title, df=df):
    tfidf = TfidfVectorizer(stop_words='english')
    df2= pd.DataFrame()
    df2 = {'combcol': user_profile}
    df.append(df2, ignore_index = True)

    #Construct the required TF-IDF matrix by applying the fit_transform method on the combcol feature
    tfidf_matrix = tfidf.fit_transform(df['combcol'])


    #Output the shape of tfidf_matrix
    tfidf_matrix.shape
    # Compute the cosine similarity matrix
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
   
  
  
    
  

    # Get the pairwsie similarity scores of all group_details with that user profile
    # And convert it into a list of tuples as described above
    sim_scores = list(enumerate(cosine_sim[-1]))

    # Sort the groups based on the cosine similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar groups. Ignore the first group.
    sim_scores = sim_scores[1:11]

    # Get the group indices
    group_indices = [i[0] for i in sim_scores]

    # Return the top 10 most similar movies
    return df['grp_name'].iloc[group_indices]


# In[85]:



    
def content_recommender_grphist(title, df=df):
    tfidf = TfidfVectorizer(stop_words='english')
    df.drop(df.tail(1).index , inplace=True)
    #Construct the required TF-IDF matrix by applying the fit_transform method on the combcol feature
    tfidf_matrix = tfidf.fit_transform(df['combcol'])

    #Output the shape of tfidf_matrix
    tfidf_matrix.shape
   
    # Compute the cosine similarity matrix
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
  
    # Get the pairwsie similarity scores of all groups with that input group
    # And convert it into a list of tuples as described above
    
    sim_scores = list(enumerate(cosine_sim[title]))

    # Sort the groups based on the cosine similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar groups. Ignore the first group.
    sim_scores = sim_scores[1:11]

    # Get the group indices
    group_indices = [i[0] for i in sim_scores]
    similarity_indices = [i[1] for i in sim_scores]
    #print(type(df['grp_name'].iloc[group_indices]))
    # Return the top 10 most similar group
    newdf = pd.DataFrame() 
    newdf['grp_name'] = df['grp_name'].iloc[group_indices]
    newdf['score']= similarity_indices
    return newdf


# In[86]:


#if no. of groups joined by user are less than three we will recommend grps based on user profile
#else we will recommend grp based on similar grps

if(len(group_joined)<3):
    
    print(content_recommender(user_profile))
else:
    
    data = pd.DataFrame()
    for item in group_joined:
        data = data.append(content_recommender_grphist(item))
    #print(data)
    data2=data.sort_values(by=['score'],ascending=False)
    #print(data2)
    data2 = data.drop_duplicates(subset=['grp_name'], keep="first", inplace=False)
    #print(data2)
    print(data2.sort_values(by=['score'],ascending=False))
    

    
    
    


# In[ ]:





# In[ ]:




