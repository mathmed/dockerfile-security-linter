
# Security Smell 02 - Senha vazia - Senha vazia no arquivo de configuração (CWE-258)
from .lists.smells import *
from .helpers.verifications import *

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
        directive = token.directive.lower()
        if(directive == "env" or directive == "arg"):
            for env in token.value:
                key, value = env[0], env[1]
                if(includes_pass(key)):
                    if(len(value) >= 1 and value.replace(" ", "") == "''"):
                        return {
                            "command": token.original, 
                            "start_line": token.start_line, 
                            "end_line": token.end_line, 
                            "security_smell": smells["SM02"],
                            "code": "SM02"
                        }

        return False
        

    def verify_run_directive(self, token):
        if(token.directive.lower() == "run"):
            for command in token.value:
                if(command.directive.lower() == "echo"):
                    for op in command.value:
                        if(includes_no_pass(op)):
                            return {
                                "command": token.original, 
                                "start_line": token.start_line, 
                                "end_line": token.end_line, 
                                "security_smell": smells["SM02"],
                                "code": "SM02"
                            }
            
                if(includes_add_user_command(command.directive)):
                    for op in command.value:
                        if(includes_disabled_password(op)):
                            return {
                                "command": token.original, 
                                "start_line": token.start_line, 
                                "end_line": token.end_line, 
                                "security_smell": smells["SM02"],
                                "code": "SM02"
                            }
        return False
            