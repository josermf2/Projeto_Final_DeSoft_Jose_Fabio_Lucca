import pygame 
from pygame import mixer
import os
import math 

'''Funções'''
#Criando a colisão do abacaxi
def colisao(lista1,lista2):
    distancia = math.sqrt((lista1[0]-lista2[0])**2 + (lista1[1]-lista2[1])**2)

    if distancia <= 74:
        return True
    else:
        return False

#Criando música de fundo
mixer.init()
mixer.music.load(os.path.join('Musicas e Efeitos Sonoros','musica_de_fundo.mp3'))
mixer.music.set_volume(0.2)
mixer.music.play(-1)

#Criando sons
def abacaxi_sound():
    mixer.init()
    abacaxi = mixer.Sound(os.path.join('Musicas e Efeitos Sonoros','abacaxi.ogg'))
    abacaxi.play()

def colisao_sound():
    mixer.init()
    colisao = mixer.Sound(os.path.join('Musicas e Efeitos Sonoros','colisao.ogg'))
    colisao.play()

def enter_sound():
    mixer.init()
    enter = mixer.Sound(os.path.join('Musicas e Efeitos Sonoros','enter.ogg'))
    enter.play()