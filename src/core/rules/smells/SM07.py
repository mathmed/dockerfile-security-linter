
# Security Smell 07 - Uso de Algoritmos decriptografia fraca - Uso de algoritmo criptográfico quebrado ouinseguro ou intensidade de criptografia inadequado (CWE-327, 328)
from .helpers.smells import *

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
        if(token.directive.lower() == "run"):
            for command in token.value:
                for op in command.value:
                    if("md5" in op.lower() and self.includes_pass(op.lower())):
                        return {
                            "command": token.original, 
                            "start_line": token.start_line, 
                            "end_line": token.end_line, 
                            "security_smell": smells["SM07"]
                        }
        return False

    def includes_pass(self, string):
        return "pass" in string.lower() or "senha" in string.lower()

