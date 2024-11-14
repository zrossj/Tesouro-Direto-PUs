from sqlalchemy import text, create_engine
import pandas as pd
from app.properties import AppProperties




def put_DB(df: pd.DataFrame):

    ppt = AppProperties()

    # parameters for db conection
    user = ppt.p.get('user').data
    password = ppt.p.get('password').data
    host = ppt.p.get('host').data
    port = ppt.p.get('port').data
    database = ppt.p.get('db').data


    uri = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'

    # creating engine with the database url passed
    engine = create_engine(uri)


    query = """ BEGIN;
                    CREATE TABLE br_treasury_titles
                    (
                        data date,
                        titulo varchar(64), 
                        taxa varchar(64), 
                        pu numeric(7,2), 
                        vencimento date,
                        ask_bid varchar(16)
                    );
                    
                    ALTER TABLE br_treasury_titles ADD CONSTRAINT "uniTiDaVen" UNIQUE (titulo, vencimento, data, ask_bid);
                    
                    COMMIT;
                    """


    cursor = engine.connect()
    try:
        cursor.execute(text(query))
        cursor.commit()
        cursor.close()

    except Exception as e:
        print(f"Ops! We got an error on the transactional block: {e}")



    # Inserting the Data (load phase); 

    with engine.connect() as con:

        try:
            df.to_sql(name = 'br_treasury_titles', 
                con=con,
                schema='public',
                if_exists='append',
                index=False)
            
        except:
            print('there is duplicated data')

    return "DB script executed!"