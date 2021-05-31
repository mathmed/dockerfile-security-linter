from argparse import ArgumentParser
from api.cli import main as CLI

def main():

    try:
        parser = ArgumentParser()

        parser.add_argument("-f", "--file", dest="filename",
                            help="Diretório do Dockerfile que será analisado.")
                            
        parser.add_argument("-m", "--mode",
                            dest="mode", default=True,
                            help="Interface que a aplicação irá funcionar.")

        args = parser.parse_args()

        if(args.mode == "cli"):
            if(args.filename):
                CLI.main(args.filename)
            else:
                raise Exception()

    except:
        print("Modo de uso python3 main.py -m <cli/web> -f <dockerfile>")

if __name__ == "__main__":
    main()
