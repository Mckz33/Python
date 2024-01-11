# validador.py

def validar_json(json_data):
    if not isinstance(json_data, list) or len(json_data) != 2:
        return False

    for elemento in json_data:
        if not isinstance(elemento, dict) or 'Ementa' not in elemento:
            return False

        if 'Conteudo' not in elemento:
            return False

    return True
