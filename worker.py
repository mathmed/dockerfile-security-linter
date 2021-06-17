import requests
import json
import glob
from pathlib import Path
from multiprocessing import Pool

url_api = "http://localhost:8000/dockerfile-analysis"
dockerfiles_path = "/home/mateus/Área de Trabalho/TCC/TCC 2/dataset/datasets/0b-deduplicated-dockerfile-sources/sources/*.Dockerfile"

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
        "SM010": 9,
        "SM011": 10,
    }
    return smells[smell]

def run(path):

    smells = [0] * 12
    path = str(path)
    params = {'dockerfile': Path(path).read_text()}
    r = requests.post(url = url_api, json = params)
    
    try:
        smells[position(json.loads(r.text)["result"][0]["code"])] += 1
    except:
        smells[11] += 1
        print("Dockerfile com sintaxe inválida.")

    return smells
    
pathlist = glob.glob(dockerfiles_path)
process = Pool(8)
results = process.map(run, pathlist) 
sumindex = [sum(elts) for elts in zip(*results)]
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
        "SM010": sumindex[9],
        "SM011": sumindex[10],
        "Erros": sumindex[11],
    }
)
