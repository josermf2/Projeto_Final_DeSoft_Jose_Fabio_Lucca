"""Foxer"""
#Importando bibliotecas
import os
import sys
import pygame

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

<<<<<<< HEAD
#Imagens das telas
telainicial1 = pygame.image.load(os.path.join("Imagens", "Fundo_tela_inicial1.png"))
telainicial2 = pygame.image.load(os.path.join("Imagens", "Fundo_tela_inicial2.png"))
=======
#Criando telas
telainicial = pygame.image.load(os.path.join("Imagens", "Fundo_tela_inicial1.png"))
>>>>>>> 9639ef52e4bacfb6d1b831c3ffa5b7d9f9b55a83
#cenario1 = pygame.image.load(os.path.join("Imagens", "Cenario_1.png"))
cenario2 = pygame.image.load(os.path.join("Imagens", "Cenario_2.png"))
cenario3 = pygame.image.load(os.path.join("Imagens", "Cenario_3.png"))
cenario4 = pygame.image.load(os.path.join("Imagens", "Cenario_4.png"))
cenario5 = pygame.image.load(os.path.join("Imagens", "Cenario_5.png"))

"""Classes"""

class Raposa():
    
    def __init__(self):
        self.raposa = pygame.image.load(os.path.join("Imagens", "Raposa_1.png"))

    
"""
class Skate():

class RacingCar(): 

class Busao():

class Caminhao():

class Car1():

class Car2():
""" 

relogio = pygame.time.Clock()

"""Game Loop"""
#Loop para rodar o jogo
rodando = True

while rodando:
    
    tela.fill(PRETO)
    tela.blit(cenario2, (0,0))

    #Eventos do jogo
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE): 
            rodando = False
            sys.exit()

    relogio.tick(60)

    pygame.display.update() #atualizando a tela
