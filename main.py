from flask import Flask, request
import pandas as pd
import py_eureka_client.eureka_client as eureka_client
from flask_pymongo import PyMongo

rest_port = 8055
eureka_client.init(eureka_server="http://eureka:8761/eureka",
                   app_name="manage-files",
                   instance_port=rest_port)

app = Flask(__name__)
app.config["MONGO_URI"] = 'mongodb://root:123456@mongo:27018/estadisticasApp?authSource=admin'
mongo = PyMongo(app)


@app.route('/prueba/', methods=["GET"])
def prueba():
    return "Conectado Python"


@app.route('/estadisticas/ver/', methods=["GET"])
def process():
    if request.method == 'GET':
        algorithm_collection = mongo.db.estadisticas
        statistics = algorithm_collection.find()
        print(type(statistics))
        print(statistics)
        return statistics


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=rest_port)
    # app.run(debug=True, port=rest_port)
