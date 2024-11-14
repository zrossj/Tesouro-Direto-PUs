from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import re


class SeleniumWebDriver:

    def __init__(self):

        self.driver=webdriver.Firefox()
    

    def get_webpage_data(self, link):

        self.driver.get(link)
        #self.webpage_data = self.driver.page_source
        return self.driver.page_source


    def get_data_tables(self, link):


        self.soup = BeautifulSoup(self.get_webpage_data(link), 'html.parser')

        self.tables = self.soup.find_all('table') # for not duplicating data; more tables were found

        return self.tables

    
    def get_raw_tables(self, link):
        
        self.dfs = []
        for soup_table in self.get_data_tables(link):
            
            row_set = []
            for row in soup_table.find_all('tr'):
                
                col_set = []

                for td in row.find_all('td'):
                    col_set.append(td.text.strip())
                
                # regex to clean the data;
                try:
                    col_set[0] = re.search('[a-zA-Z+\t ]+(\w*)' , col_set[0]).group().strip().replace('\t', '')
                    print('regex WORKED!')
                except Exception as e:
                    print(f'regex failed in: {col_set}\n{e}')
                    
                
                if len(col_set) >= 6: # slicing relevant and irregular data;
                    col_set.pop(2)

                row_set.append(col_set)
            
            
            self.dfs.append(pd.DataFrame(row_set))

        return self.dfs
            