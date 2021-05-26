
# Security Smell 03 - Credenciais definidas em texto claro - Uso de senha em texto claro (CWE-259)
from .smells import *

class SM03:
    def __init__(self, token):
        self.token = token
    def validade(self):
        token = self.token
        if(token.directive == "env"):
            if(self.includes_pass(token.value[0]) or self.includes_user(token.value[0])):
                if(len(token.value) >= 1 and token.value[1].replace(" ", "") != "''"):
                    return {
                        "command": token.directive, 
                        "start_line": token.start_line, 
                        "end_line": token.end_line, 
                        "security_smell": smells["SM03"]
                    }
        return False

    def includes_pass(self, string):
        return "pass" in string.lower() or "senha" in string.lower()

    def includes_user(self, string):
        return "user" in string.lower() or "usuario" in string.lower()

