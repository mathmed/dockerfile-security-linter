
# Security Smell 01 - Admin por padrão - Execução com privilégios desnecessários (CWE-250)
from .smells import *

class SM01:
    def __init__(self, token):
        self.token = token
    def validade(self):
        if(self.token.directive == "user"):
            if(self.token.value[0] == "root"):
                return {
                    "command": self.token.directive, 
                    "start_line": self.token.start_line, 
                    "end_line": self.token.end_line, 
                    "security_smell": smells["SM01"]
                }
        return False