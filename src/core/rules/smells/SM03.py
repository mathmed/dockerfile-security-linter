
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

        # Verifica se a diretiva do Docker é arg ou env, as possíveis para se atribuir uma variável
        if(directive == "env" or directive == "arg"):

            # Recupera cada valor de env
            for env in token.value:

                # Recupera chave e valor do env
                key, value = env[0], env[1]

                # Verifica se o env inclui senha, chave ou usuário
                if(includes_pass(key) or includes_user(key) or includes_key(key)):

                    # Verifica se o valor não é vazio (caso SM02) e se o mesmo não é uma atribuição de variável ($)
                    if(len(value) >= 1 and value.replace(" ", "") != "''" and "$" not in value):
                        return {
                            "command": token.original, 
                            "start_line": token.start_line, 
                            "end_line": token.end_line, 
                            "security_smell": smells["SM03"],
                            "code": "SM03"
                        }
        return False

    def verify_run_directive(self, token):

        # Verifica se a diretiva do Docker é run
        if(token.directive.lower() == "run"):

            # Percorrendo todos os comandos do token
            for command in token.value:

                # Verifica se o comando shell é export ou echo
                if(command.directive.lower() == "export" or command.directive.lower() == "echo"):

                    # Percorre os parâmetros do comando
                    for op in command.value:
                        
                        # Verifica se o parametro inclui senha, usuario ou chave e não inclui senha sesativada (SM02)
                        if((includes_pass(op) or includes_user(op) or includes_key(op)) and not includes_no_pass(op)):
                            return {
                                "command": token.original, 
                                "start_line": token.start_line, 
                                "end_line": token.end_line, 
                                "security_smell": smells["SM03"],
                                "code": "SM03"
                            }
        return False