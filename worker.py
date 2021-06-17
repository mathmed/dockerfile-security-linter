# Worker para executar a análise em todos dockerfiles da base de dados

import requests
import json
import glob
from pathlib import Path
from multiprocessing import Pool

# URL da API e pasta onde os Dockerfiles estão
url_api = "http://localhost:8000/dockerfile-analysis"
dockerfiles_path = "/home/mateus/Área de Trabalho/TCC/TCC 2/dataset/datasets/0b-deduplicated-dockerfile-sources/sources/*.Dockerfile"


# Converte um código de security smell para um índice de array
def position(smell):
    smells = {
        "SM01": 0,
        "SM02": 1,
        "SM03": 2,
        "SM04": 3,
        "SM05": 4,
        "SM06": 5,
        "SM07": 6,
        "SM08": 7,
        "SM09": 8,
        "SM10": 9,
        "SM11": 10,
    }
    return smells[smell]

# Executa o worker
def run(path):

    # Cria o array com quantidade de smells, 11 smells, +1 posição para erros, +1 posição para N/A smell
    smells = [0] * 13
    
    # Recebe o caminho do Dockerfile e cria o parâmetro para chamada da API
    path = str(path)
    params = {'dockerfile': Path(path).read_text()}

    # Realiza a requisição a API e salva o valor retornado
    r = requests.post(url = url_api, json = params)
    result = json.loads(r.text)["result"]

    # Verifica se algum smell foi encontrado
    if(result == "Nenhuma vulnerabilidade encontrada"):
            smells[12] += 1
    else:

        # Salva os smells no array
        try:
            for item in result:
                smells[position(item["code"])] += 1
        except:
            # Caso de erro na análise do Dockerfile
            smells[11] += 1
            print("Dockerfile com sintaxe inválida: ", path)

    return smells
    
# Recupera todos os caminhos de Dockerfiles na pasta
pathlist = glob.glob(dockerfiles_path)

# Cria threads para realizar o processamento
process = Pool(8)

# Realiza a chamada da função run com threads enviando os dockerfiles
results = process.map(run, pathlist[:10000]) 

# Soma todos os valores obtidos de smells na análise
sumindex = [sum(item) for item in zip(*results)]

# Exibe o resultado
print(
    {
        "SM01": sumindex[0],
        "SM02": sumindex[1],
        "SM03": sumindex[2],
        "SM04": sumindex[3],
        "SM05": sumindex[4],
        "SM06": sumindex[5],
        "SM07": sumindex[6],
        "SM08": sumindex[7],
        "SM09": sumindex[8],
        "SM10": sumindex[9],
        "SM11": sumindex[10],
        "Erros": sumindex[11],
        "Nenhuma vulnerabilidade": sumindex[12],
    }
)
