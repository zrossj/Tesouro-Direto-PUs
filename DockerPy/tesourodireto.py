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




log = logging.getLogger(__name__)
logging.basicConfig(filename = 'tesouroDireto.log', level = logging.INFO)


# <h3> Selenium




url = 'https://www.tesourodireto.com.br/titulos/precos-e-taxas.htm'
driver = SeleniumWebDriver()


html_tables = driver.get_data_tables(url)

df_raw = load_tables_pandas(html_tables)

df = data_processing(df_raw)

put_DB(df)


