import dockerfile
import tempfile
from .Token import Token
from .shell.ShellLexicalAnalysis import ShellLexicalAnalysis
from .natural.NaturalAnalysis import NaturalAnalysis

class LexicalAnalysis:

    def __init__(self, dockerfile_content):
        self.dockerfile_content = dockerfile_content
        self.tokens = []

    def get_tokens(self):
        return self.tokens

    def parse(self):
        temporary_dockerfile = tempfile.NamedTemporaryFile(mode = 'w+')
        temporary_dockerfile.write(self.dockerfile_content)
        temporary_dockerfile.seek(0)
        tokens = dockerfile.parse_file(temporary_dockerfile.name)
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

        natural_tokens = self.run_natural_analysis()
        for natural_token in natural_tokens:
            converted_tokens.append(natural_token)

        self.tokens = converted_tokens

    def run_shell_analysis(self, command):
        shell_analysis = ShellLexicalAnalysis(command)
        shell_analysis.parse()
        return shell_analysis.get_tokens()

    def run_natural_analysis(self):
        natural_analysis = NaturalAnalysis(self.dockerfile_content)
        natural_analysis.parse()
        return natural_analysis.get_tokens()