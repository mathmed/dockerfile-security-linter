
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
        run_directive = self.verify_run_directive(token)

        if(cmd_directive):
            return cmd_directive

        if(env_directive):
            return env_directive
        
        if(run_directive):
            return run_directive

        return False


    def verify_env_directive(self, token):
        directive = token.directive.lower()

        # Verifica se a diretiva é env ou arg
        if(directive == "env" or directive == "arg"):

            # Percorre os envs recuperando chave e valor
            for env in token.value:
                key, value = env[0], env[1]

                # Verifica se a chave é um host e possui http
                if(includes_host(key)
                    and ("http://" in value or 
                    ("https://" not in value and "$" not in value and len(value.replace(" ", "").replace("\"", "").replace("'", "")) > 0))):
                    return {
                            "command": token.original, 
                            "start_line": token.start_line, 
                            "end_line": token.end_line, 
                            "security_smell": smells["SM06"],
                            "code": "SM06"
                        }
                
        return False

    def verify_cmd_directive(self, token):
        directive = token.directive.lower()

        # Verifica se a diretiva é cmd ou entrypoint
        if(directive == "cmd" or directive == "entrypoint"):
            for item in token.value:

                # Verifica se o parâmetro possui conexão http
                if("http://" in item):
                    return {
                            "command": token.original, 
                            "start_line": token.start_line, 
                            "end_line": token.end_line, 
                            "security_smell": smells["SM06"],
                            "code": "SM06"
                        }
        return False


    def verify_run_directive(self, token):
        
        # Verifica se a diretiva é run
        if(token.directive.lower() == "run"):

            for command in token.value:
                
                # Verifica se o comando possui serviço que inicia em rede (npm, yarn, php)
                if(includes_service_start_command(command.directive)):
                    for op in command.value:

                        # Verifica se algum parâmetro possui http
                        if("http://" in op):
                            return {
                                "command": token.original, 
                                "start_line": token.start_line, 
                                "end_line": token.end_line, 
                                "security_smell": smells["SM06"],
                                "code": "SM06"
                            }
        return False