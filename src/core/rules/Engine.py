
from .smells.SM01 import SM01
from .smells.SM02 import SM02

class Engine:

    def __init__(self, tokens):
        self.tokens = tokens
        self.smells = []

    def run(self):

        for token in self.tokens:
            sm01 = SM01(token).validade()
            sm02 = SM02(token).validade()
            if(sm01):
                self.smells.append(sm01)
            if(sm02):
                self.smells.append(sm02)
                
        return self.smells