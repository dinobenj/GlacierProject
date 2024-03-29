import sqlite3
import pandas as pd
import sys

'''
This is a simple database test script. Run it after creating the database and
inspect the output to make sure everything looks alright. Takes 1 command line
arg which is the name of the database.
'''

db_filename = None
if len(sys.argv) != 2:
    print("Usage: test_db.py <db_filename>")
    quit()
else:
    db_filename = sys.argv[1]


con = sqlite3.connect(db_filename, check_same_thread=False)
cur = con.cursor()

print(pd.read_sql_query("SELECT * FROM glaciers", con))
print(cur.execute(f"SELECT glacier_name, source_time FROM glaciers WHERE glacier_name=\"Gemu Glacier\"").fetchall())