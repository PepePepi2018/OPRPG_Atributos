# Programa com funções envolvendo Haki
import database

def proximonivelhaki(exp):
    if exp < 25:
        return "25"
    else:
        return "75"

###################################################################################################################
def lvlhakirei(lvl):
    if lvl == 4 or lvl == 5:
        return 1
    elif lvl == 6 or lvl == 7:
        return 2
    elif lvl >= 8:
        return 3

###################################################################################################################

def pontoshaki(exp):

    if exp == 0:
        return 0, 0, 0, 0
    elif exp <= 25:
        return 10, 10, 10, 10     
    elif exp < 75:
        return 30, 30, 30, 30
    elif exp == 75:
        return 50, 50, 50, 50

def AttCaminho(val1, val2, val3, val4, val5, val6):
    return val1, val2, val3, val4, val5, val6

def pontosCaminhoBusou(val1,val2,val3,val4,val5,val6):
    if val4 == 1 or val5 == 1 or val6 == 1:
        return val4 * database.Especializacoes[3][0] + val5 * database.Especializacoes[4][0] + val6 * database.Especializacoes[5][0], val4 * database.Especializacoes[3][5] + val5 * database.Especializacoes[4][5] + val6 * database.Especializacoes[5][5]
    else:
        return val1 * database.Especializacoes[0][0] + val2 * database.Especializacoes[1][0] + val3 * database.Especializacoes[2][0], val1 * database.Especializacoes[0][5] + val2 * database.Especializacoes[1][5] + val3 * database.Especializacoes[2][5]

def pontosCaminhoKenbun(val1,val2,val3,val4,val5,val6):
        if val5 == 1 or val6 == 1:
            return val5 * database.Especializacoes[10][1] + val6 * database.Especializacoes[11][1], val5 * database.Especializacoes[10][2] + val6 * database.Especializacoes[11][2], val5 * database.Especializacoes[10][3] + val6 * database.Especializacoes[11][3], val5 * database.Especializacoes[10][4] + val6 * database.Especializacoes[11][4]    
        else:
            return val1 * database.Especializacoes[6][1] + val2 * database.Especializacoes[7][1] + val3 * database.Especializacoes[8][1] + val4 * database.Especializacoes[9][1], val1 * database.Especializacoes[6][2] + val2 * database.Especializacoes[7][2] + val3 * database.Especializacoes[8][2] + val4 * database.Especializacoes[9][2], val1 * database.Especializacoes[6][3] + val2 * database.Especializacoes[7][3] + val3 * database.Especializacoes[8][3] + val4 * database.Especializacoes[9][3], val1 * database.Especializacoes[6][4] + val2 * database.Especializacoes[7][4] + val3 * database.Especializacoes[8][4] + val4 * database.Especializacoes[9][4]