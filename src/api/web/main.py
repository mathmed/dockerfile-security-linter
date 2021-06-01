from flask import Flask
from flask_restful import Api
from .routes import routes

def main():

    app = Flask(__name__)
    api = Api(app)
    port = 5100
    routes(api)
    print("Aplicação WEB rodando")
    app.run(host="0.0.0.0", port=port, debug=True)
