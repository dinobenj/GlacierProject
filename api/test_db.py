import sqlite3
import pandas as pd

con = sqlite3.connect("glacier.db", check_same_thread=False)
print(pd.read_sql_query("SELECT * FROM glaciers", con))
