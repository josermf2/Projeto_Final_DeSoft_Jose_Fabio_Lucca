"""Foxer"""
#Importando bibliotecas
import os
import sys
import pygame
import random


pygame.init() #Iniciando Pygame

#Cores
BRANCO = (255, 255, 255)
CINZA = (127, 127, 127)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
AMARELO = (255, 255, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

#Icone e nome
icone = pygame.image.load(os.path.join("Imagens", "Icone.png"))
pygame.display.set_icon(icone) 
pygame.display.set_caption("Foxer")

#Criando Tela
tela = pygame.display.set_mode((1200, 700))

#Imagens das telas
telainicial1 = pygame.image.load(os.path.join("Imagens", "Fundo_tela_inicial.png"))



#Criando telas
cenario1 = pygame.image.load(os.path.join("Imagens", "opabeleza.png")).convert()
#cenario2 = pygame.image.load(os.path.join("Imagens", "Cenario_2.png")).convert()


"""Classes"""
'''
class Raposa():

class Skate():

class RacingCar(): 

class Busao():

class Caminhao():
class Car1():
    def __init__(self):
        self.carro = True
carro_pronto = Car1()


class Car2():
'''

"""Testes objetos"""
lista1 = ['RacingCar.png', 'Busão.png']
lista2 = [True,False]
class Rua:
    def __init__(self,posicao):
        self.tem_ou_nao = random.choice(lista2)
        self.posicao_x = posicao[0]
        self.posicao_y = posicao[1]

class Automoveis():
    def __init__(self,c):
        self.posicaox = c[0]
        self.posicaoy = c[1]
    def sobe_carro(self):
        self.posicaoy -=10
    def desce_carro(self):
        self.posicaoy += 10


car1img = pygame.image.load(os.path.join("Imagens",'Car1.png')).convert_alpha()
busaoimg = pygame.image.load(os.path.join("Imagens",'Busão.png')).convert_alpha()
racingcarimg = pygame.image.load(os.path.join("Imagens",'RacingCar.png')).convert_alpha()


relogio = pygame.time.Clock()
i1 = [944,540]
i2 = [816,0]
i3 = [560,540]
i4 = [432, 0]
i5 = [304, 540]
i6 = [176, 0]

car1_pronto = Automoveis(i1)
busao1_pronto = Automoveis(i1)
racingcar1_pronto = Automoveis(i1)
car2_pronto = Automoveis(i2)
busao2_pronto = Automoveis(i2)
racingcar2_pronto = Automoveis(i2)
car3_pronto = Automoveis(i3)
busao3_pronto = Automoveis(i3)
racingcar3_pronto = Automoveis(i3)
car4_pronto = Automoveis(i4)
busao4_pronto = Automoveis(i4)
racingcar4_pronto = Automoveis(i4)
car5_pronto = Automoveis(i5)
busao5_pronto = Automoveis(i5)
racingcar5_pronto = Automoveis(i5)
car6_pronto = Automoveis(i6)
busao6_pronto = Automoveis(i6)
racingcar6_pronto = Automoveis(i6)

lista0 = [car1_pronto,busao1_pronto,racingcar1_pronto]
lista8 = [car3_pronto,busao3_pronto,racingcar3_pronto]


"""Game Loop"""
#Loop para rodar o jogo
rodando = True

while rodando:
    
    deltat = relogio.tick(30)
    print(deltat)
    tela.fill(PRETO)
    tela.blit(cenario1, (0,0))

    

    #Eventos do jogo
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE): 
            rodando = False
            sys.exit()
    d = random.choice(lista0)
    if d == car1_pronto:
        tela.blit(car1img, (d.posicaox,d.posicaoy))
        d.sobe_carro()
        
    
    if d == busao1_pronto:
        tela.blit(busaoimg, (d.posicaox,d.posicaoy))
        d.sobe_carro()
    
    else:
        tela.blit(racingcarimg, (d.posicaox,d.posicaoy))
        d.sobe_carro()

    g = random.choice(lista8)
    if g == car3_pronto:
        tela.blit(car1img, (g.posicaox,g.posicaoy))
        g.sobe_carro()
    
    if g == busao3_pronto:
        tela.blit(busaoimg, (g.posicaox,g.posicaoy))
        g.sobe_carro()
    
    else:
        tela.blit(racingcarimg, (g.posicaox,g.posicaoy))
        g.sobe_carro()
    
    #xrua2 = 816
    #yrua2 += 10
    #tela.blit(rua2, (xrua2, yrua2))
    

    pygame.display.update() #atualizando a tela
    
    relogio.tick(60)

