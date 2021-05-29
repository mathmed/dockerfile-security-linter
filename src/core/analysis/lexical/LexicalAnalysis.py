import dockerfile
from .Token import Token
from .modules.shell.ShellLexicalAnalysis import ShellLexicalAnalysis

class LexicalAnalysis:

    def __init__(self, dockerfile_path):
        self.dockerfile_path = dockerfile_path
        self.tokens = []

    def get_tokens(self):
        return self.tokens

    def parse(self):
        tokens = dockerfile.parse_file(self.dockerfile_path)
        self.process_tokens(tokens)

    def process_tokens(self, tokens):
        converted_tokens = []
        for token in tokens:
            token_obj = Token(
                token[0],
                token[3],
                token[4],
                token[5],
                token[7]
            )
            if(token_obj.directive.lower() == "run"):
                token_obj.set_value(self.run_shell_analysis(token_obj.value[0]))
            converted_tokens.append(token_obj)
        self.tokens = converted_tokens

    def run_shell_analysis(self, command):
        shell_analysis = ShellLexicalAnalysis(command)
        shell_analysis.parse()
        return shell_analysis.get_tokens()