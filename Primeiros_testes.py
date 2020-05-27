"""Busãozinho mto loko"""
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
icone = pygame.image.load(os.path.join("Imagens", "Busão.png"))
pygame.display.set_icon(icone) 
pygame.display.set_caption("Busãozinho mto loko")

#Criando Tela
tela = pygame.display.set_mode((1200, 700))

#Criando cenarios
cenario1 = pygame.image.load(os.path.join("Imagens", "Cenario_1.png"))
cenario2 = pygame.image.load(os.path.join("Imagens", "Cenario_2.png"))
cenario3 = pygame.image.load(os.path.join("Imagens", "Cenario_3.png"))
cenario4 = pygame.image.load(os.path.join("Imagens", "Cenario_4.png"))
cenario5 = pygame.image.load(os.path.join("Imagens", "Cenario_5.png"))

"""Game Loop"""
#Loop para rodar o jogo
rodando = True

while rodando:
    
    tela.fill(PRETO) #preenchendo tela
    tela.blit(cenario1, (0, 0))

    #Eventos do jogo
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE): 
            rodando = False
            sys.exit()

    pygame.display.update() #atualizando a tela