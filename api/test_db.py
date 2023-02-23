import sqlite3
import pandas as pd

con = sqlite3.connect("glacier.db", check_same_thread=False)
cur = con.cursor()

print(pd.read_sql_query("SELECT * FROM glaciers", con))
print(cur.execute(f"SELECT glacier_name, source_time FROM glaciers WHERE glacier_name=\"Gemu Glacier\"").fetchall())