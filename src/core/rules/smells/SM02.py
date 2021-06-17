
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

        # Verifica se a diretiva do Docker é arg ou env, as possíveis para se atribuir uma variável
        if(directive == "env" or directive == "arg"):
            
            # Recupera cada valor de env
            for env in token.value:
                
                # Recupera chave e valor do env
                key, value = env[0], env[1]

                # Verifica se a chave inclui uma string de senha
                if(includes_pass(key)):

                    # Verifica se existe valor atribuido ao .env e se o mesmo é uma string vazia
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

        # Verifica se a diretiva do Docker é run
        if(token.directive.lower() == "run"):

            # Percorrendo todos os comandos do token
            for command in token.value:

                # Verifica se o comando shell é export ou echo
                if(command.directive.lower() == "export" or command.directive.lower() == "echo"):

                    # Percorre os parâmetros do comando
                    for op in command.value:

                        # Verifica se algum parâmetro possui indicativo de senha vazia
                        if(includes_no_pass(op)):
                            return {
                                "command": token.original, 
                                "start_line": token.start_line, 
                                "end_line": token.end_line, 
                                "security_smell": smells["SM02"],
                                "code": "SM02"
                            }

                # Verifica se está criando um usuário novo
                if(includes_add_user_command(command.directive)):

                    # Percorre os parâmetros do comando
                    for op in command.value:

                        # Verifica se algum parâmetro possui indicativo de senha vazia
                        if(includes_disabled_password(op)):
                            return {
                                "command": token.original, 
                                "start_line": token.start_line, 
                                "end_line": token.end_line, 
                                "security_smell": smells["SM02"],
                                "code": "SM02"
                            }
        return False
            