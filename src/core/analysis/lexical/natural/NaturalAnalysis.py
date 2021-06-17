
from ..Token import Token

class NaturalAnalysis:

    def __init__(self, dockerfile_content):
        
        self.dockerfile_content = dockerfile_content
        self.tokens = []

    def get_tokens(self):
        return self.tokens

    def parse(self):

        # Realiza um split em todo Dockerfile separando por linhas
        commands = self.dockerfile_content.splitlines()

        line = 1
        # Percorre todas as linhas
        for command in commands:

            # Remove espaços e verifica se é um comentário (#)
            if(len(command.strip()) > 0 and command.strip()[0] == "#"):
                
                # Cria um token de diretiva comentário
                token = Token("comment", command.strip()[1:].strip(), line, line, command.strip()[1:].strip())
                self.tokens.append(token)
            
            line+=1