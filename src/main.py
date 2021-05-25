from core.analysis.lexical.LexicalAnalysis import LexicalAnalysis
from core.rules.Engine import Engine
import pprint

def main():

    lexical = LexicalAnalysis('dockerfiles/Dockerfile')
    lexical.parse()
    tokens = lexical.getTokens()
    print(Engine(tokens).run())

if __name__ == "__main__":
    main()
