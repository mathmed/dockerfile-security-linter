
# Security Smell 06 - Uso de HTTP sem TLS - Transmissão de informações confidenciaisem texto claro (CWE-319)
from .smells import *

class SM06:
    def __init__(self, token):
        self.token = token
    def validade(self):
        token = self.token

        run_directive = self.verify_run_directive(token)
        env_directive = self.verify_env_directive(token)

        if(env_directive):
            return env_directive
        if(run_directive):
            return run_directive

        return False

    def verify_env_directive(self, token):
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

    def verify_run_directive(self, token):
        if(token.directive.lower() == "run"):
            for command in token.value:
                for op in command.value:
                    if("http://" in op):
                        return {
                            "command": token.original, 
                            "start_line": token.start_line, 
                            "end_line": token.end_line, 
                            "security_smell": smells["SM06"]
                        }
        return False


