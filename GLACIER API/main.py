from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
app = Flask(__name__)
api = Api(app)

class test_USA(Resource):
    def get(self):
        data = pd.read_csv('test_USA.csv').to_dict()  # read CSV
        return {'data': data}, 200  # return data and 200 OK code

class CountryGlaciers(Resource):
    def get(self):
        df = pd.read_csv("dda.csv")
        country_code = request.args.get('countrycode', default = "", type = str)
        glacier_name = request.args.get('glacierName', default = "", type = str)
        if glacier_name == "":
            data = df.query(f"POLITICAL_UNIT == {country_code}").to_dict()
            return data, 200
        else:
            data = df.query(f"POLITICAL_UNIT == {country_code} and NAME == {glacier_name}").to_dict()
            return data, 200

# 
class GlaciersByYear(Resource):
    def get(self):
        df = pd.read_csv("dda.csv")
        


api.add_resource(test_USA, '/test') #glaciers is our entry point
api.add_resource(CountryGlaciers, '/countryglaciers') #countryglaciers is our entry point

if __name__ == '__main__':
    app.run()