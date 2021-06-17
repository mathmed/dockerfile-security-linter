# Security Smell 11 - Download e execução de código sem verificação de integridade
# Baixa o código-fonte ou um executável de um local remoto e executa o código sem verificar suficientemente a origem e integridade do código.
# CWE-494

from .lists.smells import *
from .lists.obsolete_linux_commands import *
from .helpers.verifications import *

class SM11:
    def __init__(self, tokens):
        self.tokens = tokens

    def validade(self):

        tokens = self.tokens
        run_directive = self.verify_run_directive(tokens)

        if(run_directive):
            return run_directive

        return False

    # Recebe como parâmetro todos os tokens do Dockerfile
    def verify_run_directive(self, tokens):
        for token in tokens:

            # Verifica se o token é um run
            if(token.directive.lower() == "run"):
                for command in token.value:

                    # Verifica se no commando shell, é utilizado curl ou wget para baixar algo
                    if(command.directive.lower() in ("curl", "wget")):
                        
                        # Percorre todos os parâmetros
                        for op in command.value:
                            splited_op = op.split("/")

                            # Verifica se o parâmetro é uma url (http/https)
                            if(len(splited_op) > 0 and "http" in splited_op[0]):

                                # Divide novamente o parametro
                                splited_file = splited_op[-1].split(".")
                                
                                # Verifica se o último item da URL (arquivo) é um sh
                                # também verifica novamente o Dockerfile a fim de verificar se o arquivo é executado
                                if(len(splited_file) > 0 and splited_file[-1] == "sh" and self.verify_if_file_is_executed(tokens, command.value, splited_file[-2])):
                                    return {
                                        "command": token.original, 
                                        "start_line": token.start_line, 
                                        "end_line": token.end_line, 
                                        "security_smell": smells["SM11"],
                                        "code": "SM11"
                                    }

    def verify_if_file_is_executed(self, tokens, command, filename):

        # Percorre todo Dockerfile
        for token in tokens:

            # Verifica se é um comando shell
            if(token.directive.lower() == "run"):

                # Percorre os comandos
                for command_token in token.value:

                    # Verifica SE NÃO é wget e curl (já foram escaneados anteriormente)
                    if(command_token.directive not in ("wget", "curl")):

                        # Verifica se é um comando para executar o arquivo baixado
                        if(includes_file_execution(command_token.directive, filename) and len(command_token.value) == 0):
                            return True
                        else:
                            for op in command_token.value:
                                for word in command:
                                    if(word in op or filename in op):
                                        return True