
# Security Smell 08 - Permissão total ao sistema de arquivos - Atribuição de Permissão Incorreta para Recurso Crı́tico (CWE-732)
from .lists.smells import *
from .helpers.verifications import *

class SM08:
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
                if(command.directive.lower() == "chmod" or command.directive.lower() == "mkdir"):
                    for op in command.value:
                        if(includes_permission(op)):
                            return {
                                "command": token.original, 
                                "start_line": token.start_line, 
                                "end_line": token.end_line, 
                                "security_smell": smells["SM08"],
                                "code": "SM08"
                            }
        return False


