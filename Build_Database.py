import pathlib
import sqlite3
import pandas as pd
from pathlib import Path

path = Path.cwd()

def create_db(db_name, filename, table_name):
    file_path = path/filename
    con = sqlite3.connect(db_name)
    print('DB Build Success.')
    cursor = con.cursor()
    Sleep_Health = pd.read_csv(file_path)
    Sleep_Health.to_sql(table_name,con,index = False, if_exists ='replace')
    results = cursor.execute(f"select count(*) from {table_name}").fetchall()
    print(f'Data Imported Successfully.\n{results[0][0]} Rows Inserted.')
    con.commit()
    con.close()

if __name__=="__main__":
    db_name = "Health.db"
    filename = "Sleep_health_and_lifestyle_dataset.csv"
    table_name = "Sleep_Health"
    create_db(db_name, filename, table_name)
