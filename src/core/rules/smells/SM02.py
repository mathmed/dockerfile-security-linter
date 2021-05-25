
# Security Smell 02 - Senha vazia - Senha vazia no arquivo de configuração (CWE-258)
from .smells import *

class SM02:
    def __init__(self, token):
        self.token = token
    def validade(self):
        token = self.token
        if(token.directive == "env"):
            if(self.includes_pass(token.value[0])):
                if(len(token.value) >= 1 and token.value[1].replace(" ", "") == "''"):
                    return {
                        "command": token.directive, 
                        "start_line": token.start_line, 
                        "end_line": token.end_line, 
                        "security_smell": smells["SM02"]
                    }
        return False

    def includes_pass(self, string):
        return "pass" in string.lower() or "senha" in string.lower()

