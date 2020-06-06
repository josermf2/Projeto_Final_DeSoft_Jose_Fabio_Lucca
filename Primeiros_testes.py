"""Foxer"""
#Importando bibliotecas
import os
import sys
import pygame
import random
import time

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
lista2 = [True,True]
class Rua:
    def __init__(self,posicao):
        self.tem_ou_nao = random.choice(lista2)
        self.posicao_x = posicao[0]
        self.posicao_y = posicao[1]

class Sprite():
    def __init__(self):
        self.automovel = random.choice(lista1)

objeto = Sprite()
rua1 = pygame.image.load(os.path.join("Imagens",objeto.automovel)).convert_alpha()
rua2 = pygame.image.load(os.path.join("Imagens",objeto.automovel)).convert_alpha()

yrua1 = 540

yrua2 = 0


relogio = pygame.time.Clock()

"""Game Loop"""
#Loop para rodar o jogo
rodando = True

while rodando:
    
    deltat = relogio.tick(60)
    tela.fill(PRETO)
    tela.blit(cenario1, (0,0))



    #Eventos do jogo
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE): 
            rodando = False
            sys.exit()

    xrua1 = 944
    yrua1 -= 10
    tela.blit(rua1, (xrua1, yrua1))
    
    xrua2 = 816
    yrua2 += 10
    tela.blit(rua2, (xrua2, yrua2))
    

    pygame.display.update() #atualizando a tela
    
    relogio.tick(60)

