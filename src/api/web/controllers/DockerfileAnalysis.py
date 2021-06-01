from flask_restful import Resource
from flask import  jsonify, request
from core.analysis.lexical.LexicalAnalysis import LexicalAnalysis
from core.rules.Engine import Engine


class DockerfileAnalysis(Resource):

    def post(self):
        try:

            json_data = request.get_json(force=True)
            lexical = LexicalAnalysis(json_data["dockerfile"])
            lexical.parse()
            tokens = lexical.get_tokens()
            result = Engine(tokens).run()

            if(len(result) > 0):
                return jsonify(result=Engine(tokens).run())
            else:
                return jsonify(result="Nenhuma vulnerabilidade encontrada")
                
        except:
            return jsonify(result="Erro ao realizar parse do Dockerfile")