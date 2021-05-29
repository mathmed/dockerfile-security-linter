
# Security Smell 01 - Admin por padrão - Execução com privilégios desnecessários (CWE-250)
from .smells import *

class SM01:

    def __init__(self, token):
        self.token = token

    def validade(self):

        token = self.token
        env_directive = self.verify_env_directive(token)

        if(env_directive):
            return env_directive

        return False

    def verify_env_directive(self, token):

        if(self.token.directive == "user"):
            if(self.token.value[0] == "root"):
                return {
                    "command": self.token.original, 
                    "start_line": self.token.start_line, 
                    "end_line": self.token.end_line, 
                    "security_smell": smells["SM01"]
                }
                
        return False