from dbfread import DBF
import chardet
import json
import csv


def detect_charset(path: str) -> str:
    """
    Detecta a codificação de conjunto de caracteres do arquivo
    """
    with open(path, 'rb') as f:
        rawdata = f.read()
        resultado = chardet.detect(rawdata)
        codificacao = resultado['encoding']
    return codificacao


def bdf_to_list(path: str, encoding: str) -> list:
    """
    Lê o arquivo BDF e converte para lista bidimencional
    """
    keys = []
    values = []
    for record in DBF(path, encoding=encoding):
        if len(keys) == 0:
            keys.append(list(json.loads(json.dumps(record, indent=4)).keys()))
        values.append(list(json.loads(json.dumps(record, indent=4)).values()))
    resultado = values
    resultado.insert(0, *keys)
    return resultado


def write_csv(path: str, rows: list) -> None:
    """
    Converte e escreve a lista bidimencional para csv
    """
    with open(path, 'w', encoding="utf-8") as e:
        writer = csv.writer(e)
        writer.writerows(rows)


def main(path: str, output_path: str) -> None:
    encoding = detect_charset(path)
    resultado = bdf_to_list(path, encoding=encoding)
    write_csv(output_path, resultado)


if __name__ == "__main__":
    import _secrets
    main(_secrets.INPUT_FILE, _secrets.OUTPUT_FILE)
