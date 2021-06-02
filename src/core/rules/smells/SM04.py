
# Security Smell 04 - Vinculação com endereço IP impróprio - Controle de acesso inadequado (CWE-284)
from .lists.smells import *

class SM04:
    def __init__(self, token):
        self.token = token
    def validade(self):
        token = self.token

        run_directive = self.verify_run_directive(token)
        cmd_directive = self.verify_cmd_directive(token)
        env_directive = self.verify_env_directive(token)

        if(cmd_directive):
            return cmd_directive
        if(run_directive):
            return run_directive
        if(env_directive):
            return env_directive

        return False

    def verify_env_directive(self, token):
        if(token.directive.lower() == "env" or token.directive.lower() == "arg"):
            if(self.includes_host(token.value[0]) and self.includes_suspicious_ip(token.value[1])):
                return {
                        "command": token.original, 
                        "start_line": token.start_line, 
                        "end_line": token.end_line, 
                        "security_smell": smells["SM04"]
                }
        return False
    
    def verify_cmd_directive(self, token):
        if(token.directive.lower() == "cmd" or token.directive.lower() == "entrypoint"):
            for item in token.value:
                if(self.includes_suspicious_ip(item)):
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
                    if(self.includes_suspicious_ip(op)):
                        return {
                            "command": token.original, 
                            "start_line": token.start_line, 
                            "end_line": token.end_line, 
                            "security_smell": smells["SM04"]
                        }
        return False



    def includes_host(self, string):
        return "host" in string.lower() or "url" in string.lower() or "domain" in string.lower() or "dominio" in string.lower()

    def includes_suspicious_ip(self, string):
        return "0.0.0.0" in string or "--ip='*'" in string or "--ip=*" in string or "--host=*" in string or "--host='*'" in string