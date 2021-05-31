from core.analysis.lexical.LexicalAnalysis import LexicalAnalysis
from core.rules.Engine import Engine
from pathlib import Path
import json

def main(dockerfile_path):

    try:
        
        dockerfile_content = Path(dockerfile_path).read_text()
        lexical = LexicalAnalysis(dockerfile_content)
        lexical.parse()
        tokens = lexical.get_tokens()
        pp_json(Engine(tokens).run())

    except:
        print("Erro ao realizar análise do Dockerfile, verifique se a sintax está correta.")


def pp_json(json_thing, sort=False, indents=4):

    if type(json_thing) is str:
        string = json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents, ensure_ascii=False).encode('utf8')
    else:
        string = json.dumps(json_thing, sort_keys=sort, indent=indents, ensure_ascii=False).encode('utf8')

    print(string.decode().replace("\\", ""))

    return None

if __name__ == "__main__":
    main()
