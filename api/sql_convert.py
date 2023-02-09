import sqlite3
import pandas as pd
from dbfread import DBF



con = sqlite3.connect("glacier.db")
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS glaciers")
cur.execute("CREATE TABLE glaciers(glacier_name)")


for i, record in enumerate(DBF("data/glims_polygons.dbf")):
    print(record)
    if i > 1:
        break

print(pd.read_sql_query("SELECT * FROM glaciers", con))
