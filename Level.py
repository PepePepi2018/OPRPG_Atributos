import math

def level(exp):
    if exp <= 25:
        return 1
    elif exp <= 50:
        return 2
    elif exp <= 85:
        return 3
    elif exp <= 125:
        return 4
    elif exp <= 170:
        return 5
    elif exp <= 220:
        return 6
    elif exp <= 275:
        return 7
    elif exp <= 335:
        return 8
    elif exp < 400:
        return 9
    elif exp == 400:
        return 10

def proximonivel(lvl):
    if lvl == 1:
        return "25"
    elif lvl == 2:
        return "50"
    elif lvl == 3:
        return "85"
    elif lvl == 4:
        return "125"
    elif lvl == 5:
        return "170"
    elif lvl == 6:
        return "220"
    elif lvl == 7:
        return "275"
    elif lvl == 8:
        return "335"
    elif lvl == 9:
        return "400"
    elif lvl == 10:
        return "400"

def HP(exp):
    if exp <= 25:
        return 24 + 2*exp 
    elif exp <= 50:
        return 48 + 2*exp
    elif exp <= 85:
        return 126 + 2*exp
    elif exp <= 125:
        return 288 + 2*exp
    elif exp <= 170:
        return 390 + 2*exp
    elif exp <= 220:
        return 552 + 2*exp
    elif exp <= 275:
        return 594 + 2*exp
    elif exp <= 335:
        return 636 + 2*exp
    elif exp < 400:
        return 678 + 2*exp
    elif exp == 400:
        return 720 + 2*exp
    

def SP(exp):
    return math.floor(1.25*exp + 50)

def AttExp(exp, ganhoExp):
    if ganhoExp > 0:
        exp = exp + ganhoExp
        if 10 <= exp <= 400:
            return 0, exp
        else:
            return 1, exp - ganhoExp
    else:
        return 1, exp

