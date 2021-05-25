
from core.rules.smells.SM01 import SM01

class Engine:

    def __init__(self, tokens):
        self.tokens = tokens
        self.smells = []

    def run(self):
        for token in self.tokens:
            sm01 = SM01(token).validade()
            if(sm01):
                self.smells.append(sm01)
        return self.smells