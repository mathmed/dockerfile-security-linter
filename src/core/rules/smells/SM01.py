
# Security Smell 01 - Admin por padrão - Execução com privilégios desnecessários (CWE-250)
from .lists.smells import *

class SM01:

    def __init__(self, tokens):
        self.tokens = tokens

    def validade(self):

        tokens = self.tokens
        user_directive = self.verify_user_directive(tokens)

        if(user_directive):
            return user_directive

        return False

    # Recebe como parâmetro todos tokens do Dockerfile
    def verify_user_directive(self, tokens):
        for token in tokens:

            # Verifica se a diretiva em questão é user e o o usuário setado é root
            if(token.directive.lower() == "user"):
                if(token.value[0].lower() == "root"):
                    return {
                        "command": token.original, 
                        "start_line": token.start_line, 
                        "end_line": token.end_line, 
                        "security_smell": smells["SM01"],
                        "code": "SM01"
                    }
                else:
                    return False

        # Caso não encontrado a diretiva user, returna o smell pois o usuário padrão é o root
        return {
                "command": "Não utilização da diretiva USER", 
                "start_line": "", 
                "end_line": "", 
                "security_smell": smells["SM01"],
                "code": "SM01"
            }