import sqlite3
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
  
app = Flask(__name__)
api = Api(app)

con = sqlite3.connect("glacier.db")
cur = con.cursor()

class Glacier(Resource):
    def __init__(self):
        self.name_arg = "name"
        self.list_all_arg = "list_all"
    def get(self):
        args = request.args
        if len(args) > 1:
            return "Too many args", 400
        if not (self.name_arg in args.keys() or self.list_all_arg in args.keys()):
            return "Invalid arg: require 'name' or 'list_all'", 400
        else:
            return jsonify({"message": f"hello world {args}"})

api.add_resource(Glacier, "/glacier")

if __name__ == "__main__":
    app.run(port=80, debug = True)