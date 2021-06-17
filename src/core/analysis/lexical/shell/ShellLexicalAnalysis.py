import bashlex
import re
from .Token import Token

class ShellLexicalAnalysis:

    def __init__(self, command):
        self.command = command
        self.tokens = []

    def get_tokens(self):
        return self.tokens

    def parse(self):

        # Utiliza a biblioteca bashlex para realizar o parser do comando shell
        tokens = list(bashlex.split(re.sub(' +', ' ', self.command)))
        
        # Processa os operadores do comando, transformando em N comandos
        tokens = self.process_operators(tokens)

        # Processa os tokens
        self.process_tokens(tokens)

    def process_tokens(self, tokens):
        for sentence in tokens:
            if(len(sentence) > 0):

                # Cria um token shell
                token = Token()

                # Verifica se o comando inicia com sudo, caso sim, removê-lo, não é utilizado em nenhuma verificação
                # Adiciona então a diretiva do comando shell

                if(sentence[0].lower() == "sudo"):
                    token.set_directive(sentence[1])
                    start_in = 2

                else:
                    token.set_directive(sentence[0])
                    start_in = 1

                # Processa os argumentos do comando shell
                words_arr = []

                for operate in sentence[start_in:]:
                    words_arr.append(operate)
                token.set_value(words_arr)
                self.tokens.append(token)

    
    # Processa comandos que possuem operadores N vários comandos
    def process_operators(self, command):
        array = []
        last_split=0
        for i in range(len(command)):
            if(command[i] == "&&" or command[i] == "||"):
                if(last_split == 0):
                    array.append(command[0:i])
                else:
                    array.append(command[last_split+1:i])
                last_split=i
            if(i == len(command)-1):
                if(last_split == 0):
                    array.append(command[0:i+1])
                else:
                    array.append(command[last_split+1:i+1])
        return array
        