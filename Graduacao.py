def classificacao(valor):
    if valor == 0:
        return "Inábil"
    elif valor <= 10:
        return "Normal"
    elif valor <= 25:
        return "Bom"
    elif valor <= 49:
        return "Habilidoso"
    elif valor <= 89:
        return "Especialista"
    elif valor <= 135:
        return "Incrível"
    elif valor <= 200:
        return "Monstruoso"
    elif valor <= 285:
        return "Épico"
    elif valor <= 399:
        return "Mestre"
    elif valor >= 400:
        return "Lendário"