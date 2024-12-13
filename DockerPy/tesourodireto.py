#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import datetime as dt
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from app.data_processing import data_processing
from app.put_DB import put_DB
from app.table_load import load_tables_pandas
from app.SeleniumWebDriver import SeleniumWebDriver

import logging


# In[2]:


log = logging.getLogger(__name__)
logging.basicConfig(filename = 'tesouroDireto.log', level = logging.INFO)


# <h3> Selenium

# In[3]:


url = 'https://www.tesourodireto.com.br/titulos/precos-e-taxas.htm'
driver = SeleniumWebDriver()


# <h3> Scrapping HTML tables </h3>

# In[4]:


html_tables = driver.get_data_tables(url)


# <h3> Change to pandas DataFrame </h3>

# In[5]:


# load html tables to pandas dataframe

df_raw = load_tables_pandas(html_tables)


# ### Cleaning and Transforming

# In[9]:


# renaming of cols, dtypes, null values etc.

df = data_processing(df_raw)


# <h3> Putting On DB Postgres </h3>

# In[10]:


put_DB(df)


# In[ ]:





# In[ ]:




