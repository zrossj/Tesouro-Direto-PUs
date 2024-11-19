import pandas as pd
import logging
from bs4 import BeautifulSoup
import re


def load_tables_pandas(html_tables: list) -> pd.DataFrame:
        
    log = logging.getLogger(__name__)
    
    dfs = []
    for soup_table in html_tables:
        
        row_set = []
        for row in soup_table.find_all('tr'):
            
            col_set = []

            for td in row.find_all('td'):
                col_set.append(td.text.strip())
            
            # regex to clean the data;
            try:
                col_set[0] = re.search('[a-zA-Z+\t ]+(\w*)' , col_set[0]).group().strip().replace('\t', '')
                
            except Exception as e:
                print(f"""Regex might failed while trying to matching pattern.
                    String value: {col_set}
                    {repr(e)}\n""")
                
            
            if len(col_set) >= 6: # slicing relevant and irregular data;
                col_set.pop(2)

            row_set.append(col_set)
        
        
        dfs.append(pd.DataFrame(row_set))
    
    log.info('get_raw_tables runned with sucess')

    return dfs