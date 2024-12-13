import pandas as pd
import re
import datetime as dt


# recebe pd.dataframe 

def data_processing(dfs: list):

    print(dfs)
    assert len(dfs) == 2

    df_ask = dfs[0]
    df_bid = dfs[1]

    # new column marking
    df_ask['ask_bid'] = 'ask'
    df_bid['ask_bid'] = 'bid'


    df = pd.concat([df_ask, df_bid])

    # cleaning

    df = df.drop(columns = [4,5])

    # renaming cols 

    columns = ['titulo', 'taxa', 'pu', 'vencimento', 'ask_bid']
    df.columns = columns
    df = df.dropna(subset= ['vencimento']) 


    #numeric types;

    df.loc[:, 'pu'] = df.pu.str.replace("R$ ", '')
    df.loc[:, 'pu'] = df.pu.str.replace('.', '')
    df.loc[:, 'pu'] = df.pu.str.replace(',', '.')
    df['pu'] = df.pu.astype(float)

    ## datetime;


    df['vencimento'] = df.vencimento.apply(lambda x: dt.datetime.strptime(x, '%d/%m/%Y'))


    #

    assert df.duplicated(subset=['titulo', 'vencimento', 'ask_bid'], keep=False).sum() == 0 

    d0 = dt.date.today()
    df['data'] = d0

    return df