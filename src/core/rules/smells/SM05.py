
# Security Smell 05 - Comentário suspeito - Comentário suspeito (CWE-546)
from .lists.smells import *
from .helpers.verifications import *

class SM05:

    def __init__(self, token):
        self.token = token
        
    def validade(self):

        token = self.token
        comment_directive = self.verify_comment_directive(token)

        if(comment_directive):
            return comment_directive

        return False


    def verify_comment_directive(self, token):

        # Verifica se o token é um comentário
        if(token.directive.lower() == "comment"):

            # Verifica se inclui uma sentença suspeita
            if(includes_suspicious_word(token.value.lower())):
                return {
                        "command": token.original, 
                        "start_line": token.start_line, 
                        "end_line": token.end_line, 
                        "security_smell": smells["SM05"],
                        "code": "SM05"
                    }
        return False


