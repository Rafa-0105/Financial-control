from flask import Flask
from flask_restx import Api, Resource


app = Flask(__name__)
api = Api(app)

@api.route('/get_results')
class GetExcel(Resource):
    def get(self):
        return True