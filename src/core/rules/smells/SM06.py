
# Security Smell 06 - Uso de HTTP sem TLS - Transmissão de informações confidenciaisem texto claro (CWE-319)
from .lists.smells import *

class SM06:

    def __init__(self, token):
        self.token = token

    def validade(self):
        token = self.token

        cmd_directive = self.verify_cmd_directive(token)
        env_directive = self.verify_env_directive(token)

        if(cmd_directive):
            return cmd_directive

        if(env_directive):
            return env_directive
        
        return False


    def verify_env_directive(self, token):
        if(token.directive.lower() == "env" or token.directive.lower() == "arg"):
            if(self.includes_host(token.value[0]) and ("http://" in token.value[1] or ("https://" not in token.value[1] and "$" not in token.value[1]))):
                return {
                        "command": token.original, 
                        "start_line": token.start_line, 
                        "end_line": token.end_line, 
                        "security_smell": smells["SM06"]
                    }
        return False

    def verify_cmd_directive(self, token):
        if(token.directive.lower() == "cmd" or token.directive.lower() == "entrypoint"):
            for item in token.value:
                if("http://" in item):
                    return {
                            "command": token.original, 
                            "start_line": token.start_line, 
                            "end_line": token.end_line, 
                            "security_smell": smells["SM06"]
                        }
        return False


    def includes_host(self, string):
        return "host" in string.lower() or "url" in string.lower() or "domain" in string.lower() or "dominio" in string.lower()
