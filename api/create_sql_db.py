import sqlite3
import pandas as pd
from dbfread import DBF
import sys

"""
The data used for this script is from this website: https://www.glims.org/. You
got to make an account to download it and there are glims_polygons.dbf files
for different years. You can run this script several times for different glims
dbf files and add to the same database file. 
"""


if __name__ == "__main__":
    
    db_filename = None
    glims_file = None

    if len(sys.argv) != 3:
        print("Usage: create_sql_db.py <db_filename> <glims_polygon_filename>")
        quit()
    else:
        db_filename = sys.argv[1]
        glims_file = sys.argv[2]

    print(f"NOTE: running the program will create/modify {db_filename} using the contents from {glims_file}.\nPress y to continue.")
    choice = input().lower()
    if not choice in {"yes", "y", "ye", ""}:
        quit()
    
    # The data base file will be created if it does not already exist.
    con = sqlite3.connect(f"{db_filename}")
    cur = con.cursor()
    
    # If the glacier table exists, it will be dropped.
    cur.execute("CREATE TABLE IF NOT EXISTS glaciers (glacier_id TEXT, \
                                                      glacier_name TEXT, \
                                                      source_time TEXT, \
                                                      analysis_time TEXT, \
                                                      geo_area TEXT, \
                                                      area REAL, \
                                                      mean_elev INTEGER, \
                                                      min_elev INTEGER, \
                                                      max_elev INTEGER, \
                                                      UNIQUE (glacier_name, source_time));")
    con.commit()

    # If you want to read from a different glims data base, the file name below must be changed.
    for i, record in enumerate(DBF(glims_file, char_decode_errors="ignore")):

        # Here we iterate through all the records in the glim file.
        # Only the parameters below are stored in the sql db.
        
        glacier_id = record["glac_id"]
        glacier_name = record["glac_name"].replace("'", "").strip()
        source_time = record["src_date"]
        analysis_time = record["anlys_time"]
        geo_area = record["geog_area"]
        area = record["db_area"]
        mean_elev = record["mean_elev"]
        min_elev = record["min_elev"]
        max_elev = record["max_elev"]

        # Any empty glacier name and id will be ignored.
        if glacier_name == "None" and glacier_id == "None":
            continue
        print(i, glacier_name, glacier_id)

        cur.execute(f"INSERT OR REPLACE INTO glaciers (glacier_id, \
                                                       glacier_name, \
                                                       source_time, \
                                                       analysis_time, \
                                                       geo_area, \
                                                       area, \
                                                       mean_elev, \
                                                       min_elev, \
                                                       max_elev) \
                                            VALUES('{glacier_id}', \
                                                   '{glacier_name}', \
                                                   '{source_time}', \
                                                   '{analysis_time}', \
                                                   '{geo_area}', \
                                                    {area}, \
                                                    {min_elev}, \
                                                    {max_elev}, \
                                                    {mean_elev});")
        
    con.commit()
        
    print(pd.read_sql_query("SELECT * FROM glaciers", con))