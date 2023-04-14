import sqlite3
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import sys

'''
This is the API that is connected to the sql database created from the glims
dataset. Currently, all it does is allow access to the glaciers, and its
corresponding info: source time, area, min elevation, max elevation, and mean
elevation. 
'''

'''
TODO: 

1. There still is no decoding of some of the glacier names according to the
glims documentation. That is one thing that should be added.

2. The precip wrapper is not connect to this api.

3. The http server is still a test server. 
'''


app = Flask(__name__)
api = Api(app)

db_filename = None

if len(sys.argv) != 2:
    print("Usage: glacier_api.py <db_filename>")
    quit()
else:
    db_filename = sys.argv[1]

# The data base we connect to is the one created by create_sql_db.py
con = sqlite3.connect(db_filename, check_same_thread=False)
cur = con.cursor()

class Glacier(Resource):
    '''
    This class serves all data pertaining to a Glacier.
    '''
    
    def __init__(self):
        self.get_name_arg = "name"
        self.get_id_arg = "id"
        self.get_list_all_arg = "list_all"
        self.post_name_arg = "glacier_names"
        self.post_id_arg = "glacier_ids"

    def get(self):
        '''
        URL must be in the form of http://localhost/glacier. There are three
        arguments: name, id, and list_all. 

        1. name={glacier_name} returns all data for the glacier with glacier_name.
        2. id={glaicer_id} returns all data for the glacier with glacier_id.
        3. list_all={true} returns all glaciers names and ids in the database.

        Note that only one of the three args can be used at a time. 
        '''
        
        args = request.args
        if len(args) > 1:
            return "Too many args", 400
        elif self.get_list_all_arg in args.keys(): # dumps all the glacier names
            if args[self.get_list_all_arg] == "true":
                return jsonify({"glaciers": cur.execute("SELECT glacier_id, glacier_name FROM glaciers").fetchall()})
            else:
                return jsonify({"glaciers": ""})
        elif self.get_name_arg in args.keys():
            data = cur.execute(f"SELECT glacier_id, source_time, analysis_time, geo_area, area, min_elev, max_elev, mean_elev FROM glaciers WHERE glacier_name=\"{args[self.get_name_arg]}\"").fetchall()
            data = [{"glacier_id": entry[0],
                     "source_time": entry[1],
                     "analysis_time": entry[2],
                     "geo_area": entry[3],
                     "area": entry[4],
                     "min_elev": entry[5],
                     "max_elev": entry[6],
                     "mean_elev": entry[7]   
                    } for entry in data]
            if len(data) == 0:
                return f"No data for glacier: '{args[self.get_name_arg]}'", 400
            else:
                return jsonify({f"{args[self.get_name_arg]}": data})
        elif self.get_id_arg in args.keys():
            data = cur.execute(f"SELECT glacier_name, source_time, analysis_time, geo_area, area, min_elev, max_elev, mean_elev FROM glaciers WHERE glacier_id=\"{args[self.get_id_arg]}\"").fetchall()
            data = [{"glacier_name": entry[0],
                     "source_time": entry[1],
                     "analysis_time": entry[2],
                     "geo_area": entry[3],
                     "area": entry[4],
                     "min_elev": entry[5],
                     "max_elev": entry[6],
                     "mean_elev": entry[7]   
                    } for entry in data]
            if len(data) == 0:
                return f"No data for glacier: '{args[self.get_id_arg]}'", 400
            else:
                return jsonify({f"{args[self.get_id_arg]}": data})
        else:
            return "Invalid arg: require only 'name', 'id', or 'list_all' as arguments to URL", 400

    def post(self):
        '''
        Send a json form with one key called glaciers with a list of glaciers to query.
        Here are some example curl commands:

        1. curl -X POST http://localhost/glacier -H "Content-Type: application/json" -d "{\"glacier_names\": [\"Gemu Glacier\", \"Grewingk Glacier\", \"Dogshead Glacier\"]}"  
        2. curl -X POST http://localhost/glacier -H "Content-Type: application/json" -d "{\"glacier_names\": [\"Gemu Glacier\"]}"
        3. curl -X POST http://localhost/glacier -H "Content-Type: application/json" -d "{\"glacier_ids\": [\"G083924E30412N\", \"G209046E59576N\"]}"
        4. curl -X POST http://localhost/glacier -H "Content-Type: application/json" -d "{\"glacier_ids\": [\"G207974E61361N\"]}"  

        If an item in the list is not a glacier in the database, nothing will be shown in the output.
        '''
        data = dict(request.get_json())
        if len(data) != 1 or not (bool(self.post_name_arg in data.keys()) ^ bool(self.post_id_arg in data.keys())):
            return f"Only one key required with name '{self.post_name_arg}' or '{self.post_id_arg}'.", 400
        elif self.post_name_arg in data.keys():
            glacier_list = data[self.post_name_arg]
            return_data = {}
            for glacier in glacier_list:
                print(glacier)
                data = cur.execute(f"SELECT glacier_id, source_time, analysis_time, geo_area, area, min_elev, max_elev, mean_elev FROM glaciers WHERE glacier_name=\"{glacier}\"").fetchall()
                data = [{"glacier_id": entry[0],
                         "source_time": entry[1],
                         "analysis_time": entry[2],
                         "geo_area": entry[3],
                         "area": entry[4],
                         "min_elev": entry[5],
                         "max_elev": entry[6],
                         "mean_elev": entry[7]   
                        } for entry in data]
                if len(data) != 0:
                    return_data[glacier] = data
            return jsonify(return_data)
        elif self.post_id_arg in data.keys():
            glacier_id_list = data[self.post_id_arg]
            return_data = {}
            for glacier_id in glacier_id_list:
                print(glacier_id)
                data = cur.execute(f"SELECT glacier_name, source_time, analysis_time, geo_area, area, min_elev, max_elev, mean_elev FROM glaciers WHERE glacier_id=\"{glacier_id}\"").fetchall()
                data = [{"glacier_name": entry[0],
                         "source_time": entry[1],
                         "analysis_time": entry[2],
                         "geo_area": entry[3],
                         "area": entry[4],
                         "min_elev": entry[5],
                         "max_elev": entry[6],
                         "mean_elev": entry[7]   
                        } for entry in data]
                if len(data) != 0:
                    return_data[glacier_id] = data
            return jsonify(return_data)

class Precipitation(Resource):
    
    def __init__(self):
        pass
    
    def get(self):
        pass

api.add_resource(Glacier, "/glacier")
api.add_resource(Precipitation, "/precip")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug = True)