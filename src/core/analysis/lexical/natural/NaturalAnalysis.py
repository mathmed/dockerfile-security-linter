
from ..Token import Token

class NaturalAnalysis:

    def __init__(self, dockerfile_content):
        self.dockerfile_content = dockerfile_content
        self.tokens = []

    def get_tokens(self):
        return self.tokens

    def parse(self):

        commands = self.dockerfile_content.splitlines()
        for command in commands:
            if(command and command.strip()[0] == "#"):
                token = Token("comment", command.strip()[1:].strip(), "", "", command.strip()[1:].strip())
                self.tokens.append(token)
