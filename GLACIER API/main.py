from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
app = Flask(__name__)
api = Api(app)


class test_USA(Resource):
    def get(self):
        data = pd.read_csv('test_USA.csv')  # read CSV
        data = data.to_dict()  # convert dataframe to dictionary
        return {'data': data}, 200  # return data and 200 OK code

        
class CountryGlaciers(Resource):
    def get(self):
        df = pd.read_csv("dda.csv")
        countrycode = request.args.get('countrycode', default = "", type =  str)
        glacierName = request.args.get('glacierName', default = "", type = str)
        if glacierName == "":
            return_data = df.loc[df["POLITICAL_UNIT"] == countrycode]
            return_data = return_data.to_dict()
            return return_data, 200
        else:
            return_data = df.loc[df["POLITICAL_UNIT"] == countrycode]
            return_data = return_data.loc[df["NAME"] == glacierName]
            return return_data.to_dict(), 200


api.add_resource(test_USA, '/test') #glaciers is our entry point
api.add_resource(CountryGlaciers, '/countryglaciers') #countryglaciers is our entry point
if __name__ == '__main__':
    app.run()