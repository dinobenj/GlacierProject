import sqlite3
import pandas as pd
from flask import Flask, jsonify, request
from flask_restful import Resource, Api

'''
This is the API that is connected to the sql database created from the glims
dataset. Currently, all it does is allow access to the glaciers, and its
corresponding info: source time, area, min elevation, max elevation, and mean
elevation. 
'''


app = Flask(__name__)
api = Api(app)

# The data base we connect to is the one created by create_sql_db.py
con = sqlite3.connect("glacier.db", check_same_thread=False)
cur = con.cursor()

class Glacier(Resource):
    '''
    This class serves all data pertaining to a Glacier.
    '''
    
    def __init__(self):
        self.name_arg = "name"
        self.list_all_arg = "list_all"
        self.post_arg = "glaciers"

    def get(self):
        '''
        URL must be in the form of http://localhost/glacier?name={glacier_name}
        Returns all data points in the db listed for the glacier.
        '''
        args = request.args
        if len(args) > 1:
            return "Too many args", 400
        elif self.list_all_arg in args.keys(): # dumps all the glacier names
            if args[self.list_all_arg] == "true":
                return jsonify({"glaciers": cur.execute("SELECT glacier_name FROM glaciers").fetchall()})
            else:
                return jsonify({"glaciers": ""})
        elif self.name_arg in args.keys():
            data = cur.execute(f"SELECT source_time, area, min_elev, max_elev, mean_elev FROM glaciers WHERE glacier_name=\"{args[self.name_arg]}\"").fetchall()
            data = [{"source_time": entry[0],
                     "area": entry[1],
                     "min_elev": entry[2],
                     "max_elev": entry[3],
                     "mean_elev": entry[4]   
                    } for entry in data]
            if len(data) == 0:
                return f"No data for glacier: '{args[self.name_arg]}'", 400
            else:
                return jsonify({f"{args[self.name_arg]}": data})
        else:
            return "Invalid arg: require only 'name' or 'list_all' as arguments to URL", 400

    def post(self):
        '''
        Send a json form with one key called glaciers with a list of glaciers to query.
        Here are some example curl commands:
        curl -X POST http://localhost/glacier -H "Content-Type: application/json" -d "{\"glaciers\": [\"Gemu Glacier\", \"Grewingk Glacier\"]}"  
        curl -X POST http://localhost/glacier -H "Content-Type: application/json" -d "{\"glaciers\": [\"Gemu Glacier\"]}"
        If an item in the list is not a glacier in the database, nothing will be shown in the output.
        '''
        data = dict(request.get_json())
        if len(data) != 1 or not self.post_arg in data.keys():
            return f"Only one key required with name '{self.post_arg}'.", 400
        else:
            glacier_list = data[self.post_arg]
            return_data = {}
            for glacier in glacier_list:
                print(glacier)
                data = cur.execute(f"SELECT source_time, area, min_elev, max_elev, mean_elev FROM glaciers WHERE glacier_name=\"{glacier}\"").fetchall()
                data = [{"source_time": entry[0],
                        "area": entry[1],
                        "min_elev": entry[2],
                        "max_elev": entry[3],
                        "mean_elev": entry[4]   
                        } for entry in data]
                if len(data) != 0:
                    return_data[glacier] = data
            
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