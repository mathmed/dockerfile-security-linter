
# Security Smell 03 - Credenciais definidas em texto claro - Uso de senha em texto claro (CWE-259)
from .smells import *

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
        if(token.directive == "env"):
            if(self.includes_pass(token.value[0]) or self.includes_user(token.value[0])):
                if(len(token.value) >= 1 and token.value[1].replace(" ", "") != "''"):
                    return {
                        "command": token.original, 
                        "start_line": token.start_line, 
                        "end_line": token.end_line, 
                        "security_smell": smells["SM03"]
                    }
        return False

    def verify_run_directive(self, token):
        if(token.directive == "run"):
            for command in token.value:
                if(command.directive.lower() == "export"):
                    for op in command.value:
                        if(self.includes_pass(op) or self.includes_user(op)):
                            return {
                                "command": token.original, 
                                "start_line": token.start_line, 
                                "end_line": token.end_line, 
                                "security_smell": smells["SM03"]
                            }
        return False

    def includes_pass(self, string):
        return "pass" in string.lower() or "senha" in string.lower()

    def includes_user(self, string):
        return "user" in string.lower() or "usuario" in string.lower()

