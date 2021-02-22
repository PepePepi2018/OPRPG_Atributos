import Level

def arma(dados): # dados será um vetor de 5 elementos, o primeiro a exp, o segundo tipo, o terceiro o dano, o quarto o acerto e o quinto a pontaria
    acerto = 0
    pontaria = 0
    level = Level.level(dados[0])
    if dados[1] == 0:
        dano = dados[2]
    elif dados[1] == 1:
        dano = dados[2] * level
    elif dados[1] == 2:
        dano = dados[2] * level
        acerto = dados[3] * level
        pontaria = dados[4] * level
    return dano, acerto, pontaria