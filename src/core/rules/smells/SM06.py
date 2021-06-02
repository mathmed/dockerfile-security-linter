
# Security Smell 06 - Uso de HTTP sem TLS - Transmissão de informações confidenciaisem texto claro (CWE-319)
from .lists.smells import *
from .helpers.verifications import *

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
        directive = token.directive.lower()
        if(directive == "env" or directive == "arg"):

            if(directive == "arg"):
                sentence = token.value[0].split("=")
                key = sentence[0]
                value = "" if len(sentence) == 1 else sentence[1] 
            else:
                key = token.value[0]
                value = token.value[1]

            if(includes_host(key) and ("http://" in value or ("https://" not in value and "$" not in value))):
                return {
                        "command": token.original, 
                        "start_line": token.start_line, 
                        "end_line": token.end_line, 
                        "security_smell": smells["SM06"]
                    }
        return False

    def verify_cmd_directive(self, token):
        directive = token.directive.lower()
        if(directive == "cmd" or directive == "entrypoint"):
            for item in token.value:
                if("http://" in item):
                    return {
                            "command": token.original, 
                            "start_line": token.start_line, 
                            "end_line": token.end_line, 
                            "security_smell": smells["SM06"]
                        }
        return False


