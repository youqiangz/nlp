import json
from flask_restful import Api, Resource
from flask import request
from flask import Flask
import time


def creat_app():
    app = Flask(__name__)
    return app


app = creat_app()
api = Api(app)


class getInfo(Resource):
    def post(self):
        try:
            json_data = request.json
            res = self.process(json_data)
            return res
        except Exception as e:
            print(e)
            return {'code': 100, 'msg': '失败', 'data': []}

    def process(self, json_data):
        return json_data


api.add_resource(getInfo, '/learning/text_clasify')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, threaded=False)