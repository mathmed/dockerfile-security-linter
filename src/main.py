from argparse import ArgumentParser
from api.cli import main as CLI
from api.web import main as WEB

def main():

    # Recebendo parâmetros

    parser = ArgumentParser()

    parser.add_argument("-f", "--file", dest="filename",
                        help="Diretório do Dockerfile que será analisado (somente modo CLI).")
                        
    parser.add_argument("-m", "--mode",
                        dest="mode", default=True,
                        help="Interface que a aplicação irá funcionar.")

    args = parser.parse_args()

    # Iniciando em modo CLI ou WEB
    if(args.mode == "cli"):
        if(args.filename):
            CLI.main(args.filename)
        else:
            raise Exception()

    if(args.mode == "web"):
        WEB.main()

if __name__ == "__main__":
    main()
