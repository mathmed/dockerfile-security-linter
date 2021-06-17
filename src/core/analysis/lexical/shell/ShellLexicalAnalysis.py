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
        tokens = list(bashlex.split(re.sub(' +', ' ', self.command)))
        tokens = self.process_operators(tokens)
        self.process_tokens(tokens)

    def process_tokens(self, tokens):
        for sentence in tokens:
            if(len(sentence) > 0):
                token = Token()
                if(sentence[0].lower() == "sudo"):
                    token.set_directive(sentence[1])
                    start_in = 2
                else:
                    token.set_directive(sentence[0])
                    start_in = 1
                words_arr = []
                for operate in sentence[start_in:]:
                    words_arr.append(operate)
                token.set_value(words_arr)
                self.tokens.append(token)

    def process_operators(self, command):
        array = []
        last_split=0
        for i in range(len(command)):
            if(command[i] == "&&" or command[i] == "||"):
                if(last_split == 0):
                    array.append(command[0:i])
                else:
                    array.append(command[last_split+1:i])
                last_split=i
            if(i == len(command)-1):
                if(last_split == 0):
                    array.append(command[0:i+1])
                else:
                    array.append(command[last_split+1:i+1])
        return array
        