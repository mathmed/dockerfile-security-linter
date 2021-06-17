
# Security Smell 07 - Uso de Algoritmos decriptografia fraca - Uso de algoritmo criptográfico quebrado ouinseguro ou intensidade de criptografia inadequado (CWE-327, 328)
from .lists.smells import *
from .helpers.verifications import *

class SM07:

    def __init__(self, token):
        self.token = token
        
    def validade(self):
        token = self.token

        run_directive = self.verify_run_directive(token)

        if(run_directive):
            return run_directive

        return False

    def verify_run_directive(self, token):

        # Verifica se a diretiva é run
        if(token.directive.lower() == "run"):
            for command in token.value:
                for op in command.value:

                    # Verifica se o commando possui algum parâmetro com algoritmo fraco (eg: md5, sha1)
                    if(includes_weak_encryption(op)):
                        return {
                            "command": token.original, 
                            "start_line": token.start_line, 
                            "end_line": token.end_line, 
                            "security_smell": smells["SM07"],
                            "code": "SM07"
                        }
        return False

