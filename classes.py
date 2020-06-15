import pygame
import random
import os

"""Classes"""
#Criando a classe da raposa
class Raposa:
    def __init__(self,posicao):
        self.posicaox = posicao[0]
        self.posicaoy = posicao[1]
        self.retangulo = pygame.Rect((self.posicaox, self.posicaoy), (128,128))
    def sobe_raposa(self):
        self.posicaoy -= 128
        self.retangulo.top = self.posicaoy     
    def desce_raposa(self):
        self.posicaoy += 128
        self.retangulo.top = self.posicaoy 
    def direita(self):
        self.posicaox += 128
        self.retangulo.left = self.posicaox 
    def esquerda(self):
        self.posicaox -= 128
        self.retangulo.left = self.posicaox 

#Criando a classe do abacaxi
class Frutas:
    def __init__(self,posicao):
        self.posicaox = posicao[0]
        self.posicaoy = posicao[1]

