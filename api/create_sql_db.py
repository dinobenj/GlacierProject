import sqlite3
import pandas as pd
from dbfread import DBF



con = sqlite3.connect("glacier.db")
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS glaciers;")
cur.execute("CREATE TABLE glaciers (glacier_name TEXT, \
                                    UNIQUE(glacier_name));")


for i, record in enumerate(DBF("data/glims_polygons.dbf")):
    glacier_name = record["glac_name"]
    if glacier_name == "None":
        continue
    
    print(glacier_name)
    cur.execute(f"INSERT OR REPLACE INTO glaciers (glacier_name) VALUES('{glacier_name}');")
    if i > 50:
        break

print(pd.read_sql_query("SELECT * FROM glaciers", con))
