import database
def soma(pontos, temBonus):
    # pontos é um vetor onde é Bruto, Racial, Edc, Akuma, Haki, HakiComp, Arma, Itens, Bonus
    # pontos é um vetor onde é   0  ,   1   ,  2 ,   3  ,   4 ,     5   ,   6 ,   7  ,   8
    somatorio = 0
    aux = 0
    for som in pontos[0:4]:
        aux = aux + som
    for som in pontos[4:8]:
        somatorio = somatorio + som

    if temBonus == 1:
        if aux < pontos[8]:
            somatorio = somatorio + pontos[8]
        else:
            somatorio = somatorio + aux
    else:
        somatorio = somatorio + aux


    return somatorio

def somaBruto(pontos):
    som = 0
    for i in range(0,6):
        som = som + pontos[i][0]
    
    return som

def ProcessarRaca(pontos, raca, val1, val2):
    pontos[0][1] = database.ShowRaca[raca][2]  # Dano
    if database.ShowRaca[raca][0] == 1:
        pontos[1][1] = database.ShowRaca[raca][3] * (1 - val1)  # Acerto
        pontos[2][1] = database.ShowRaca[raca][4] * val1  # Pontaria
    else:
        pontos[1][1] = 0
        pontos[2][1] = 0
    if database.ShowRaca[raca][1] == 1:
        pontos[3][1] = database.ShowRaca[raca][5] * (1 - val2)  # Esquiva
        pontos[4][1] = database.ShowRaca[raca][6] * val2  # Bloqueio
    else:
        pontos[3][1] = 0
        pontos[4][1] = 0
    pontos[5][1] = database.ShowRaca[raca][7]  # Resistência
   