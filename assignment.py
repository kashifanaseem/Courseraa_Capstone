#!/usr/bin/env python
# coding: utf-8

# ## coverting wikipedia table into dataframe

# In[68]:


from bs4 import BeautifulSoup as bsoup
import lxml
import pandas as pd
from pandas import DataFrame
import numpy as np
import requests as req
from urllib.request import urlopen as ureq
print("done!")


# In[6]:


my_url= 'https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M'


# In[7]:


r= req.get(my_url)


# ## Parsing the web html file with BeautifulSoup packag

# In[8]:


page=bsoup(r.text,"html.parser")
page


# ## finding the table into the page

# In[13]:


table=page.table
table


# In[36]:


results=table.find_all('tr')
rows=len(results)
rows


# In[37]:


results[0:5]


# ## The Header of the DataFrame is the first row of data

# In[38]:


header=results[0].text.split()
header


# ## Let's check some rows in order to prepare to build the loop that will extract all cells into a DataFrame. For example, let's examine row 100

# In[39]:


text=results[100].text.split('\n')
text


# In[40]:


Postcode=text[1]
Postcode


# In[41]:


Borough=text[2]
Borough


# In[42]:


Neighborhood=text[3]
Neighborhood


# ## Iteration loop to extract all cells into a dataframe df

# In[47]:


records =[]
n=1
while n < rows :
    Postcode=results[n].text.split('\n')[1]
    Borough=results[n].text.split('\n')[2]
    Neighborhood=results[n].text.split('\n')[3]
    records.append((Postcode, Borough,Neighborhood))
    n=n+1

df=pd.DataFrame(records, columns=['PostalCode', 'Borough', 'Neighbourhood'])
df.head(5)


# In[48]:


df.shape


# In[49]:


df.tail()


# ## there are some rows with not assigned strings

# In[50]:


df[df['Borough']=='Not assigned'].count()


# In[51]:


df1=df[~df.Borough.str.contains("Not assigned")]                          #to drop those rows
df1=df1.reset_index(drop=True)


# In[56]:


df1.shape


# ## Let's examine the dataframe first to set up the best loop algorithm. How many unique postalcodes , Boroughs and Neighbourhood names are there?

# In[59]:


postalcodes = df1['PostalCode'].nunique()
boroughs = df1['Borough'].nunique()
neighbourhoods= df1['Neighbourhood'].nunique()
print('Unique Postalcodes : ' + str(postalcodes))
print('Unique Boroughs  : '+ str(boroughs))
print('Unique Neighbourhoods  :' + str(neighbourhoods))


# In[60]:


df1.head()


# In[61]:


rows1=len(df1)
rows1


# In[62]:


df2=df1
df2.head()      #copy of data frame


# In[64]:


rows2=len(df2)-1
rows2


# In[65]:


n=0

while n < nrows2 :
    post1=df2.iloc[n,0]
    m=n+1
    post2=df2.iloc[m,0]
    neigh1=df2.iloc[n,2]
    neigh2=df2.iloc[m,2]
    if post1==post2:
        df2.Neighbourhood[n,2] = neigh1=neigh1+','+neigh2
        df2=df2.drop(df2.index[m])
        nrows2=nrows2-1
        df2 = df2.reset_index(drop=True)
    else:
        n=n+1
df2.index


# In[66]:


df2.shape


# In[67]:


df2.head()


# In[ ]:




