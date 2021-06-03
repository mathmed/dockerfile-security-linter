
from .smells.SM01 import SM01
from .smells.SM02 import SM02
from .smells.SM03 import SM03
from .smells.SM04 import SM04
from .smells.SM05 import SM05
from .smells.SM06 import SM06
from .smells.SM07 import SM07
from .smells.SM08 import SM08
from .smells.SM09 import SM09
from .smells.SM10 import SM10

class Engine:

    def __init__(self, tokens):
        self.tokens = tokens
        self.smells = []

    def run(self):

        sm01 = SM01(self.tokens).validade()
        if(sm01):
            self.smells.append(sm01)

        for token in self.tokens:

            sm02 = SM02(token).validade()
            sm03 = SM03(token).validade()
            sm04 = SM04(token).validade()
            sm05 = SM05(token).validade()
            sm06 = SM06(token).validade()
            sm07 = SM07(token).validade()
            sm08 = SM08(token).validade()
            sm09 = SM09(token).validade()
            sm10 = SM10(token).validade()

            if(sm02):
                self.smells.append(sm02)
            if(sm03):
                self.smells.append(sm03)
            if(sm04):
                self.smells.append(sm04)
            if(sm05):
                self.smells.append(sm05)
            if(sm06):
                self.smells.append(sm06)
            if(sm07):
                self.smells.append(sm07)
            if(sm08):
                self.smells.append(sm08)      
            if(sm09):
                self.smells.append(sm09)  
            if(sm10):
                self.smells.append(sm10)
                 
        return self.smells