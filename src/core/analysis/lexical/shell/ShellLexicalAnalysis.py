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
        tokens = bashlex.parse(re.sub(' +', ' ', self.command))
        self.process_tokens(tokens)

    def process_tokens(self, tokens):
        for command_shell in tokens:
            if(command_shell.kind == "list"):
                for sentence in command_shell.parts:
                    if(sentence.kind != "operator"):
                        token = Token()
                        token.set_directive(sentence.parts[0].word)
                        words_arr = []
                        for operate in sentence.parts[1:]:
                            words_arr.append(operate.word)
                        token.set_value(words_arr)
                        self.tokens.append(token)
            else:
                if(command_shell.kind != "operator"):
                    token = Token()
                    token.set_directive(command_shell.parts[0].word)
                    words_arr = []
                    for operate in command_shell.parts[1:]:
                        words_arr.append(operate.word)
                    token.set_value(words_arr)
                    self.tokens.append(token)
            

                        
        