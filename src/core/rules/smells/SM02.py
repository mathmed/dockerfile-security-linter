
# Security Smell 02 - Senha vazia - Senha vazia no arquivo de configuração (CWE-258)
from .helpers.smells import *

class SM02:
    def __init__(self, token):
        self.token = token
    def validade(self):

        token = self.token

        env_directive = self.verify_env_directive(token)
        run_directive = self.verify_run_directive(token)

        if(env_directive):
            return env_directive

        if(run_directive):
            return run_directive

        return False

    def verify_env_directive(self, token):
        if(token.directive == "env"):
            if(self.includes_pass(token.value[0])):
                if(len(token.value) >= 1 and token.value[1].replace(" ", "") == "''"):
                    return {
                        "command": token.original, 
                        "start_line": token.start_line, 
                        "end_line": token.end_line, 
                        "security_smell": smells["SM02"]
                    }
        return False

    def verify_run_directive(self, token):
        if(token.directive == "run"):
            for command in token.value:
                if(command.directive.lower() == "echo"):
                    for op in command.value:
                        if("nopasswd" in op.lower() or "all=nopasswd" in op.lower() or "nopasswd:all" in op.lower()):
                            return {
                                "command": token.original, 
                                "start_line": token.start_line, 
                                "end_line": token.end_line, 
                                "security_smell": smells["SM02"]
                            }
            
                if(command.directive.lower() == "adduser" or command.directive.lower() == "useradd"):
                    for op in command.value:
                        if("disabled-password" in op.lower()):
                            return {
                                "command": token.original, 
                                "start_line": token.start_line, 
                                "end_line": token.end_line, 
                                "security_smell": smells["SM02"]
                            }
        return False
            
    def includes_pass(self, string):
        return "pass" in string.lower() or "senha" in string.lower() 

