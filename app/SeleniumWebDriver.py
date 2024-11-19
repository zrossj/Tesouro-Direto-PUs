from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import re

import logging


log = logging.getLogger(__name__)
logging.basicConfig(filename = 'tesouroDireto.log')
log.info("SeleniumWeb Start")

class SeleniumWebDriver:

    def __init__(self):

        
        self.driver=webdriver.Firefox()
        log = logging.getLogger(__name__)
        

    def get_webpage_data(self, link):

        self.driver.get(link)
        #self.webpage_data = self.driver.page_source
        return self.driver.page_source


    def get_data_tables(self, link):


        self.soup = BeautifulSoup(self.get_webpage_data(link), 'html.parser')

        self.tables = self.soup.find_all('table') # for not duplicating data; more tables were found


        return self.tables
            