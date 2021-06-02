
# Security Smell 05 - Comentário suspeito - Comentário suspeito (CWE-546)
from .lists.smells import *
from .lists.suspicious_words import *

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
        if(token.directive.lower() == "comment"):
            if(self.includes_suspicious_word(token.value.lower())):
                return {
                        "command": token.original, 
                        "start_line": token.start_line, 
                        "end_line": token.end_line, 
                        "security_smell": smells["SM05"]
                    }
        return False

    def includes_suspicious_word(self, sentence):
        for word in suspicious_words:
            if(word in sentence):
                return True
