from flask import Flask, jsonify, request
from flask_restful import Resource, Api
  
app = Flask(__name__)
api = Api(app)

class Test(Resource):
    def get(self):
        return jsonify({'message': 'hello world'})

api.add_resource(Test, '/test') 

if __name__ == '__main__':
    app.run(port=80, debug = True)