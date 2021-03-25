import Level
import Graduacao
import database

def codedados(dados, formas, itens, cores):
    # Texto que retornará
    texto = ''
    
    # Auxiliar para baixar os dados
    aux = ''
    for io in range(len(dados)):
        aux = f'{aux}{str(dados[io])}\n'

    texto = f'{texto}{aux}'

    # Auxiliar para baixar as formas
    aux = ''
    for io in range(len(formas)):
        for i in range(7):
            aux = f'{aux}{str(formas[io][i])}\n'
    aux = f'{aux}Acabou\n'

    texto = f'{texto}{aux}'

    # Auxiliar para baixar as cores
    aux = ''
    for io in range(11):
        aux = f'{aux}{cores[io]}\n'
    
    texto = f'{texto}{aux}'

    # Auxiliar para baixar os itens
    aux = ''
    for i in range(len(itens)):
        for io in range(7):
            aux = f'{aux}{str(itens[i][io])}\n'
    
    texto = f'{texto}{aux}'

    return texto

def codeatributos(lvl, dados, pontos, formas, itens, cores):
    texto = f'[b]LEVEL:[/b] {str(lvl)}\n'
    texto = f'{texto}[b]EXP:[/b] {str(dados[0])}/{Level.proximonivel(lvl)}\n'
    texto = f'{texto}[b]BERRIES:[/b] {dados[1]}\n'
    texto = f'{texto}[b]BANCO:[/b] {dados[2]}\n\n'

    texto = f'{texto}[b][color=green]HP:[/color][/b]: {str(Level.HP(dados[0]))}\n'
    texto = f'{texto}[b][color=blue]SP:[/color][/b]: {str(Level.SP(dados[0]))}\n\n'

    for i in range(6):
        # Qual atributo é
        if i == 0:
            texto = f'{texto}[b]DANO:[/b] '
        elif i == 1:
            texto = f'{texto}[b]ACERTO:[/b] '
        elif i == 2:
            texto = f'{texto}[b]PONTARIA:[/b] '
        elif i == 3:
            texto = f'{texto}[b]ESQUIVA:[/b] '
        elif i == 4:
            texto = f'{texto}[b]BLOQUEIO:[/b] '
        elif i == 5:
            texto = f'{texto}[b]RESISTÊNCIA:[/b] '

        # Bruto
        if cores[0] == 'white':
            texto = f'{texto}{str(pontos[i][0])} '
        else:
            texto = f'{texto}[color={cores[0]}]{str(pontos[i][0])}[/color] '

        # Racial
        if pontos[i][1] != 0:
            if cores[1] == 'white':
                texto = f'{texto}(+{str(pontos[i][1])} Racial) '
            else:
                texto = f'{texto}[color={cores[1]}](+{str(pontos[i][1])} Racial)[/color] '

        # EDC
        if pontos[i][2] != 0:
            if cores[2] == 'white':
                texto = f'{texto}(+{str(pontos[i][2])} EDC) '
            else:
                texto = f'{texto}[color={cores[2]}](+{str(pontos[i][2])} EDC)[/color] '

        # Akuma
        if pontos[i][3]!= 0:
            if cores[3] == 'white':
                for j in range(len(formas)):
                    if formas[j][i] != 0:
                        texto = f'{texto}(+{str(formas[j][i])} {str(formas[j][6])}) '
            else:
                texto = f'{texto}[color={cores[3]}]'
                for j in range(len(formas)):
                    if formas[j][i] != 0:
                        texto = f'{texto}(+{str(formas[j][i])} {str(formas[j][6])})'
                texto = f'{texto}[/color] '

        # Arma
        if pontos[i][6] != 0:
            if cores[4] == 'white':
                texto = f'{texto}(+{str(pontos[i][6])} Arma) '
            else:
                texto = f'{texto}[color={cores[4]}](+{str(pontos[i][6])}Arma)[/color] '                   
       
        # Haki
        if pontos[i][4] != 0:
            if i == 0 or i == 5:
                if cores[5] == 'white':    
                    texto = f'{texto}(+{str(pontos[i][4])} Busoushoku) '
                else:    
                    texto = f'{texto}[color={cores[5]}](+{str(pontos[i][4])} Busoushoku)[/color] '
            else:
                if cores[6] == 'white':
                    texto = f'{texto}(+{str(pontos[i][4])} Kensbunshoku) '
                else:    
                    texto = f'{texto}[color={cores[6]}](+{str(pontos[i][4])} Kenbunshoku)[/color] '

        # Caminho do Haki
        if pontos[i][5] != 0:
            if i == 0 or i == 5:
                if cores[5] == 'white':
                    for j in range(5,-1,-1):
                        if dados[21+j] == 1 and database.Especializacoes[j][i] != 0:
                            texto = f'{texto}(+{str(database.Especializacoes[j][i])} {str(database.Especializacoes[j][6])}) '
                else:
                    texto = f'{texto[0:len(texto)-8]}'
                    for j in range(5,-1,-1):
                        if dados[21+j] == 1 and database.Especializacoes[j][i] != 0:
                            texto = f'{texto}(+{str(database.Especializacoes[j][i])} {str(database.Especializacoes[j][6])})'
                    texto = f'{texto}[/color] '
            else:
                if cores[6] == 'white':
                    for j in range(5,-1,-1):
                        if dados[29+j] == 1 and database.Especializacoes[6+j][i] != 0:
                            texto = f'{texto}(+{str(database.Especializacoes[6+j][i])} {str(database.Especializacoes[6+j][6])}) '
                else:
                    texto = f'{texto[0:len(texto)-8]}'
                    for j in range(5,-1,-1):
                        if dados[29+j] == 1 and database.Especializacoes[6+j][i] != 0:
                            texto = f'{texto}(+{str(database.Especializacoes[6+j][i])} {str(database.Especializacoes[6+j][6])})'
                    texto = f'{texto}[/color] '

        # Itens
        if pontos[i][7] != 0:
            if dados[40] == 1:
                if cores[7] == 'white':
                    texto = f'{texto}(+ {str(pontos[i][7])} Itens) '
                else:
                    texto = f'{texto}[color={cores[7]}](+ {str(pontos[i][7])} Itens)[/color] '
            else:
                if cores[7] == 'white':
                    for j in range(len(itens)):
                        if itens[j][i] != 0:
                            texto = f'{texto}(+{str(itens[j][i])} {str(itens[j][6])}) '
                else:
                    texto = f'{texto}[color={cores[7]}]'
                    for j in range(len(itens)):
                        if itens[j][i] != 0:
                            texto = f'{texto}(+{str(itens[j][i])} {str(itens[j][6])})'
                    texto = f'{texto}[/color] '

        # Bônus
        if pontos[i][8] != 0:
            if cores[8] == 'white':
                texto = f'{texto}(+ {str(pontos[i][8])} Bônus) '
            else:
                texto = f'{texto}[color={cores[8]}](+ {str(pontos[i][8])} Bônus)[/color] '
                   
        # Soma
        if cores[9] == 'white':
            texto = f'{texto} = {str(pontos[i][9])} '
        else:
            texto = f'{texto} = [color={cores[9]}]{str(pontos[i][9])}[/color] '
        
        # Classificação
        if cores[10] == 'white':
            texto = f'{texto}~ {str(Graduacao.classificacao(pontos[i][9]))}\n'
        else:
            texto = f'{texto}~ [color={cores[10]}]{str(Graduacao.classificacao(pontos[i][9]))}[/color]\n'
          
    texto = f'{texto}[b]VELOCIDADE DE ATAQUE:[/b] 3\n'

    return texto
