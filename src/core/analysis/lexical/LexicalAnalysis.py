import dockerfile
from .Token import Token

class LexicalAnalysis:

    def __init__(self, dockerfile_path):
        self.dockerfile_path = dockerfile_path
        self.tokens = []

    def get_tokens(self):
        return self.tokens

    def parse(self):
        self.tokens = dockerfile.parse_file(self.dockerfile_path)
        self.convert_tokens()

    def convert_tokens(self):
        converted_tokens = []
        for token in self.tokens:
            converted_tokens.append(Token(token))
        self.tokens = converted_tokens