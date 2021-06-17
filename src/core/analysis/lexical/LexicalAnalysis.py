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
        
        # Cria um arquivo temporário de acordo com o conteúdo do Dockerfile
        temporary_dockerfile = tempfile.NamedTemporaryFile(mode = 'w+')
        temporary_dockerfile.write(self.dockerfile_content)
        temporary_dockerfile.seek(0)

        # Realiza o parse do arquivo com a biblioteca parse_file
        tokens = dockerfile.parse_file(temporary_dockerfile.name)
        
        # Realiza pós-processamento nos tokens
        self.process_tokens(tokens)

    def process_tokens(self, tokens):
        converted_tokens = []
        for token in tokens:

            # Cria o objeto do token somente com as informações que são necessárias da biblioteca
            token_obj = Token(
                token[0],
                token[3],
                token[4],
                token[5],
                token[7]
            )

            # Caso o comando seja shell, é necessário realizar outro parser e processamento
            if(token_obj.directive.lower() == "run"):
                token_obj.set_value(self.run_shell_analysis(token_obj.value[0]))

            # Caso o comando seja env/arg, é necessário realizar outro processamento
            elif(token_obj.directive.lower() == "env"):
                token_obj.set_value(self.convert_array_env_directive(token_obj.value))

            elif(token_obj.directive.lower() == "arg"):
                token_obj.set_value(self.convert_array_arg_directive(token_obj.value))
            
            # Adiciona o token criado
            converted_tokens.append(token_obj)

        # Realiza o parser de comentário (a lib dockerfile não faz)
        natural_tokens = self.run_natural_analysis()
        for natural_token in natural_tokens:
            converted_tokens.append(natural_token)

        self.tokens = converted_tokens

    def run_shell_analysis(self, command):

        # Chama a classe de shell analysis para processar o comando e retorna o token
        shell_analysis = ShellLexicalAnalysis(command)
        shell_analysis.parse()
        return shell_analysis.get_tokens()

    def run_natural_analysis(self):

        # Chama a classe de natural analysis para processar o dockerfile e retorna os tokens
        natural_analysis = NaturalAnalysis(self.dockerfile_content)
        natural_analysis.parse()
        return natural_analysis.get_tokens()

    # Processa os argumentos da diretiva ENV, transformando em um array de mais fácil manipulação
    def convert_array_env_directive(self, command):
        envs_array = []
        aux_array = []
        if(len(command) > 2):
            # Transforma o array resultante de envs em um array de arrays, no qual cada um representa um env
            for i in range(len(command)):
                aux_array.append(command[i])
                if i % 2 > 0 and i != 0:
                    envs_array.append(aux_array)
                    aux_array = []

            return envs_array

        return [command]

    # Processa os argumentos da diretiva ARG, transformando em um array de mais fácil manipulação
    def convert_array_arg_directive(self, command):
        arg_array = []
        aux_array = []
        
        # Transforma o array resultante de arg em um array de arrays, no qual cada um representa um env
        for i in range(len(command)):
            sentence = command[i].split("=")
            arg_array.append([sentence[0], sentence[1] if len(sentence) == 2 else "''"])
        return arg_array