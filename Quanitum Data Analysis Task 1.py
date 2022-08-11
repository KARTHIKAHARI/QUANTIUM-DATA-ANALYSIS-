#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[15]:


dataset = pd.read_excel(r'C:\Users\karth\Desktop\Data Analysis\Quanitum\QVI_transaction_data.xlsx')


# In[16]:


dataset.head()


# # Summary 

# In[17]:


dataset.describe()


# # Checking for Nulls

# In[18]:


dataset.isnull().sum()


# In[ ]:


#No nulls are present in this dataset.


# # Checking for Outliers

# In[19]:


sns.boxplot(dataset.TOT_SALES)


# In[20]:


#Cant get a proper idea from this boxplot 


# In[21]:


#Plotting a Histogram 


# In[22]:


sns.distplot(dataset.TOT_SALES, kde = True)


# In[23]:


#We see that the data is distributed mostly below 100 and outlier is around 600.We need to clean this.


# In[24]:


#From the data summary we see that mean value in the column TOT_SALES is ~7.3


# In[27]:


numericdata = dataset.select_dtypes('float','int')


# In[28]:


numericdata.head()


# In[29]:


numericdata = dataset.select_dtypes(['float','int'])


# In[30]:


numericdata.head()


# # Data Cleaning

# In[31]:


#I am going to remove the outlier


# In[32]:


x = numericdata[numericdata['TOT_SALES']< 8.000]


# In[33]:


sns.distplot(x.TOT_SALES, kde = False)


# In[34]:


#Lets plot a boxplot to see the dataset after removing the outliers


# In[35]:


sns.boxplot(x.TOT_SALES)


# In[36]:


#From the boxplot we see that the outliers have been removed.


# # So we created and interpreted high level summaries of data. Also removed the outliers present in the dataset.

# # •	Checking data formats  

# In[37]:


dataset.dtypes


# In[38]:


#There is no error in the data format


# In[ ]:




