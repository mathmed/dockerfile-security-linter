import dockerfile
from .Token import Token

class LexicalAnalysis:

    def __init__(self, dockerfilePath):
        self.dockerfilePath = dockerfilePath
        self.tokens = []

    def getTokens(self):
        return self.tokens

    def parse(self):
        self.tokens = dockerfile.parse_file(self.dockerfilePath)
        self.convertTokens()

    def convertTokens(self):
        convertedTokens = []
        for token in self.tokens:
            convertedTokens.append(Token(token))
        self.tokens = convertedTokens