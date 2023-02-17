import sqlite3
import pandas as pd
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
  
app = Flask(__name__)
api = Api(app)

con = sqlite3.connect("glacier.db", check_same_thread=False)
cur = con.cursor()

print(pd.read_sql_query("SELECT * FROM glaciers", con))

cur.execute("select * from glaciers")
results = cur.fetchall()
print(len(results))


class Glacier(Resource):
    def __init__(self):
        self.name_arg = "name"
        self.list_all_arg = "list_all"
    def get(self):
        args = request.args
        if len(args) > 1:
            return "Too many args", 400
        elif self.list_all_arg in args.keys(): # dumps all the glacier names
            print(cur.execute("SELECT glacier_name FROM glaciers").fetchall())
            return jsonify({"listing all": f"hello world {args[self.list_all_arg]}"})
        elif self.name_arg in args.keys():
            return jsonify({"name": f"hello world {args[self.name_arg]}"})
        else:
            return "Invalid arg: require only 'name' or 'list_all' as arguments to URL", 400

api.add_resource(Glacier, "/glacier")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug = True)