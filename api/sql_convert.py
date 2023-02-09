import sqlite3
from dbfread import DBF

for record in DBF("data/glims_polygons.dbf"):
    print(record)