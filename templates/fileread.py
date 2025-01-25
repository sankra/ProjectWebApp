import pandas as pd
from sqlalchemy import create_engine

database_url='postgresql://postgres:Admin123@localhost/paintings'
Engine= create_engine(database_url)
connection=Engine.connect()

files=['artist','canvas_size','image_link','museum','museum_hours','product_size','subject','work']
for file in files:
    df=pd.read_csv(f'C:/Users/sankr/OneDrive/Desktop/Full App Changes 20240112/Postgres/archive/{file}.csv')
    df.to_sql(file,con=connection, if_exists='replace', index=False)