#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import json 
import requests
import pandas as pd
import numpy as np 
import streamlit as st
import datetime
from os import listdir
from os.path import isfile, join
import glob
import re
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt


# In[5]:


response = requests.get("http://api.open-notify.org/astros.json/?results=10")


# In[6]:


print(response.status_code)


# In[7]:


print(response.text)


# In[8]:


data1 = json.loads(response.text)
print(data1)


# In[9]:


count = 0
for key, value in data1.items():
        if isinstance(value, list):
              count += len(value)
print(count)


# In[11]:


for item in data1["people"]:
    name = (item["name"])  
    print(name)


# In[13]:

st.title("ISS Data")



# In[14]:

st.sidebar.subheader('Name of the Astrounauts')
for item in data1["people"]:
    name = (item["name"])  
    st.sidebar.text(name)  
    


# In[15]:

st.sidebar.subheader('Count of the Astronauts')
count = 0
for key, value in data1.items():
        if isinstance(value, list):
              count += len(value)
st.sidebar.text(count)




response2 = requests.get("http://api.open-notify.org/iss-now.json")
data2 = json.loads(response2.text)
data3 = pd.DataFrame.from_dict(data2)
data3 = data3.drop(columns=['timestamp', 'message'])

st.sidebar.subheader('Actual location of ISS')
st.sidebar.dataframe(data3)




# In[17]:
st.subheader('The current location of ISS in the map')
data3 =  data3.T
data3[["latitude", "longitude"]] = data3[["latitude", "longitude"]].apply(pd.to_numeric)
st.map(data3,zoom=(0))

# In[18]:
import datetime
now = datetime.datetime.now()
st.sidebar.subheader('The current time:')
st.sidebar.text(now)




# In[ ]:




