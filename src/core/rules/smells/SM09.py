# Security Smell 09 - Uso de imagens Docker não oficiais - As imagens oficiais são mantidas pela empresa Docker e disponibilizadas no dockerhub
from .helpers.smells import *
from .helpers.official_docker_images import *

class SM09:
    def __init__(self, token):
        self.token = token
    def validade(self):
        token = self.token

        from_directive = self.verify_from_directive(token)

        if(from_directive):
            return from_directive

        return False
    
    def verify_from_directive(self, token):
        if(token.directive.lower() == "from"):
            image = token.value[0].split(":")[0]
            if(image not in official_docker_images):
                return {
                        "command": token.original, 
                        "start_line": token.start_line, 
                        "end_line": token.end_line, 
                        "security_smell": smells["SM09"]
                    }
        return False


