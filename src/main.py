import json

from flask import Flask
from flask_restful import Resource, Api, reqparse
from API.prodData import prod_calculate

app = Flask(__name__)
api = Api(app)


class ProductionPlan(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()  # initialize

    def get(self):
        data = json.load(open("../example_payloads/payload1.json"))
        return {'data': data}, 200  # return data and 200 OK code

    def post(self):
        self.parser.add_argument('load', required=True, type=int)  # add arguments
        self.parser.add_argument('fuels', required=True, type=dict)
        self.parser.add_argument('powerplants', required=True, type=list, location='json')

        args = self.parser.parse_args()  # parse arguments to dictionary
        response = prod_calculate(**args)

        return response, 200  # return response with 200 OK


api.add_resource(ProductionPlan, '/productionplan')  # productionplan is our entry point

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=8888)  # run our Flask app
