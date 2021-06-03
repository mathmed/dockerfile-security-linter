
# Security Smell 03 - Credenciais definidas em texto claro - Uso de senha em texto claro (CWE-259)
from .lists.smells import *
from .helpers.verifications import *

class SM03:
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
        directive = token.directive.lower()
        if(directive == "env" or directive == "arg"):
            for env in token.value:
                key, value = env[0], env[1]
                if(includes_pass(key) or includes_user(key) or includes_key(key)):
                    if(len(value) >= 1 and value.replace(" ", "") != "''" and "$" not in value):
                        return {
                            "command": token.original, 
                            "start_line": token.start_line, 
                            "end_line": token.end_line, 
                            "security_smell": smells["SM03"]
                        }
        return False

    def verify_run_directive(self, token):
        if(token.directive.lower() == "run"):
            for command in token.value:
                if(command.directive.lower() == "export" or command.directive.lower() == "echo"):
                    for op in command.value:
                        if((includes_pass(op) or includes_user(op) or includes_key(op)) and not includes_no_pass(op)):
                            return {
                                "command": token.original, 
                                "start_line": token.start_line, 
                                "end_line": token.end_line, 
                                "security_smell": smells["SM03"]
                            }
        return False