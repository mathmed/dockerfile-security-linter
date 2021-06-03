# Security Smell 10 - Uso de funções ou comandos obsoletos
# O código usa funções descontinuadas ou obsoletas, o que sugere que o código não foi revisado ou mantido ativamente.
# CWE-477
from .lists.smells import *
from .lists.obsolete_linux_commands import *

class SM10:
    def __init__(self, token):
        self.token = token
    def validade(self):
        token = self.token

        run_directive = self.verify_run_directive(token)

        if(run_directive):
            return run_directive

        return False
    
    def verify_run_directive(self, token):
        if(token.directive.lower() in obsolete_linux_commands):
            return {
                    "command": token.original, 
                    "start_line": token.start_line, 
                    "end_line": token.end_line, 
                    "security_smell": smells["SM10"],
                    "code": "SM10"
                }
        return False


