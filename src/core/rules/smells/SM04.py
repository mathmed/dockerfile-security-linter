
# Security Smell 04 - Vinculação com endereço IP impróprio - Controle de acesso inadequado (CWE-284)
from .lists.smells import *
from .helpers.verifications import *
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
        directive = token.directive.lower()

        # Verifica se a diretiva do Docker é arg ou env, as possíveis para se atribuir uma variável
        if(directive == "env" or directive == "arg"):

            # Recupera cada valor de env, chave e valor
            for env in token.value:
                key, value = env[0], env[1]

                # Verifica se a chave do env inclui atribuição de url e o valor é um IP inseguro
                if(includes_host(key) and includes_suspicious_ip(value)):
                    return {
                            "command": token.original, 
                            "start_line": token.start_line, 
                            "end_line": token.end_line, 
                            "security_smell": smells["SM04"],
                            "code": "SM04"
                    }

        return False
    
    def verify_cmd_directive(self, token):
        directive = token.directive.lower()

        # Verifica se a diretiva do Docker é cmd ou entrypoint
        if(directive == "cmd" or directive == "entrypoint"):

            # Percorre todos os itens do comando
            for item in token.value:

                # Verifica se o item é um IP suspeito
                if(includes_suspicious_ip(item)):
                    return {
                            "command": token.original, 
                            "start_line": token.start_line, 
                            "end_line": token.end_line, 
                            "security_smell": smells["SM04"],
                            "code": "SM04"
                        }
        return False

    def verify_run_directive(self, token):
        # Verifica se a diretiva do Docker é run
        if(token.directive.lower() == "run"):

            # Percorre os parâmetros do comando
            for command in token.value:
                for op in command.value:

                    # Verifica se o parâmetro do comando inclui um IP suspeito
                    if(includes_suspicious_ip(op)):
                        return {
                            "command": token.original, 
                            "start_line": token.start_line, 
                            "end_line": token.end_line, 
                            "security_smell": smells["SM04"],
                            "code": "SM04"
                        }
        return False
