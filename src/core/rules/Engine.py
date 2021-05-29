
from .smells.SM01 import SM01
from .smells.SM02 import SM02
from .smells.SM03 import SM03
from .smells.SM04 import SM04
from .smells.SM06 import SM06

class Engine:

    def __init__(self, tokens):
        self.tokens = tokens
        self.smells = []

    def run(self):

        for token in self.tokens:
            sm01 = SM01(token).validade()
            sm02 = SM02(token).validade()
            sm03 = SM03(token).validade()
            sm04 = SM04(token).validade()
            sm06 = SM06(token).validade()
            if(sm01):
                self.smells.append(sm01)
            if(sm02):
                self.smells.append(sm02)
            if(sm03):
                self.smells.append(sm03)
            if(sm04):
                self.smells.append(sm04)
            if(sm06):
                self.smells.append(sm06)
        return self.smells