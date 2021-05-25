from core.analysis.lexical.LexicalAnalysis import LexicalAnalysis
from core.rules.Engine import Engine
import pprint

def main():

    lexical = LexicalAnalysis('/home/dsl/dockerfiles/Dockerfile')
    lexical.parse()
    tokens = lexical.get_tokens()
    print(Engine(tokens).run())

if __name__ == "__main__":
    main()
