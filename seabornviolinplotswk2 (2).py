#!/usr/bin/env python
# coding: utf-8

# In[1]:


from matplotlib import pyplot as plt
import seaborn as sns;
import pandas as pd;


# In[2]:


my_data = pd.read_csv('gapminder_with_codes(1).csv');





# In[4]:


sns.set(style= 'whitegrid', palette= 'pastel', color_codes= True);


# In[8]:


sns.violinplot(y=my_data.gdpPercap);


# In[5]:


sns.violinplot(x=my_data.lifeExp);


# In[6]:


sns.violinplot(y=my_data.gdpPercap, x=my_data.lifeExp);


# In[ ]:




