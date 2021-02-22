# Programa Criador de Fichas de OPRPG  22/05/2018
# Versão 2.0 - 20/12/2020
# Criado por PepePepi
# Python 3.9

# Imports do Kivy
import kivy
from kivy.app import App
from kivy.uix.widget  import Widget
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.checkbox import CheckBox
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput

from plyer import filechooser

# Imports do Meu Programa
import Atributos # Função para processar a somatória de um atributo
import Bonus # Função para calcular o bônus
import database # Tamanho de fonte, Nome das graduações, Nomes e atributos das raças
import ExportarDados # Função para exportar dados para um txt
import Graduacao # Uma função que retorna a graduação de um atributo
import Haki # Programa com funções que envolvem haki
import Level # Funções que envolvem a experiência do usuário ou o seu level

import os # Para baixar e importar os dados

####################################################################################################################
# Variáveis globais que serão utilizadas

global lvl
lvl = 1
global lvlPro
lvlPro = 1
global pontos
global pontosPro # Igual a pontos, só que da projeção
# Pontos é uma matriz onde:
# As linhas são os atributos
# E as colunas são Bruto, Racial, Edc, Akuma, Haki, Comp.Haki, Arma, Itens, Bonus, Total
# E as colunas são   0  ,   1   ,  2 ,   3  ,   4 ,     5    ,   6 ,   7  ,   8  ,   9
pontos = []
pontosPro = []

for i in range(0, 6):
    vet = []
    for j in range(0, 10):
        vet.append(0)  # preenche cada coluna da linha da matriz com zero
    pontos.append(vet)

for i in range(0, 6):
    vet = []
    for j in range(0, 10):
        vet.append(0)  # preenche cada coluna da linha da matriz com zero
    pontosPro.append(vet)

global dados # Vetor de dados que sei que não conseguem criar  mais opções como itens ou formas zoans
global dadosPro # Vetor igual o de dados, só que para projeção
# Dados é uma matriz que possui os seguintes dados em sequência: 
# EXP (0), BERRIES (1), BANCO (2), 
# Bru1 (3), Bru2 (4), Bru3 (5), Bru4 (6), Bru5 (7), Bru6 (8)
# Raça (9), EscRaça1 (10), EscRaça2 (11), 
# EDC_1 (12), EDC_2 (13), EDC_3 (14), EDC_4 (15), EDC_5 (16), EDC_6 (17),
# Akuma Mult (18) 
# HakiB (19), ExpHakiB (20), Opç1 (21), Opç2 (22), Opç3 (23), Opc4 (24), Opc5 (25), Opc6 (26), 
# HakiK (27), ExpHakiK (28), Opç1 (29), Opç2 (30), Opç3 (31), Opç4 (32), Opc5 (33), Opc6 (34), 
# HakiRei (35)
# TipoArma (36), dano (37), acerto (38), pontaria (39)
# InfoItens(40)

dados = []
dadosPro = []
for i in range(0, 41):
    dados.append(0)
    dadosPro.append(0)

global formas
formas = []

global colors
#         Bruto    Racial      EDC        Akuma      Arma    Haki Busou  Haki K    Itens       Bonus    total   clas
colors = ['white', '#0000ff', '#660000', '#ccccff', 'white', 'gray', 'softblue', '#66cc99', 'orange', 'white', 'white']

global itens
itens = []

global principal
principal = 0

global projecao
projecao = 0

####################################################################################################################

Builder.load_file('ficha.kv')

####################################################################################################################

class StartScreen(Screen):
    pass
    def PegarDados(self):
        #path = filechooser.open_file(title="Qual ficha vai atualizar?", 
        #                     filters=[("Comma-separated Values", "*.txt")])

        path = filechooser.open_file(title="Qual ficha vai atualizar?", 
                             filters=[("*.txt")])


        if path == []:
            avisoPath = Popup(title='Path Not Found',
                        content=Label(text='Tem certeza que selecionou algo?', halign='center', valign='middle'),
                        size_hint=(None, None), size=(400,200))
            avisoPath.open()
            return

        texto = open(path[0], "r")

        erro = self.AttDados(texto)
        texto.close()
        if erro == 1:
            avisoArquivo = Popup(title='Algo de errado não está certo',
                        content=Label(text='O arquivo que você selecionou não bateu com o padrão pedido por algum motivo.\nTente outro...', halign='center', valign='middle'),
                        size_hint=(None, None), size=(700,200))
            avisoArquivo.open()
            return
        self.manager.get_screen('attxp').AttInput()
        self.manager.current = 'attxp'

    def AttDados(self, texto):
        try:
            # Coletando os primeiros 40 dados
            for i in range(len(dados)):
                if i != 1 and i != 2:
                    dados[i] = int(texto.readline())
                else:
                    dados[i] = texto.readline()
                    dados[i] = dados[i][0:(len(dados[i])-1)]
    
            # Coletando as formas de Akumas

            auxAkuma = 0
            while True:
                aux2 = []
                for i in range(7):
                    aux2.append(texto.readline())
                    if aux2[len(aux2)-1] == 'Acabou\n':
                        auxAkuma = 1
                        break
                if auxAkuma == 1:
                    break
                formas.append(aux2)

            # Pegando as cores
            for i in range(11):
                colors[i] = texto.readline()
                colors[i] = colors[i][0:len(colors[i])-1]

            # Pegando os itens
            aux2 = 0
            while True:
                aux = []
                for i in range(7):
                    aux.append(texto.readline())
                    if aux[len(aux)-1] == '':
                        aux2 = 1
                        break
                if aux2 == 1:
                    break
                itens.append(aux)


            for i in range(len(formas)):
                for j in range(0,7):
                    if j == 6:
                        aux = formas[i][6]
                        formas[i][6] = aux[0:len(aux)-2]
                    else:
                        formas[i][j] = int(formas[i][j])
            for i in range(len(itens)):
                for j in range(0,7):
                    if j == 6:
                        aux = itens[i][6]
                        itens[i][6] = aux[0:len(aux)-2]
                    else:
                        itens[i][j] = int(itens[i][j])
            return 0
        except:
            return 1

class InputXPScreen(Screen):
    pass
    
    def processarXP(self, expInput):
        global lvl
        global dados
        
        try:
            exp = int(expInput.text)
        except ValueError:
            self.ZerarXP(expInput)
            avisoXpInv = Popup(title='XP Inválida',
                        content=Label(text='A sua experiência só existe\nentre os valores de 10 e 400\nPor favor arrume', halign='center', valign='middle'),
                        size_hint=(None, None), size=(400,200))
            avisoXpInv.open()
            return

        auxerr, dados[0] = Level.AttExp(dados[0],exp)           
        lvl = Level.level(dados[0]) 

        if auxerr == 0:
            self.manager.current = 'raca'          
        else:
            self.ZerarXP(expInput)
            avisoXpInv = Popup(title='XP Inválida',
                        content=Label(text='A sua experiência só existe\nentre os valores de 10 e 400\nPor favor arrume', halign='center', valign='middle'),
                        size_hint=(None, None), size=(400,200))
            avisoXpInv.open()
        
    def ZerarXP(self,expInput):
        expInput.text = "10"

class AttXPScreen(Screen):
    pass
    def AttInput(self):
        global lvl 
        lvl  = Level.level(dados[0])

        if lvl > 3 and (dados[19] == 1 or dados[27] == 1):
            self.ids.apresentacao.text = "Aparentemente você já possuia Haki, por isso poderá colocar um ganho para ele"
            self.ids.inputexpextra.disabled = False
        else:
            self.ids.apresentacao.text = "Aparentemente a ficha que você colocou não possuía haki"
            self.ids.inputexpextra.disabled = True

    def AttFicha(self):
        global lvl
    
        if self.ids.inputexp.text != '':
            dados[0] = dados[0] + int(self.ids.inputexp.text)

        if self.ids.inputexpextra.text != '':
            dados[20] = dados[20] + int(self.ids.inputexpextra.text)*dados[19]
            dados[28] = dados[28] + int(self.ids.inputexpextra.text)*dados[27]

        lvl = Level.level(dados[0])

        for i in range(0,6):
            # Atualizando Pontos do Bruto
            pontos[i][0] = dados[3+i]

            # Atualizando Pontos do EDC
            pontos[i][2] = dados[12+i]*lvl

        # Atualizando Pontos Raciais
        Atributos.ProcessarRaca(pontos,dados[9], dados[10], dados[11])

        # Atalizando Pontos da Akuma
        if len(formas) != 0:
            for i in range(0,6):
                pontos[i][3] = formas[0][i]

        # Atualizando Pontos de Haki
        pontos[0][4], pontos[5][4], temp, temp = Haki.pontoshaki(dados[20])
        pontos[1][4], pontos[2][4], pontos[3][4], pontos[4][4] = Haki.pontoshaki(dados[28])

        del temp

        # Atualizando Pontos do Caminho do Haki
        pontos[0][5], pontos[5][5] = Haki.pontosCaminhoBusou(dados[21],dados[22],dados[23],dados[24],dados[25],dados[26])
        pontos[1][5], pontos[2][5], pontos[3][5], pontos[4][5] = Haki.pontosCaminhoKenbun(dados[29],dados[30],dados[31],dados[32],dados[33],dados[34])
   
        # Atualizando Pontos das Armas
        if dados[36] == 0:
            pontos[0][6] = dados[37]
        elif dados[36] == 1:
            pontos[0][6] = dados[37]*lvl
        else:  
            pontos[0][6] = dados[37]*lvl
            pontos[1][6] = dados[38]*lvl
            pontos[2][6] = dados[39]*lvl

        # Atualizando Pontos dos Itens
        self.manager.get_screen('item').ProcessarItens(0)
        self.manager.get_screen('mainscreen').ModoNormal()
        self.manager.current = 'mainscreen'

class RacaScreen(Screen):
    pass

    def MudarRaca(self, raiz, valor):
        if projecao == 0:
            dados[9] = valor
        else:
            dadosPro[9] = valor

        if database.ShowRaca[valor][0] == 1:
            raiz.acerto.disabled = False
            raiz.pontaria.disabled = False
        else:
            raiz.acerto.disabled = True
            raiz.pontaria.disabled = True

        if database.ShowRaca[valor][1] == 1:
            raiz.esquiva.disabled = False
            raiz.bloqueio.disabled = False
        else:
            raiz.esquiva.disabled = True
            raiz.bloqueio.disabled = True

    def ProcessarRaca(self, valor1, valor2, valor3, valor4):

        if database.ShowRaca[dados[9]][0] == 1 and (valor1.state == 'normal' and valor3.state == 'normal'):
            avisoEscolha = Popup(title='Sem escolha',
                        content=Label(text='Você não escolheu entre Acerto e Pontaria\nPor favor arrume', halign='center', valign='middle'),
                        size_hint=(None, None), size=(400,200))
            avisoEscolha.open()
            return

        if database.ShowRaca[dados[9]][1] == 1 and (valor2.state == 'normal' and valor4.state == 'normal'):
            avisoEscolha = Popup(title='Sem escolha',
                        content=Label(text='Você não escolheu entre Esquiva e Bloqueio\nPor favor arrume', halign='center', valign='middle'),
                        size_hint=(None, None), size=(400,200))
            avisoEscolha.open()
            return

        if valor1.state == 'down':
            Esc1 = 0
        else:
            Esc1 = 1

        if valor2.state == 'down':
            Esc2 = 0
        else:
            Esc2 = 1

        if projecao == 0:
            dados[10] = Esc1
            dados[11] = Esc2
            Atributos.ProcessarRaca(pontos,dados[9], Esc1, Esc2)
        else:
            dadosPro[10] = Esc1
            dadosPro[11] = Esc2
            Atributos.ProcessarRaca(pontosPro,dadosPro[9], Esc1, Esc2)

        self.QualTela()

    def QualTela(self):
        global principal
        if principal == 0:
            if lvl < 3:
                self.manager.current = 'basicedc'
            else:
                self.manager.current = 'choiceedc'
        else:
            self.manager.get_screen('mainscreen').AttRacial()
            self.manager.get_screen('mainscreen').AttBonus()
            self.manager.get_screen('mainscreen').AttTotal()
            self.manager.current = 'mainscreen'

class BasicEDCScreen(Screen):
    pass
    def edcdone(self, dano, acerto, esquiva):
        if projecao == 0:
            if dano.state == 'down':
                dados[12] = 2
                dados[17] = 0
            else:
                dados[12] = 0
                dados[17] = 2

            if acerto.state == 'down':
                dados[13] = 2
                dados[14] = 0
            else:
                dados[13] = 0
                dados[14] = 2

            if esquiva.state == 'down':
                dados[15] = 2
                dados[16] = 0
            else:
                dados[15] = 0
                dados[16] = 2

            for i in range(0,6):
                pontos[i][2] = dados[12+i]*lvl
        else:
            if dano.state == 'down':
                dadosPro[12] = 2
                dadosPro[17] = 0
            else:
                dadosPro[12] = 0
                dadosPro[17] = 2

            if acerto.state == 'down':
                dadosPro[13] = 2
                dadosPro[14] = 0
            else:
                dadosPro[13] = 0
                dadosPro[14] = 2

            if esquiva.state == 'down':
                dadosPro[15] = 2
                dadosPro[16] = 0
            else:
                dadosPro[15] = 0
                dadosPro[16] = 2

            for i in range(0,6):
                pontosPro[i][2] = dadosPro[12+i]*lvl
                
        if principal == 0:
            self.manager.get_screen('mainscreen').ModoNormal()
            self.manager.current = 'mainscreen'

        else:
            self.manager.get_screen('mainscreen').AttEDC()
            self.manager.get_screen('mainscreen').AttBonus()
            self.manager.get_screen('mainscreen').AttTotal()
            self.manager.current = 'mainscreen'
            
class ChoiceEDCScreen(Screen):
    pass

    def NaoMudei(self):
        self.manager.current = 'basicedc'
    
    def Mudei(self):
        self.manager.current = 'modifiededc'

class ModifiedEDC(Screen):
    pass

    def ProcessarEDC(self, dano, acerto, pontaria, esquiva, bloqueio, resistencia):
        if dano.text == '':
            dan = 0
        else:
            dan = int(dano.text)

        if acerto.text == '':
            ace = 0
        else:
            ace = int(acerto.text)

        if pontaria.text == '':
            pon = 0
        else:
            pon = int(pontaria.text)

        if esquiva.text == '':
            esq = 0
        else:
            esq = int(esquiva.text)

        if bloqueio.text == '':
            blo = 0
        else:
            blo = int(bloqueio.text)

        if resistencia.text == '':
            res = 0
        else:
            res = int(resistencia.text)

        if dan + ace + pon + esq + blo + res != 6:
            avisoValorInv = Popup(title='Valor Inválido',
                        content=Label(text='EDC necessariamente distribui 6 pontos por Level\nPor favor arrume', halign='center', valign='middle'),
                        size_hint=(None, None), size=(400,200))
            avisoValorInv.open()
            return

        if dan == 6 or ace == 6 or pon == 6 or esq == 6 or blo == 6 or res >= 3:
            avisoValorInv = Popup(title='Valor Inválido',
                        content=Label(text='A distribuição máxima de um atributo é 5x lvl\nLembrando que o limite da Resistência é 2x porque sim\nPor favor arrume', halign='center', valign='middle'),
                        size_hint=(None, None), size=(400,200))
            avisoValorInv.open()
            return

        if projecao == 0:
            dados[12] = dan
            dados[13] = ace
            dados[14] = pon
            dados[15] = esq
            dados[16] = blo
            dados[17] = res

            for i in range(0,6):
                pontos[i][2] = dados[12+i]*lvl
        else:
            dadosPro[12] = dan
            dadosPro[13] = ace
            dadosPro[14] = pon
            dadosPro[15] = esq
            dadosPro[16] = blo
            dadosPro[17] = res

            for i in range(0,6):
                pontosPro[i][2] = dadosPro[12+i]*lvl

        if principal == 0:
            self.manager.get_screen('mainscreen').ModoNormal()
            self.manager.current = 'mainscreen'
        else:
            self.manager.get_screen('mainscreen').AttEDC()
            self.manager.get_screen('mainscreen').AttBonus()
            self.manager.get_screen('mainscreen').AttTotal()
            self.manager.current = 'mainscreen'

class AkumaScreen(Screen):
    pass

    def AttList(self):
        texto = ""
        for i in range(len(formas)):
            texto = texto + "Item " + str(i) + " - Nome: " + formas[i][6] + " - Atributos: " + str(formas[i][0]) + ", " + str(formas[i][1]) + ", " + str(formas[i][2]) + ", " + str(formas[i][3]) + ", " + str(formas[i][4]) + ", " + str(formas[i][5]) + "\n"

        if len(formas) == 0:
            texto = "Lista Vazia"

        self.ids.listaakuma.text = texto

    def ChangeMul(self,valor):
        if dados[18] != valor and len(formas) > 0:
            self.boxPopApagar = BoxLayout()
            self.boxPopApagar.orientation = 'vertical'
            self.boxPopApagar.add_widget(Label(text="Você tem certeza que quer realizar essa mudança?"))
            self.boxPopApagar.add_widget(Label(text="Isso apagará todas as formas que você possui"))

            self.gridPopApagar = GridLayout()
            self.gridPopApagar.cols = 2
            self.ButtonNao = Button(text = "Não", on_press = lambda a: self.ProcessarMudanca(valor,0))
            self.ButtonSim = Button(text = "Sim", on_press = lambda a: self.ProcessarMudanca(valor,1))
            
            self.gridPopApagar.add_widget(self.ButtonNao)
            self.gridPopApagar.add_widget(self.ButtonSim)
            
            self.boxPopApagar.add_widget(self.gridPopApagar)

            self.avisoApagar = Popup(title='Tem certeza?', content= self.boxPopApagar, size_hint=(None, None), size=(400,200),auto_dismiss=False)
            self.avisoApagar.open()
        else:
            self.ProcessarMudanca(valor,1)

    def ProcessarMudanca(self, valor, escolha):
        global formas
        if len(formas) > 0:
            self.avisoApagar.dismiss()

        if escolha == 0:
            if valor == 9:
                self.ids.mul8.state = 'down'
                self.ids.mul9.state = 'normal'
            else:
                self.ids.mul8.state = 'normal'
                self.ids.mul9.state = 'down' 

        else:
            dados[18] = valor
            formas = []
            self.AttList()

    def SwapForm(self,num):
        
        aux = int(num.text)
        if aux+1 > len(formas):
            avisoValorInv = Popup(title='Valor Inválido',
                        content=Label(text='Você está tentando colocar uma forma no topo acima do que existe\nPor favor arrume', halign='center', valign='middle'),
                        size_hint=(None, None), size=(500,200))
            avisoValorInv.open()
            return
        
        auxLista = formas.pop(aux)

        formas.insert(0,auxLista)

        self.AttList()

    def DelList(self, num):

        try:
            aux = int(num.text)
        except ValueError:
            avisoValorInv = Popup(title='Valor Inválido',
                        content=Label(text='Favor colocar algum número que deseja apagar', halign='center', valign='middle'),
                        size_hint=(None, None), size=(400,200))
            avisoValorInv.open()
            return

        if aux+1 > len(formas):
            avisoValorInv = Popup(title='Valor Inválido',
                        content=Label(text='Você está tentando apagar um valor acima do que existe\nPor favor arrume', halign='center', valign='middle'),
                        size_hint=(None, None), size=(400,200))
            avisoValorInv.open()
            return

        formas.remove(formas[aux])

        self.AttList()

    def CreateForm(self, dano, acerto, pontaria, esquiva, bloqueio, resistencia, nome):
        if dano.text == '':
            dan = 0
        else:
            dan = int(dano.text)

        if acerto.text == '':
            ace = 0
        else:
            ace = int(acerto.text)

        if pontaria.text == '':
            pon = 0
        else:
            pon = int(pontaria.text)

        if esquiva.text == '':
            esq = 0
        else:
            esq = int(esquiva.text)

        if bloqueio.text == '':
            blo = 0
        else:
            blo = int(bloqueio.text)

        if resistencia.text == '':
            res = 0
        else:
            res = int(resistencia.text)

        if dan + ace + pon + esq + blo + res != dados[18]:
            avisoValorInv = Popup(title='Valor Inválido',
                        content=Label(text='A opção selecionada de multiplicador\nnão está igual a soma dos valores que você colocou\nPor favor arrume', halign='center', valign='middle'),
                        size_hint=(None, None), size=(400,200))
            avisoValorInv.open()
            return

        aux = []
        aux.append(dan)
        aux.append(ace)
        aux.append(pon)
        aux.append(esq)
        aux.append(blo)
        aux.append(res)

        for i in range(5,-1,-1):            
            if aux[i] == 0:
                del(aux[i])

        aux.sort()

        if len(aux) < 3 or aux[1] < 2:
            avisoValorInv = Popup(title='Valores Inválidos',
                        content=Label(text='Uma forma de Zoan precisa posuir pelo menos 3 atributos bonificados\n'
                                        'Sendo o menor pelo menos 1x e o segundo menor pelo menos 2x\n'
                                        'Por favor arrume', halign='center', valign='middle'),
                        size_hint=(None, None), size=(600,200))
            avisoValorInv.open()
            return

        aux2 = []
        aux2.append(dan)
        aux2.append(ace)
        aux2.append(pon)
        aux2.append(esq)
        aux2.append(blo)
        aux2.append(res)
        aux2.append(nome.text)

        formas.append(aux2)

        self.AttList()

    def ProcessarAkuma(self):
        # Atualizar os pontos de Akuma
        if len(formas) != 0:
            for i in range(0,6):
                pontos[i][3] = lvl*formas[0][i]
                pontosPro[i][3] = lvlPro*formas[0][i]
            
        else:
            for i in range(0,6):
                pontos[i][3] = 0
                pontosPro[i][3] = 0

        self.AttList()

        self.manager.get_screen('mainscreen').AttAkuma()

        # Atualizar o Bônus
        self.manager.get_screen('mainscreen').AttBonus()
        
        self.manager.get_screen('mainscreen').AttTotal()
        self.manager.current = 'mainscreen'

class HakiScreen(Screen):
    pass
    def ProcessarHaki(self, xpb, xpk):       
        if xpb.text == '':
            hakiB = 0
        else:
            hakiB = int(xpb.text)
        if xpk.text == '':
            hakiK = 0
        else:
            hakiK = int(xpk.text)

        if projecao == 0:
            hakiB = hakiB * dados[19]
            hakiK = hakiK * dados[27]
        else:
            hakiB = hakiB * dadosPro[19]
            hakiK = hakiK * dadosPro[27]

        if hakiB > 75 or hakiB < 0 or hakiK > 75 or hakiK < 0:
            avisoXPInv = Popup(title='XP Inválida',
                        content=Label(text='Favor colocar um valor de EXP válido.\nA EXP para Haki só existe entre os valores 0 a 75', halign='center', valign='middle'),
                        size_hint=(None, None), size=(400,200))
            avisoXPInv.open()
            return
        
        if projecao == 0:
            dados[20] = hakiB
            dados[28] = hakiK
        else:
            dadosPro[20] = hakiB
            dadosPro[28] = hakiK
            
        if projecao == 0:
            pontos[0][4], pontos[5][4], temp, temp = Haki.pontoshaki(hakiB)
            pontos[1][4], pontos[2][4], pontos[3][4], pontos[4][4] = Haki.pontoshaki(hakiK)
        else:
            pontosPro[0][4], pontosPro[5][4], temp, temp = Haki.pontoshaki(hakiB)
            pontosPro[1][4], pontosPro[2][4], pontosPro[3][4], pontosPro[4][4] = Haki.pontoshaki(hakiK)
            

        del temp

        self.manager.get_screen('mainscreen').AttHaki()

        if hakiB <= 25 and hakiK <= 25:
            self.manager.get_screen('mainscreen').AttTotal()
            self.manager.current = 'mainscreen'
        else:
            self.manager.get_screen('caminho').AttInput()
            self.manager.current = 'caminho'

    def AttBusou(self):
        if (projecao == 0 and lvl == 4 and dados[27] == 1) or (projecao == 1 and lvlPro == 4 and dadosPro[27] == 1):
                avisoLvlIns = Popup(title='Nope',
                            content=Label(text='Somente no Level 5 para cima para ter os dois', halign='center', valign='middle'),
                            size_hint=(None, None), size=(400,200))
                avisoLvlIns.open()
                self.ids.busou.state = 'normal'
                return

        if projecao == 0:
            dados[19] = 1 - dados[19]    
        else:
            dadosPro[19] = 1 - dadosPro[19]
        
        self.AttInputB()

    def AttInputB(self):
        if (projecao == 0 and dados[19] == 1) or (projecao == 1 and dadosPro[19] == 1):
            self.ids.inputxpbusou.disabled = False
            self.ids.busou.state = 'down'
        else:
            self.ids.inputxpbusou.disabled = True
            self.ids.busou.state = 'normal'

        if projecao == 0:
            self.ids.inputxpbusou.text = f'{dados[20]}'
        else:
            self.ids.inputxpbusou.text = f'{dadosPro[20]}'
        
    def AttKenbun(self):
        if (projecao == 0 and lvl == 4 and dados[19] == 1) or (projecao == 1 and lvlPro == 4 and dadosPro[19] == 1):
            avisoLvlIns = Popup(title='Nope',
                            content=Label(text='Somente no Level 5 para cima para ter os dois', halign='center', valign='middle'),
                            size_hint=(None, None), size=(400,200))
            avisoLvlIns.open()
            self.ids.kenbun.state = 'normal'
            return

        if projecao == 0:
            dados[27] = 1 - dados[27]    
        else:
            dadosPro[27] = 1 - dadosPro[27]
        
        self.AttInputK()

    def AttInputK(self):
        if (projecao == 0 and dados[27] == 1) or (projecao == 1 and dadosPro[27] == 1):
            self.ids.inputxpkenbun.disabled = False
            self.ids.kenbun.state = 'down'
        else:
            self.ids.inputxpkenbun.disabled = True
            self.ids.kenbun.state = 'normal'

        if projecao == 0:
            self.ids.inputxpkenbun.text = f'{dados[28]}'
        else:
            self.ids.inputxpkenbun.text = f'{dadosPro[28]}'

    def AttRei(self):
        if projecao == 0:
            dados[35] = 1 - dados[35]
            self.HakiRei()
        else:
            dadosPro[35] = 1 - dadosPro[35]
            self.HakiRei()

    def HakiRei(self):
        if (dados[35] == 1 and projecao == 0) or (dadosPro[35] == 1 and projecao == 1):
            self.ids.rei.state = 'down'
        else:
            self.ids.rei.state = 'normal'

class CaminhoScreen(Screen):
    pass
    def AttInput(self):
        if (dados[20] == 75 and projecao == 0) or (dadosPro[20] == 75 and projecao == 1):
            self.ids.imbuir.disabled = False
            self.ids.tribal.disabled = False
            self.ids.superioridade.disabled = False
            self.ids.ryou.disabled = False
            self.ids.impregnacao.disabled = False
            self.ids.corpo.disabled = False            
        elif (75 > dados[20] > 25 and projecao == 0) or (75 > dadosPro  [20] > 25 and projecao == 1):
            self.ids.imbuir.disabled = False
            self.ids.tribal.disabled = False
            self.ids.superioridade.disabled = False
            self.ids.ryou.disabled = True
            self.ids.ryou.state = 'normal'
            self.ids.impregnacao.disabled = True
            self.ids.impregnacao.state = 'normal'
            self.ids.corpo.disabled = True
            self.ids.corpo.state = 'normal'
        else:
            self.ids.imbuir.disabled = True
            self.ids.imbuir.state = 'normal'
            self.ids.tribal.disabled = True
            self.ids.tribal.state = 'normal'
            self.ids.superioridade.disabled = True
            self.ids.superioridade.state = 'normal'                
            self.ids.ryou.disabled = True
            self.ids.ryou.state = 'normal'
            self.ids.impregnacao.disabled = True
            self.ids.impregnacao.state = 'normal'
            self.ids.corpo.disabled = True
            self.ids.corpo.state = 'normal'

        if (dados[28] == 75 and projecao == 0) or (dadosPro[28] == 75 and projecao == 1):
            self.ids.foresight.disabled = False
            self.ids.verauras.disabled = False
            self.ids.emocoes.disabled = False
            self.ids.ouvirvozes.disabled = False            
            self.ids.previsao.disabled = False
            self.ids.vozcoisas.disabled = False
        elif (75 > dados[28] > 25 and projecao == 0) or (75 > dadosPro[28] > 25 and projecao == 1):
            self.ids.foresight.disabled = False
            self.ids.verauras.disabled = False
            self.ids.emocoes.disabled = False
            self.ids.ouvirvozes.disabled = False
            self.ids.previsao.disabled = True
            self.ids.previsao.state = 'normal'
            self.ids.vozcoisas.disabled = True
            self.ids.vozcoisas.state = 'normal'
        else:
            self.ids.foresight.disabled = True
            self.ids.foresight.state = 'normal'
            self.ids.verauras.disabled = True
            self.ids.verauras.state = 'normal'
            self.ids.emocoes.disabled = True
            self.ids.emocoes.state = 'normal'
            self.ids.ouvirvozes.disabled = True
            self.ids.ouvirvozes.state = 'normal'
            self.ids.previsao.disabled = True
            self.ids.previsao.state = 'normal'
            self.ids.vozcoisas.disabled = True
            self.ids.vozcoisas.state = 'normal'

        if projecao == 0:       
            if dados[21] == 1:
                self.ids.tribal.state = 'down'
            if dados[22] == 1:
                self.ids.imbuir.state = 'down'
            if dados[23] == 1:
                self.ids.superioridade.state = 'down'
            if dados[24] == 1:
                self.ids.ryou.state = 'down'
            if dados[25] == 1:
                self.ids.impregnacao.state = 'down'
            if dados[26] == 1:
                self.ids.corpo.state = 'down'

            if dados[29] == 1:
                self.ids.foresight.state = 'down'
            if dados[30] == 1:
                self.ids.verauras.state = 'down'
            if dados[31] == 1:
                self.ids.emocoes.state = 'down'
            if dados[32] == 1:
                self.ids.ouvirvozes.state = 'down'
            if dados[33] == 1:
                self.ids.previsao.state = 'down'
            if dados[34] == 1:
                self.ids.vozcoisas.state = 'down'
        else:
            if dadosPro[21] == 1:
                self.ids.tribal.state = 'down'
            if dadosPro[22] == 1:
                self.ids.imbuir.state = 'down'
            if dadosPro[23] == 1:
                self.ids.superioridade.state = 'down'
            if dadosPro[24] == 1:
                self.ids.ryou.state = 'down'
            if dadosPro[25] == 1:
                self.ids.impregnacao.state = 'down'
            if dadosPro[26] == 1:
                self.ids.corpo.state = 'down'

            if dadosPro[29] == 1:
                self.ids.foresight.state = 'down'
            if dadosPro[30] == 1:
                self.ids.verauras.state = 'down'
            if dadosPro[31] == 1:
                self.ids.emocoes.state = 'down'
            if dadosPro[32] == 1:
                self.ids.ouvirvozes.state = 'down'
            if dadosPro[33] == 1:
                self.ids.previsao.state = 'down'
            if dadosPro[34] == 1:
                self.ids.vozcoisas.state = 'down'
        
    def ProcessarCaminho(self, tri, imb, sup, ryo, imp, cor, fore, vera, emo, ouv, pre, voz):

        if tri.state == 'normal':
            B1 = 0
        else:
            B1 = 1
        
        if imb.state == 'normal':
            B2 = 0
        else:
            B2 = 1

        if sup.state == 'normal':
            B3 = 0
        else:
            B3 = 1

        if ryo.state == 'normal':
            B4 = 0
        else:
            B4 = 1
        
        if imp.state == 'normal':
            B5 = 0
        else:
            B5 = 1

        if cor.state == 'normal':
            B6 = 0
        else:
            B6 = 1
        

        if fore.state == 'normal':
            K1 = 0
        else:
            K1 = 1
        
        if vera.state == 'normal':
            K2 = 0
        else:
            K2 = 1

        if emo.state == 'normal':
            K3 = 0
        else:
            K3 = 1

        if ouv.state == 'normal':
            K4 = 0
        else:
            K4 = 1
        
        if pre.state == 'normal':
            K5 = 0
        else:
            K5 = 1

        if voz.state == 'normal':
            K6 = 0
        else:
            K6 = 1

        if projecao == 0:
            if dados[19] == 0:
                B1 = 0
                B2 = 0
                B3 = 0
                B4 = 0
                B5 = 0
                B6 = 0
            if dados[27] == 0:
                K1 = 0
                K2 = 0
                K3 = 0
                K4 = 0
                K5 = 0
                K6 = 0  
        else:
            if dadosPro[19] == 0:
                B1 = 0
                B2 = 0
                B3 = 0
                B4 = 0
                B5 = 0
                B6 = 0
            if dadosPro[27] == 0:
                K1 = 0
                K2 = 0
                K3 = 0
                K4 = 0
                K5 = 0
                K6 = 0  

        if (dados[20] < 75 and projecao == 0) or (dadosPro[20] < 75 and projecao == 1):
            if B1 + B2 + B3 > 1:
                avisoHakiDemais = Popup(title='Nope',
                        content=Label(text='Você só pode ter um haki intermediário com essa EXP\nFavor Arrumar', halign='center', valign='middle'),
                        size_hint=(None, None), size=(400,200))
                avisoHakiDemais.open()   
                return
            
        if (dados[28] < 75 and projecao == 0) or (dadosPro[28] < 75 and projecao == 1):
            if K1 + K2 + K3 + K4 > 1:
                avisoHakiDemais = Popup(title='Nope',
                        content=Label(text='Você só pode ter um haki intermediário com essa EXP\nFavor Arrumar', halign='center', valign='middle'),
                        size_hint=(None, None), size=(400,200))
                avisoHakiDemais.open()   
                return

        if ((B4 == 1) or (B5 == 1) or (B6 == 1)) and ((K5 == 1) or (K6==1)):
            avisoHakiDemais = Popup(title='Nope',
                        content=Label(text='Parabéns pelos 75 de experiência em ambos os Hakis\nSó que você só pode ser mestre de um deles.\nNo segundo você pode pegar dois intermediários pelo menos\nFavor Arrumar', halign='center', valign='middle'),
                        size_hint=(None, None), size=(450,200))
            avisoHakiDemais.open()   
            return

        if (dados[20] == 75 and projecao == 0) or (dadosPro[20] == 75 and projecao == 1):
            if B1 + B2 + B3 + B4 + B5 + B6 > 2:
                avisoHakiDemais = Popup(title='Nope',
                        content=Label(text='Você só pode ter um haki avançado (lembre-se de marcar o intermediário antecessor)\nOu dois hakis intermediários\nFavor Arrumar', halign='center', valign='middle'),
                        size_hint=(None, None), size=(550,200))
                avisoHakiDemais.open()
                return
            
            if B4 == 1 and B1 != 1:
                avisoHakiErrado = Popup(title='Nope',
                        content=Label(text='Para aprender Ryou é necessário ter o Tribal\nFavor Arrumar', halign='center', valign='middle'),
                        size_hint=(None, None), size=(400,200))
                avisoHakiErrado.open()
                return
            
            if B5 == 1 and B2 != 1:
                avisoHakiErrado = Popup(title='Nope',
                        content=Label(text='Para aprender Impregnação Permanente é necessário ter o Imbuir\nFavor Arrumar', halign='center', valign='middle'),
                        size_hint=(None, None), size=(500,200))
                avisoHakiErrado.open()
                return
            
            if B6 == 1 and B3 != 1:
                avisoHakiErrado = Popup(title='Nope',
                        content=Label(text='Para aprender Corpo Completo é necessário ter o Superioridade\nFavor Arrumar', halign='center', valign='middle'),
                        size_hint=(None, None), size=(500,200))
                avisoHakiErrado.open()
                return
        
        if (dados[28] == 75 and projecao == 0) or (dadosPro[28] == 75 and projecao == 1):
            if K1 + K2 + K3 + K4 + K5 + K6 > 2:
                avisoHakiDemais = Popup(title='Nope',
                        content=Label(text='Você só pode ter um haki avançado (lembre-se de marcar o intermediário antecessor)\nOu dois hakis intermediários\nFavor Arrumar', halign='center', valign='middle'),
                        size_hint=(None, None), size=(600,200))
                avisoHakiDemais.open()
                return
            
            if K5 == 1 and K1 != 1:
                avisoHakiErrado = Popup(title='Nope',
                        content=Label(text='Para aprender Previsão do Futuro é necessário ter o Foresight\nFavor Arrumar', halign='center', valign='middle'),
                        size_hint=(None, None), size=(450,200))
                avisoHakiErrado.open()
                return

            if K6 == 1 and K4 != 1:
                avisoHakiErrado = Popup(title='Nope',
                        content=Label(text='Para aprender A Voz de Todas as Coisas é necessário ter o Ouvir Vozes\nFavor Arrumar', halign='center', valign='middle'),
                        size_hint=(None, None), size=(500,200))
                avisoHakiErrado.open()
                return

        if projecao == 0:
            dados[21:27] = Haki.AttCaminho(B1,B2,B3,B4,B5,B6)
            dados[29:35] = Haki.AttCaminho(K1,K2,K3,K4,K5,K6)

            pontos[0][5], pontos[5][5] = Haki.pontosCaminhoBusou(B1,B2,B3,B4,B5,B6)
            pontos[1][5], pontos[2][5], pontos[3][5], pontos[4][5] = Haki.pontosCaminhoKenbun(K1,K2,K3,K4,K5,K6)
        else:
            dadosPro[21:27] = Haki.AttCaminho(B1,B2,B3,B4,B5,B6)
            dadosPro[29:35] = Haki.AttCaminho(K1,K2,K3,K4,K5,K6)

            pontosPro[0][5], pontosPro[5][5] = Haki.pontosCaminhoBusou(B1,B2,B3,B4,B5,B6)
            pontosPro[1][5], pontosPro[2][5], pontosPro[3][5], pontosPro[4][5] = Haki.pontosCaminhoKenbun(K1,K2,K3,K4,K5,K6)
        
        self.manager.get_screen('mainscreen').AttCaminho()
        self.manager.get_screen('mainscreen').AttTotal()
        self.manager.current = 'mainscreen'

class GunScreen(Screen):
    pass
    def AttInputs(self, num):
        if num == 0:
            self.ids.inputacertoarma.disabled = True
            self.ids.inputpontariaarma.disabled = True
            self.ids.babylon.state = 'normal'
            self.ids.lw.state = 'normal'
            self.ids.armanormal.state = 'down'
            self.ids.danoarma.text = "Dano de sua arma: "
        elif num == 1:
            self.ids.inputacertoarma.disabled = True
            self.ids.inputpontariaarma.disabled = True
            self.ids.babylon.state = 'normal'
            self.ids.lw.state = 'down'
            self.ids.armanormal.state = 'normal'
            self.ids.danoarma.text = "Multiplicador do Dano: "
        else:
            self.ids.babylon.state = 'down'
            self.ids.lw.state = 'normal'
            self.ids.armanormal.state = 'normal'
            self.ids.inputacertoarma.disabled = False
            self.ids.inputpontariaarma.disabled = False
            self.ids.danoarma.text = "Multiplicador do Dano: "
        
        if projecao == 0:
            self.ids.inputdanoarma.text = str(dados[37])
            self.ids.inputacertoarma.text = str(dados[38])
            self.ids.inputpontariaarma.text = str(dados[39])
        else:
            self.ids.inputdanoarma.text = str(dadosPro[37])
            self.ids.inputacertoarma.text = str(dadosPro[38])
            self.ids.inputpontariaarma.text = str(dadosPro[39])
        
    def ChangeGunType(self, num):
        if projecao == 0:
            dados[36] = num
            self.AttInputs(dados[36])
        else:
            dadosPro[36] = num
            self.AttInputs(dadosPro[36])

    def ProcessarArma(self, dan, ace, pon):
        if projecao == 0:
            if dados[36] == 0:
                dados[37] = dan.text
                dados[38] = 0
                dados[39] = 0
                pontos[0][6] = int(dan.text)
                pontos[1][6] = 0
                pontos[2][6] = 0
            elif dados[36] == 1:
                dados[37] = dan.text
                dados[38] = 0
                dados[39] = 0
                pontos[0][6] = int(dan.text)*lvl
                pontos[1][6] = 0
                pontos[2][6] = 0
            elif dados[36] == 2:
                dados[37] = int(dan.text)
                dados[38] = int(ace.text)
                dados[39] = int(pon.text)
                pontos[0][6] = int(dan.text)*lvl
                pontos[1][6] = int(ace.text)*lvl
                pontos[2][6] = int(pon.text)*lvl
        else:
            if dadosPro[36] == 0:
                dadosPro[37] = dan.text
                dadosPro[38] = 0
                dadosPro[39] = 0
                pontosPro[0][6] = int(dan.text)
                pontosPro[1][6] = 0
                pontosPro[2][6] = 0
            elif dadosPro[36] == 1:
                dadosPro[37] = dan.text
                dadosPro[38] = 0
                dadosPro[39] = 0
                pontosPro[0][6] = int(dan.text)*lvlPro
                pontosPro[1][6] = 0
                pontosPro[2][6] = 0
            elif dadosPro[36] == 2:
                dadosPro[37] = int(dan.text)
                dadosPro[38] = int(ace.text)
                dadosPro[39] = int(pon.text)
                pontosPro[0][6] = int(dan.text)*lvlPro
                pontosPro[1][6] = int(ace.text)*lvlPro
                pontosPro[2][6] = int(pon.text)*lvlPro
        self.manager.get_screen('mainscreen').AttArma()
        self.manager.get_screen('mainscreen').AttTotal()
        self.manager.current = 'mainscreen'

class ItemScreen(Screen):
    pass

    def AttBaixar(self):
        if dados[40] == 0:
            self.ids.itensjuntos.state = 'normal'
        else:
            self.ids.itensjuntos.state = 'down'

    def AltBaixar(self):
        dados[40] = 1 - dados[40]

    def AttList(self):
        texto = ""
        for i in range(len(itens)):
            texto = texto + "Item " + str(i) + " - Nome: " + itens[i][6] + " - Atributos: " + str(itens[i][0]) + ", " + str(itens[i][1]) + ", " + str(itens[i][2]) + ", " + str(itens[i][3]) + ", " + str(itens[i][4]) + ", " + str(itens[i][5]) + "\n"

        if len(itens) == 0:
            texto = "Lista Vazia"

        self.ids.listaitens.text = texto

    def DelList(self, num):
        
        try:
            aux = int(num.text)
        except ValueError:
            avisoValorInv = Popup(title='Valor Inválido',
                        content=Label(text='Favor colocar algum número que deseja apagar', halign='center', valign='middle'),
                        size_hint=(None, None), size=(400,200))
            avisoValorInv.open()
            return

        if aux+1 > len(itens):
            avisoValorInv = Popup(title='Valor Inválido',
                        content=Label(text='Você está tentando apagar um valor acima do que existe\nPor favor arrume', halign='center', valign='middle'),
                        size_hint=(None, None), size=(400,200))
            avisoValorInv.open()
            return

        itens.remove(itens[aux])

        self.AttList()

    def CreateItem(self, dano, acerto, pontaria, esquiva, bloqueio, resistencia, nome):
        if dano.text == '':
            dan = 0
        else:
            dan = int(dano.text)

        if acerto.text == '':
            ace = 0
        else:
            ace = int(acerto.text)

        if pontaria.text == '':
            pon = 0
        else:
            pon = int(pontaria.text)

        if esquiva.text == '':
            esq = 0
        else:
            esq = int(esquiva.text)

        if bloqueio.text == '':
            blo = 0
        else:
            blo = int(bloqueio.text)

        if resistencia.text == '':
            res = 0
        else:
            res = int(resistencia.text)

        aux = []
        aux.append(dan)
        aux.append(ace)
        aux.append(pon)
        aux.append(esq)
        aux.append(blo)
        aux.append(res)
        aux.append(nome.text)

        itens.append(aux)

        self.AttList()

    def ProcessarItens(self,val):
        for j in range(6):
            soma = 0
            for i in range(len(itens)):
                soma = soma + itens[i][j]
            pontos[j][7] = soma
        
        if val == 1:
            self.manager.get_screen('mainscreen').AttItens()
            self.manager.get_screen('mainscreen').AttTotal()
            self.manager.current = 'mainscreen'

class ColorScreen(Screen):
    pass

    def AttCor(self,bruto, racial, edc, akuma, arma, hakib, hakik, item, bonus, total, clas):

            if bruto.text != '':
                colors[0] = bruto.text

            if racial.text != '':
                colors[1] = racial.text

            if edc.text != '':
                colors[2] = edc.text

            if akuma.text != '':
                colors[3] = akuma.text

            if arma.text != '':
                colors[4] = arma.text

            if hakib.text != '':
                colors[5] = hakib.text

            if hakik.text != '':
                colors[6] = hakik.text

            if item.text != '':
                colors[7] = item.text

            if bonus.text != '':
                colors[8] = bonus.text

            if total.text != '':
                colors[9] = total.text

            if clas.text != '':
                colors[10] = clas.text

            self.AttLista()

    def AttLista(self):
        self.ids.brutocolor.text = "Bruto: " + colors[0]
        self.ids.racialcolor.text = "Racial: " + colors[1]
        self.ids.edccolor.text = "EDC: " + colors[2]
        self.ids.akumacolor.text = "Akuma: " + colors[3]
        self.ids.armacolor.text = "Arma: " + colors[4]
        self.ids.hakibcolor.text = "Haki Busou: " + colors[5]
        self.ids.hakikcolor.text = "Haki Kunbun: " + colors[6]
        self.ids.itemcolor.text = "Item: " + colors[7]
        self.ids.bonuscolor.text = "Bônus: " + colors[8]
        self.ids.totalcolor.text = "Total: " + colors[9]
        self.ids.classificacaocolor.text = "Classificação: " + colors[10]

class MainScreen(Screen):
    def ModoNormal(self):
        global principal 
        
        self.ids.level.text = f"Level: {lvl}"
        self.ids.experiencia.text = f"Experiência: {dados[0]}"
        self.ids.hp.text = f"HP: {Level.HP(dados[0])}"
        self.ids.sp.text = f"SP: {Level.SP(dados[0])}"

        self.AttBruto()
        self.AttRacial()
        self.AttEDC()
        self.AttAkuma()
        self.AttHaki()
        self.AttCaminho()
        self.AttArma()
        self.AttItens()
        self.AttBonus()
        self.AttTotal()

        self.ids.tagcontrole.text = "Atributos"
        principal = 1

    def ModoProjecao(self):
        global lvlPro
        for i in range(len(dados)):
            dadosPro[i] = dados[i]
        
        lvlPro = Level.level(dadosPro[0])

        for i in range(0,6):
            for j in range(0,10):
                pontosPro[i][j] = pontos[i][j]
                
    def MudarProjecao(self):
        global projecao
        projecao = 1 - projecao

        if projecao == 1:
            avisoProjecao = Popup(title='Projeção',
                        content=Label(text='Olá, como funciona a projeção? Bem, ela serve como uma projeção do futuro do personagem.\n'
                                    'Lembrando: qualquer alteração em formas de Akuma, Itens, ou cores afetará o modo normal.\n'  
                                    'Pois estes independem da experiência do seu personagem.\n'
                                    'É possível modificar o bruto a vontade.\n'
                                    'Porém este não pode ser colocado num valor menor que o bruto do modo normal.\n', halign='center', valign='middle'),
                        size_hint=(None, None), size=(800,300))
            avisoProjecao.open()
            self.ids.tagcontrole.text = "Projeção"
            self.ids.linhacontrole.cols = 3
            self.ids.linhacontrole.remove_widget(self.ids.experiencia)
            self.ids.linhacontrole.remove_widget(self.ids.hp)
            self.ids.linhacontrole.remove_widget(self.ids.sp)

            self.ids.level.text = "Experiência:"
            
            expPro = TextInput(text = f'{dados[0]}', input_filter = 'int')

            expProOK = Button(text = "XP Projeção", on_press = lambda a: self.AttExpPro(expPro))

            self.ids.linhacontrole.add_widget(expPro)
            self.ids.linhacontrole.add_widget(expProOK)

            self.ModoProjecao()
        else:
            self.ids.tagcontrole.text = "Atributos"
            self.ids.linhacontrole.clear_widgets()

            self.ids.linhacontrole.cols = 4

            self.ids.level.text = f"Level: {lvl}"
            self.ids.linhacontrole.add_widget(self.ids.level)
            self.ids.linhacontrole.add_widget(self.ids.experiencia)
            self.ids.linhacontrole.add_widget(self.ids.hp)
            self.ids.linhacontrole.add_widget(self.ids.sp)

            self.ModoNormal()

    def AttExpPro(self, exppro):
        global lvlPro
        if exppro.text == '':
            aux = 0
        else:
            aux = int(exppro.text)

        if aux > 400:
            avisoLvlIns = Popup(title='Nope',
                            content=Label(text='Projeção... mas o teto ainda é 400', halign='center', valign='middle'),
                            size_hint=(None, None), size=(400,200))
            avisoLvlIns.open()
            return

        if aux < dados[0]:
            avisoLvlIns = Popup(title='Nope',
                            content=Label(text='Projeção... sabe, é bom por mais XP do que você tem', halign='center', valign='middle'),
                            size_hint=(None, None), size=(400,200))
            avisoLvlIns.open()
            return
        else:
            dadosPro[0] = aux
            lvlPro = Level.level(dadosPro[0])

        for i in range(0,6):
            pontosPro[i][2] = dadosPro[12+i]*lvlPro
        
        self.manager.get_screen('akuma').ProcessarAkuma()

        if dadosPro[36] == 1:
            pontosPro[0][6] = dadosPro[37]*lvlPro
        elif dadosPro[36] == 2:
            pontosPro[0][6] = dadosPro[37]*lvlPro
            pontosPro[1][6] = dadosPro[38]*lvlPro
            pontosPro[2][6] = dadosPro[39]*lvlPro
       
        self.AttBruto()
        self.AttEDC()
        self.AttArma()
        self.AttAkuma()
        self.AttBonus()
        self.AttTotal()
            
    def QualEDC(self):
        if (lvl < 3 and projecao == 0) or (lvlPro < 3 and projecao == 1):
            self.manager.current = 'basicedc'
        else:
            self.manager.current = 'choiceedc'

    def Akuma(self):
        if dados[18] == 0:
            dados[18] = 8
        
        if dados[18] == 8:
            self.manager.get_screen('akuma').ids.mul8.state = 'down'
            self.manager.get_screen('akuma').ids.mul9.state = 'normal'
        else:
            self.manager.get_screen('akuma').ids.mul9.state = 'down'
            self.manager.get_screen('akuma').ids.mul8.state = 'normal'
        self.manager.get_screen('akuma').AttList()
        self.manager.current = 'akuma'

    def Haki(self):
        global lvl
        global lvlPro
        if (projecao  == 0 and lvl < 4) or (projecao == 1 and lvlPro < 4):
            avisoLvlIns = Popup(title='Nope',
                            content=Label(text='Somente no Level 4 para cima', halign='center', valign='middle'),
                            size_hint=(None, None), size=(400,200))
            avisoLvlIns.open()
            return
        self.manager.get_screen('haki').AttInputB()
        self.manager.get_screen('haki').AttInputK()
        self.manager.get_screen('haki').HakiRei()
        self.manager.current = 'haki'
        
    def Arma(self):
        if projecao == 0:
            self.manager.get_screen('arma').AttInputs(dados[36])
            self.manager.current = 'arma'
        else:
            self.manager.get_screen('arma').AttInputs(dadosPro[36])
            self.manager.current = 'arma'

    def Itens(self):
        self.manager.get_screen('item').AttBaixar()
        self.manager.get_screen('item').AttList()
        self.manager.current = 'item'

    def Colors(self):
        self.manager.get_screen('color').AttLista()
        self.manager.current = 'color'

    def AttBruto(self):
        if projecao == 0:    
            self.ids.danobruto.text = f'{pontos[0][0]}'
            self.ids.acertobruto.text = str(pontos[1][0])
            self.ids.pontariabruto.text = str(pontos[2][0])
            self.ids.esquivabruto.text = str(pontos[3][0])
            self.ids.bloqueiobruto.text = str(pontos[4][0])
            self.ids.resistenciabruto.text = str(pontos[5][0])
            
            self.ids.avisopontos.text = f"Faltam {dados[0] - Atributos.somaBruto(pontos)} pontos para distribuir"
        else:
            self.ids.danobruto.text = str(pontosPro[0][0])
            self.ids.acertobruto.text = str(pontosPro[1][0])
            self.ids.pontariabruto.text = str(pontosPro[2][0])
            self.ids.esquivabruto.text = str(pontosPro[3][0])
            self.ids.bloqueiobruto.text = str(pontosPro[4][0])
            self.ids.resistenciabruto.text = str(pontosPro[5][0])
            
            self.ids.avisopontos.text = f"Faltam {dadosPro[0] - Atributos.somaBruto(pontosPro)} pontos para distribuir"
                    
    def AttRacial(self):
        if projecao == 0:
            self.ids.danoracial.text = str(pontos[0][1])
            self.ids.acertoracial.text = str(pontos[1][1])
            self.ids.pontariaracial.text = str(pontos[2][1])
            self.ids.esquivaracial.text = str(pontos[3][1])
            self.ids.bloqueioracial.text = str(pontos[4][1])
            self.ids.resistenciaracial.text = str(pontos[5][1])
        else:
            self.ids.danoracial.text = str(pontosPro[0][1])
            self.ids.acertoracial.text = str(pontosPro[1][1])
            self.ids.pontariaracial.text = str(pontosPro[2][1])
            self.ids.esquivaracial.text = str(pontosPro[3][1])
            self.ids.bloqueioracial.text = str(pontosPro[4][1])
            self.ids.resistenciaracial.text = str(pontosPro[5][1])
            
    def AttEDC(self):
        if projecao == 0:
            self.ids.danoedc.text = str(pontos[0][2])
            self.ids.acertoedc.text = str(pontos[1][2])
            self.ids.pontariaedc.text = str(pontos[2][2])
            self.ids.esquivaedc.text = str(pontos[3][2])
            self.ids.bloqueioedc.text = str(pontos[4][2])
            self.ids.resistenciaedc.text = str(pontos[5][2])
        else:
            self.ids.danoedc.text = str(pontosPro[0][2])
            self.ids.acertoedc.text = str(pontosPro[1][2])
            self.ids.pontariaedc.text = str(pontosPro[2][2])
            self.ids.esquivaedc.text = str(pontosPro[3][2])
            self.ids.bloqueioedc.text = str(pontosPro[4][2])
            self.ids.resistenciaedc.text = str(pontosPro[5][2])
        
    def AttAkuma(self):
        if projecao == 0:
            self.ids.danoakuma.text = str(pontos[0][3])
            self.ids.acertoakuma.text = str(pontos[1][3])
            self.ids.pontariaakuma.text = str(pontos[2][3])
            self.ids.esquivaakuma.text = str(pontos[3][3])
            self.ids.bloqueioakuma.text = str(pontos[4][3])
            self.ids.resistenciaakuma.text = str(pontos[5][3])
        else:
            self.ids.danoakuma.text = str(pontosPro[0][3])
            self.ids.acertoakuma.text = str(pontosPro[1][3])
            self.ids.pontariaakuma.text = str(pontosPro[2][3])
            self.ids.esquivaakuma.text = str(pontosPro[3][3])
            self.ids.bloqueioakuma.text = str(pontosPro[4][3])
            self.ids.resistenciaakuma.text = str(pontosPro[5][3])

    def AttHaki(self):
        if projecao == 0:
            self.ids.danohaki.text = str(pontos[0][4])
            self.ids.acertohaki.text = str(pontos[1][4])
            self.ids.pontariahaki.text = str(pontos[2][4])
            self.ids.esquivahaki.text = str(pontos[3][4])
            self.ids.bloqueiohaki.text = str(pontos[4][4])
            self.ids.resistenciahaki.text = str(pontos[5][4])
        else:
            self.ids.danohaki.text = str(pontosPro[0][4])
            self.ids.acertohaki.text = str(pontosPro[1][4])
            self.ids.pontariahaki.text = str(pontosPro[2][4])
            self.ids.esquivahaki.text = str(pontosPro[3][4])
            self.ids.bloqueiohaki.text = str(pontosPro[4][4])
            self.ids.resistenciahaki.text = str(pontosPro[5][4])

    def AttCaminho(self):
        if projecao == 0:
            self.ids.danocaminho.text = str(pontos[0][5])
            self.ids.acertocaminho.text = str(pontos[1][5])
            self.ids.pontariacaminho.text = str(pontos[2][5])
            self.ids.esquivacaminho.text = str(pontos[3][5])
            self.ids.bloqueiocaminho.text = str(pontos[4][5])
            self.ids.resistenciacaminho.text = str(pontos[5][5])
        else:
            self.ids.danocaminho.text = str(pontosPro[0][5])
            self.ids.acertocaminho.text = str(pontosPro[1][5])
            self.ids.pontariacaminho.text = str(pontosPro[2][5])
            self.ids.esquivacaminho.text = str(pontosPro[3][5])
            self.ids.bloqueiocaminho.text = str(pontosPro[4][5])
            self.ids.resistenciacaminho.text = str(pontosPro[5][5])
            
    def AttArma(self):
        if projecao == 0:
            self.ids.danoarma.text = str(pontos[0][6])
            self.ids.acertoarma.text = str(pontos[1][6])
            self.ids.pontariaarma.text = str(pontos[2][6])
        else:
            self.ids.danoarma.text = str(pontosPro[0][6])
            self.ids.acertoarma.text = str(pontosPro[1][6])
            self.ids.pontariaarma.text = str(pontosPro[2][6])

    def AttItens(self):
        self.ids.danoitem.text = str(pontos[0][7])
        self.ids.acertoitem.text = str(pontos[1][7])
        self.ids.pontariaitem.text = str(pontos[2][7])
        self.ids.esquivaitem.text = str(pontos[3][7])
        self.ids.bloqueioitem.text = str(pontos[4][7])
        self.ids.resistenciaitem.text = str(pontos[5][7])
    
    def AttBonus(self):
        if projecao == 0:
            pontos[1][8] = Bonus.bonus(pontos[2])
            pontos[2][8] = Bonus.bonus(pontos[1])
            pontos[3][8] = Bonus.bonus(pontos[4])
            pontos[4][8] = Bonus.bonus(pontos[3])
            self.ids.acertobonus.text = str(pontos[1][8])
            self.ids.pontariabonus.text = str(pontos[2][8])
            self.ids.esquivabonus.text = str(pontos[3][8])
            self.ids.bloqueiobonus.text = str(pontos[4][8])
        else:
            pontosPro[1][8] = Bonus.bonus(pontosPro[2])
            pontosPro[2][8] = Bonus.bonus(pontosPro[1])
            pontosPro[3][8] = Bonus.bonus(pontosPro[4])
            pontosPro[4][8] = Bonus.bonus(pontosPro[3])
            self.ids.acertobonus.text = str(pontosPro[1][8])
            self.ids.pontariabonus.text = str(pontosPro[2][8])
            self.ids.esquivabonus.text = str(pontosPro[3][8])
            self.ids.bloqueiobonus.text = str(pontosPro[4][8])

    def AttTotal(self):
        if projecao == 0:    
            pontos[0][9] = Atributos.soma(pontos[0],0)
            pontos[1][9] = Atributos.soma(pontos[1],1)
            pontos[2][9] = Atributos.soma(pontos[2],1)
            pontos[3][9] = Atributos.soma(pontos[3],1)
            pontos[4][9] = Atributos.soma(pontos[4],1)
            pontos[5][9] = Atributos.soma(pontos[5],0)
            self.ids.danototal.text = str(pontos[0][9])
            self.ids.acertototal.text = str(pontos[1][9])
            self.ids.pontariatotal.text = str(pontos[2][9])
            self.ids.esquivatotal.text = str(pontos[3][9])
            self.ids.bloqueiototal.text = str(pontos[4][9])
            self.ids.resistenciatotal.text = str(pontos[5][9])
            self.ids.danograduacao.text = Graduacao.classificacao(pontos[0][9])
            self.ids.acertograduacao.text = Graduacao.classificacao(pontos[1][9])
            self.ids.pontariagraduacao.text = Graduacao.classificacao(pontos[2][9])
            self.ids.esquivagraduacao.text = Graduacao.classificacao(pontos[3][9])
            self.ids.bloqueiograduacao.text = Graduacao.classificacao(pontos[4][9])
            self.ids.resistenciagraduacao.text = Graduacao.classificacao(pontos[5][9])
        else:
            pontosPro[0][9] = Atributos.soma(pontosPro[0],0)
            pontosPro[1][9] = Atributos.soma(pontosPro[1],1)
            pontosPro[2][9] = Atributos.soma(pontosPro[2],1)
            pontosPro[3][9] = Atributos.soma(pontosPro[3],1)
            pontosPro[4][9] = Atributos.soma(pontosPro[4],1)
            pontosPro[5][9] = Atributos.soma(pontosPro[5],0)
            self.ids.danototal.text = str(pontosPro[0][9])
            self.ids.acertototal.text = str(pontosPro[1][9])
            self.ids.pontariatotal.text = str(pontosPro[2][9])
            self.ids.esquivatotal.text = str(pontosPro[3][9])
            self.ids.bloqueiototal.text = str(pontosPro[4][9])
            self.ids.resistenciatotal.text = str(pontosPro[5][9])
            self.ids.danograduacao.text = Graduacao.classificacao(pontosPro[0][9])
            self.ids.acertograduacao.text = Graduacao.classificacao(pontosPro[1][9])
            self.ids.pontariagraduacao.text = Graduacao.classificacao(pontosPro[2][9])
            self.ids.esquivagraduacao.text = Graduacao.classificacao(pontosPro[3][9])
            self.ids.bloqueiograduacao.text = Graduacao.classificacao(pontosPro[4][9])
            self.ids.resistenciagraduacao.text = Graduacao.classificacao(pontosPro[5][9])
            
    def Add(self, num, valor):
        if (projecao == 0 and dados[0] - (Atributos.somaBruto(pontos) + valor) < 0) or (projecao == 1 and dadosPro[0] - (Atributos.somaBruto(pontosPro) + valor) < 0):
            avisoTooMuch = Popup(title='Too Much',
                            content=Label(text='Infelizmente você não tem tantos pontos assim para distribuir\nTente outra coisa', halign='center', valign='middle'),
                            size_hint=(None, None), size=(450,200))
            avisoTooMuch.open()
            return
        else:
            if projecao == 0:
                pontos[num][0] = pontos[num][0] + valor
            else:
                pontosPro[num][0] = pontosPro[num][0] + valor
            if num == 1 or num == 2 or num == 3 or num == 4:
                self.AttBonus()
            self.AttBruto()
            self.AttTotal()
        
    def Sub(self, num, valor):

        if (projecao == 0 and pontos[num][0] - valor < dados[3+num]) or (projecao == 1 and pontosPro[num][0] - valor < dadosPro[3+num]):
            avisoTooMuch = Popup(title='Too Much',
                            content=Label(text='Você quer retirar mais pontos do que pode.\nSeja porque chegou a 0\nSeja porque chegou ao que a sua já tinha\nTente outra coisa', halign='center', valign='middle'),
                            size_hint=(None, None), size=(400,200))
            avisoTooMuch.open()
            return
        else:
            if projecao == 0:
                pontos[num][0] = pontos[num][0] - valor
            else:
                pontosPro[num][0] = pontosPro[num][0] - valor
                
            if num == 1 or num == 2 or num == 3 or num == 4:
                self.AttBonus()
            self.AttBruto()
            self.AttTotal()
        
    def BaixarDados(self):        
        if self.ids.inputberries.text == '':
            dados[1] = '0'
            dadosPro[1] = '0'
        else:
            dados[1] = self.ids.inputberries.text
            dadosPro[1] = self.ids.inputberries.text

        if self.ids.inputbanco.text == '':
            dados[2] = '0'
            dadosPro[2] = '0'
        else:
            dados[2] = self.ids.inputbanco.text
            dadosPro[2] = self.ids.inputbanco.text

        # Auxiliar para baixar os pontos
        for i in range(6):
            dados[3+i] = pontos[i][0]
            dadosPro[3+i] = pontosPro[i][0]

        if projecao == 0:
            texto = ExportarDados.codedados(dados,formas,itens,colors)
        else:
            texto = ExportarDados.codedados(dadosPro,formas,itens,colors)
            
        path = filechooser.open_file(title="Escolha/Crie um arquivo para salvar os dados", filters=[("*.txt")])
        if path == []:
            avisoPath = Popup(title='Path Not Found',
                        content=Label(text='Tem certeza que selecionou algo?', halign='center', valign='middle'),
                        size_hint=(None, None), size=(400,200))
            avisoPath.open()
            return

        arquivo = open(path[0], "w")
        arquivo.write(texto)
        arquivo.close()
        avisoBaixado = Popup(title='Dados Baixados',
                        content=Label(text='Dados baixados com sucesso', halign='center', valign='middle'),
                        size_hint=(None, None), size=(400,200))
        avisoBaixado.open()

    def BaixarAtributos(self):
        if projecao == 0:
            texto = ExportarDados.codeatributos(lvl,dados,pontos,formas,itens,colors)
        else:
            texto = ExportarDados.codeatributos(lvlPro,dadosPro,pontosPro,formas,itens,colors)
        
        path = filechooser.open_file(title="Escolha/Crie um arquivo para salvar os dados", filters=[("*.txt")])
        if path == []:
            avisoPath = Popup(title='Path Not Found',
                        content=Label(text='Tem certeza que selecionou algo?', halign='center', valign='middle'),
                        size_hint=(None, None), size=(400,200))
            avisoPath.open()
            return

        arquivo = open(path[0], "w")
        arquivo.write(texto)
        arquivo.close()
        avisoBaixado = Popup(title='Atributos Baixados',
                        content=Label(text='Atributos baixados com sucesso', halign='center', valign='middle'),
                        size_hint=(None, None), size=(400,200))
        avisoBaixado.open()

class FichaApp(App):

    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(StartScreen(name='start'))
        sm.add_widget(InputXPScreen(name='inputxp'))
        sm.add_widget(AttXPScreen(name='attxp'))
        sm.add_widget(RacaScreen(name='raca'))
        sm.add_widget(BasicEDCScreen(name='basicedc'))
        sm.add_widget(ChoiceEDCScreen(name='choiceedc'))
        sm.add_widget(ModifiedEDC(name='modifiededc'))
        sm.add_widget(AkumaScreen(name='akuma'))
        sm.add_widget(GunScreen(name='arma'))
        sm.add_widget(MainScreen(name='mainscreen'))
        sm.add_widget(HakiScreen(name='haki'))
        sm.add_widget(CaminhoScreen(name='caminho'))
        sm.add_widget(ItemScreen(name='item'))
        sm.add_widget(ColorScreen(name='color'))
        return sm
    
if __name__ == '__main__':
    FichaApp().run()