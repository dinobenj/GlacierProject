import sqlite3
import pandas as pd
from dbfread import DBF

"""
The data used for this script is from this website: https://www.glims.org/.
You got to make an account to download it and there are glims_polygons.dbf files.
"""


if __name__ == "__main__":
    print("NOTE: running the program will create/overwrite glacier.db. press y to continue.")
    choice = input().lower()
    if not choice in {"yes", "y", "ye", ""}:
        quit()

    # The data base file will be created if it does not already exist.
    con = sqlite3.connect("glacier.db")
    cur = con.cursor()
    
    # If the glacier table exists, it will be dropped.
    cur.execute("DROP TABLE IF EXISTS glaciers;")
    cur.execute("CREATE TABLE glaciers (glacier_name TEXT, \
                                        source_time TEXT, \
                                        area REAL, \
                                        mean_elev INTEGER, \
                                        min_elev INTEGER, \
                                        max_elev INTEGER, \
                                        UNIQUE (glacier_name, source_time));")
    con.commit()

    # If you want to read from a different glims data base, the file name below must be changed.
    for i, record in enumerate(DBF("data/glims_polygons.dbf", char_decode_errors="ignore")):
        
        # Here we iterate through all the records in the glim file.
        # Only the parameters below are stored in the sql db.
        glacier_name = record["glac_name"].replace("'", "").strip()
        source_time = record["src_date"]
        area = record["db_area"]
        mean_elev = record["mean_elev"]
        min_elev = record["min_elev"]
        max_elev = record["max_elev"]
        
        # Any empty glacier name will be ignored.
        if glacier_name == "None":
            continue
        print(i, glacier_name)

        cur.execute(f"INSERT OR REPLACE INTO glaciers (glacier_name, \
                                                       source_time, \
                                                       area, \
                                                       mean_elev, \
                                                       min_elev, \
                                                       max_elev) \
                                            VALUES('{glacier_name}', \
                                                   '{source_time}', \
                                                    {area}, \
                                                    {min_elev}, \
                                                    {max_elev}, \
                                                    {mean_elev});")
        
    con.commit()
        
    print(pd.read_sql_query("SELECT * FROM glaciers", con))
