import Graduacao
import math
import database

def bonus(pontos):
    somatorio = 0
    for k in [0, 1, 2, 3]:     
        # pontos é um vetor onde é Bruto, Racial, Edc, Akuma, Haki, Arma, Itens, Bonus
        # pontos é um vetor onde é   0  ,   1   ,  2 ,   3  ,   4 ,  5  ,   6  ,   7
        somatorio = somatorio + pontos[k] # Soma do Bruto, racial, edc e akuma
    b = math.floor(somatorio / 2) # Bônus é igual a metade da soma do Bruto + Racial + EDC + Akuma
    
    claS = Graduacao.classificacao(somatorio) # classificação do somatório
    claB = Graduacao.classificacao(b) # classificação do bônus

    if claS == claB:
        if database.classes[claS] == 1:
            b = 0
        elif database.classes[claS] == 2:
            b = 10
        elif database.classes[claS] == 3:
            b = 25
        elif database.classes[claS] == 4:
            b = 49
        elif database.classes[claS] == 5:
            b = 89
        elif database.classes[claS] == 6:
            b = 135
        elif database.classes[claS] == 7:
            b = 200
        elif database.classes[claS] == 8:
            b = 285
        elif database.classes[claS] == 9:
            b = 399
    return b