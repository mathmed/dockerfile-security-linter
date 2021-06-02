
# Security Smell 01 - Admin por padrão - Execução com privilégios desnecessários (CWE-250)
from .lists.smells import *

class SM01:

    def __init__(self, token):
        self.token = token

    def validade(self):

        token = self.token
        user_directive = self.verify_user_directive(token)

        if(user_directive):
            return user_directive

        return False

    def verify_user_directive(self, token):

        if(token.directive.lower() == "user"):
            if(token.value[0].lower() == "root"):
                return {
                    "command": self.token.original, 
                    "start_line": self.token.start_line, 
                    "end_line": self.token.end_line, 
                    "security_smell": smells["SM01"]
                }
                
        return False