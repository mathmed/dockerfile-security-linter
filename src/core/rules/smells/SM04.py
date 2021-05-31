
# Security Smell 04 - Vinculação com endereço IP impróprio - Controle de acesso inadequado (CWE-284)
from .helpers.smells import *

class SM04:
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
                if("0.0.0.0" in item):
                    return {
                            "command": token.original, 
                            "start_line": token.start_line, 
                            "end_line": token.end_line, 
                            "security_smell": smells["SM04"]
                        }
        return False

    def verify_run_directive(self, token):
        if(token.directive.lower() == "run"):
            for command in token.value:
                for op in command.value:
                    if("0.0.0.0" in op):
                        return {
                            "command": token.original, 
                            "start_line": token.start_line, 
                            "end_line": token.end_line, 
                            "security_smell": smells["SM04"]
                        }
        return False


