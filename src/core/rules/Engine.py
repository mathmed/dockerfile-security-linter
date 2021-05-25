
from .smells.SM01 import SM01

class Engine:

    def __init__(self, tokens):
        self.tokens = tokens
        self.smells = []

    def run(self):
        for token in self.tokens:
            sm01 = self.validade(token)
            if(sm01):
                self.smells.append(sm01)
        return self.smells

    def validade(self, token):
        return SM01(token).validade()