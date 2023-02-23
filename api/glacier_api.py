import sqlite3
import pandas as pd
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
  
app = Flask(__name__)
api = Api(app)

con = sqlite3.connect("glacier.db", check_same_thread=False)
cur = con.cursor()

class Glacier(Resource):
    def __init__(self):
        self.name_arg = "name"
        self.list_all_arg = "list_all"
    def get(self):
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
            print(data)
            if len(data) == 0:
                return f"No data for glacier: \"{args[self.name_arg]}\"", 400
            else:
                return jsonify({f"{args[self.name_arg]}": data})
        else:
            return "Invalid arg: require only 'name' or 'list_all' as arguments to URL", 400

api.add_resource(Glacier, "/glacier")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug = True)