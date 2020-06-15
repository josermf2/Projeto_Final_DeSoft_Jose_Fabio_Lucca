"""Foxer"""
#Importando bibliotecas
import os
import sys
import pygame
from pygame import mixer
import random
import math
import numpy as np
from classes import Raposa, Automoveis, Frutas, Rua1, Rua2, Rua3, Rua4, Rua5, Rua6 

#Iniciando Pygame
pygame.init() 

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
tela = pygame.display.set_mode((1200, 644))

#Criando o placar 
score = 0

#Importando a Fonte
'''Caso a fonte SuperMario256 apresente algum problema, coloque a linha 36 como comentario (#) e tire o # da linha 37'''
fonte = pygame.font.SysFont('SuperMario256', 90)
#fonte = pygame.font.SysFont('Arial', 50) 
 

'''Carregando Imagens'''
#Imagens das telas
telainicial1 = pygame.image.load(os.path.join("Imagens", "Tela_inicial_final.png"))
telacenario = pygame.image.load(os.path.join("Imagens", "Telacenario.png"))
telafinal = pygame.image.load(os.path.join("Imagens", "Tela_final1.png"))

#Imagem do cenário
cenario1 = pygame.image.load(os.path.join("Imagens", "Foxercenariofinal.png")).convert()
cenario2 = pygame.image.load(os.path.join("Imagens", "Foxercenariofinal2.png")).convert()
cenario3 = pygame.image.load(os.path.join("Imagens", "Foxercenariofinal3.png")).convert()

#Imagens da raposa 
raposaimg = pygame.image.load(os.path.join('Imagens','Raposa_1.png')).convert_alpha()
raposa2img = pygame.image.load(os.path.join('Imagens','Raposa_11.png')).convert_alpha()

#Imagem do abacaxi
abacaxiimg = pygame.image.load(os.path.join('Imagens','Abacaxi64.png')).convert_alpha()

#Icone das vidas
vidaimg1 = pygame.image.load(os.path.join('Imagens','vida.png')).convert_alpha()
vidaimg2 = pygame.image.load(os.path.join('Imagens','vida2.png')).convert_alpha()
vidaimg3 = pygame.image.load(os.path.join('Imagens','vida3.png')).convert_alpha()

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

'''Listas'''
#Criando a lista de velocidades 
velocidade = [2,3]
v = 4

#Criando a lista do abacaxi
lista_abacaxix = np.arange(80,1216,128)
lista_abacaxiy = np.arange(34,650,128)
lista_abacaxi_inicial = []

for i in lista_abacaxix:
    for u in lista_abacaxiy:
        lista_abacaxi_inicial.append([i,u])

#Deletando posições críticas do abacaxi
lista_abacaxi = []
abacaxi = True
for i in range (len(lista_abacaxi_inicial)):
    if lista_abacaxi_inicial[i][1] == 34:
        if lista_abacaxi_inicial[i][0] == 80 or lista_abacaxi_inicial[i][0] == 208 or lista_abacaxi_inicial[i][0] == 464 or lista_abacaxi_inicial[i][0] == 848 or lista_abacaxi_inicial[i][0] == 1104:
            pass
        else:
            lista_abacaxi.append(lista_abacaxi_inicial[i])
    elif lista_abacaxi_inicial[i][1] == 546:
        if lista_abacaxi_inicial[i][0] == 336 or lista_abacaxi_inicial[i][0] == 592 or lista_abacaxi_inicial[i][0] == 976:
            pass
        else:
            lista_abacaxi.append(lista_abacaxi_inicial[i])
    else:
        lista_abacaxi.append(lista_abacaxi_inicial[i])

'''Criando objetos'''
#Objeto da Raposa 
raposa_objeto = Raposa([1072,258])

#Objeto Abacaxi
abacaxi_objeto = Frutas(random.choice(lista_abacaxi))

#Objeotos dos carros
obj1 = Rua1(random.choice(velocidade))
a1 = obj1.carro
obj2 = Rua2(random.choice(velocidade))
a2 = obj2.carro
obj3 = Rua3(random.choice(velocidade))
a3 = obj3.carro  
obj4 = Rua4(random.choice(velocidade))
a4 = obj4.carro  
obj5 = Rua5(random.choice(velocidade))
a5 = obj5.carro  
obj6 = Rua6(random.choice(velocidade))
a6 = obj6.carro    


#Criando o relógio do pygame
relogio = pygame.time.Clock()

cenario10 = False
cenario20 = False
cenario30 = False

"""Game Loop"""
#Loop geral
Foxer = True
while Foxer:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE): #evento de quit do jogo
            Foxer = False
            sys.exit()


    #Loop do menu
    telainicial = True
    while telainicial:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE): #evento de quit do jogo
                Foxer = False
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN or evento.key == pygame.K_KP_ENTER: #evento de início do jogo
                    enter_sound()
                    #Resetando parâmetros do jogo
                    abacaxi_objeto = Frutas(random.choice(lista_abacaxi)) 
                    score = 0
                    v = 5
                    velocidade = [3,4]
                    raposa_objeto.posicaox = 1072
                    raposa_objeto.posicaoy = 258
                    raposa_objeto.retangulo.left = 1072
                    raposa_objeto.retangulo.top = 258
                    vida = 3
                    cenario10 = False
                    cenario20 = False
                    cenario30 = False
                    j = True
                    Timer = True
                    telainicial = False
        tela.fill(PRETO)
        tela.blit(telainicial1, (0,0)) #mostrando tela inicial do jogo
        pygame.display.update() #atualizando a tela

    #Loop do menu de cenários
    cenarios = True
    while cenarios:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE): #evento de quit do jogo
                Foxer = False
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1 or evento.key == pygame.K_KP1: #evento para escolher cenário 1
                    enter_sound()
                    cenario10 = True
                    cenarios = False
                elif evento.key == pygame.K_2 or evento.key == pygame.K_KP2: #evento para escolher cenário 2
                    enter_sound()
                    cenario20 = True
                    cenarios = False
                elif evento.key == pygame.K_3 or evento.key == pygame.K_KP3: #evento para escolher cenário 3
                    enter_sound()
                    cenario30 = True
                    cenarios = False    
        tela.fill(PRETO)
        tela.blit(telacenario, (0,0)) #mostrando tela inicial do jogo
        pygame.display.update() #atualizando a tela

    #Loop do jogo
    jogo = True
    while jogo:
        deltat = relogio.tick(60) #definindo a taxa de FPS do jogo
        tela.fill(PRETO)

        #Mostrando o cenário escolhido
        if cenario10 == True:
            tela.blit(cenario1, (0,0))
            vidaimg = vidaimg1
        elif cenario20 == True:
            tela.blit(cenario2, (0,0))
            vidaimg = vidaimg2
        elif cenario30 == True: 
            tela.blit(cenario3, (0,0))
            vidaimg = vidaimg3
           
        textsurface = fonte.render(str(score), False, PRETO)
        tela.blit(textsurface,(70,60)) #mostrando o score do jogador 
        tela.blit(abacaxiimg, (abacaxi_objeto.posicaox,abacaxi_objeto.posicaoy)) #mostrando o abacaxi

        #Mostrando a raposa 
        if j == True and raposa_objeto.posicaox != 48:
            tela.blit(raposaimg, (raposa_objeto.posicaox,raposa_objeto.posicaoy)) 
        elif j == False and raposa_objeto.posicaox == 1072:
            tela.blit(raposaimg, (raposa_objeto.posicaox,raposa_objeto.posicaoy))
        else:
            tela.blit(raposa2img, (raposa_objeto.posicaox,raposa_objeto.posicaoy)) #invertendo a imagem da raposa

        #Eventos do jogo
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE): #evento de quit do jogo
                Foxer = False
                sys.exit()
            if evento.type == pygame.KEYDOWN: #reconhecendo comandos do jogador
                if evento.key == pygame.K_UP: #andando para cima
                    raposa_objeto.sobe_raposa()
                    if raposa_objeto.posicaox == 48 and raposa_objeto.posicaoy == 2:
                        raposa_objeto.desce_raposa()
                    else:
                        pass
                if evento.key == pygame.K_DOWN: #andando para baixo
                    raposa_objeto.desce_raposa()                
                if evento.key == pygame.K_RIGHT: #andando para a direita 
                    raposa_objeto.direita()
                    j = False
                if evento.key == pygame.K_LEFT: #andando para a esquerda
                    raposa_objeto.esquerda()
                    if raposa_objeto.posicaox == 48 and raposa_objeto.posicaoy == 2:
                        raposa_objeto.direita()
                    else:
                        pass                
                    j = True

        #Mostrando número de vidas
        if vida == 3: #3 vidas
            tela.blit(vidaimg, (1085, 15))
            tela.blit(vidaimg, (1120, 15))
            tela.blit(vidaimg, (1155, 15))
        elif vida == 2: #2 vidas
            raposa_objeto.posicaox = 1072
            raposa_objeto.posicaoy = 258
            raposa_objeto.retangulo.left = 1072
            raposa_objeto.retangulo.top = 258
            vida += 0.10
        elif vida == 2.1: 
            tela.blit(vidaimg, (1120, 15))
            tela.blit(vidaimg, (1155, 15))
        elif vida == 1.1: #1 vida
            raposa_objeto.posicaox = 1072
            raposa_objeto.posicaoy = 258
            raposa_objeto.retangulo.left = 1072
            vida += 0.10            
        elif vida >= 1.2 and vida <=1.3: #0 vidas
            tela.blit(vidaimg, (1155, 15))
        #detectando colisão da raposa com o abacaxi
        if colisao([raposa_objeto.posicaox,raposa_objeto.posicaoy], [abacaxi_objeto.posicaox,abacaxi_objeto.posicaoy]) == True:
            abacaxi_sound() #implementando o som da colisão com o abacaxi
            score += 1
            if score%2 == 0 and score != 0 and velocidade[-1] < 12: #adicionando novas velocidades à lista de velocidade
                    velocidade.append(v)
                    v += 0.1
            o = random.choice(lista_abacaxi) #randomizando o surgimento dos abacaxis
            abacaxi_objeto.posicaox = o[0]
            abacaxi_objeto.posicaoy = o[1]

        #criando e movimentando os carros
        if a1.posicaoy < -129: #rua 1  
            a1.posicaoy = 838 
            obj1 = Rua1(random.choice(velocidade))
            a1 = obj1.carro
        else:
            a1.movimentacao()

        if a2.posicaoy > 829: #rua 2
            a2.posicaoy = -138 
            obj2 = Rua2(random.choice(velocidade))
            a2 = obj2.carro
        else:
            a2.movimentacao()

        if a3.posicaoy < -129: #rua 3
            a3.posicaoy = 838 
            obj3 = Rua3(random.choice(velocidade))
            a3 = obj3.carro
        else:
            a3.movimentacao()

        if a4.posicaoy > 829: #rua 4
            a4.posicaoy = -138 
            obj4 = Rua4(random.choice(velocidade))
            a4 = obj4.carro
        else:
            a4.movimentacao()

        if a5.posicaoy < -129: #rua 5
            a5.posicaoy = 838 
            obj5 = Rua5(random.choice(velocidade))
            a5 = obj5.carro
        else:
            a5.movimentacao()

        if a6.posicaoy > 829: #rua 6
            a6.posicaoy = -138 
            obj6 = Rua6(random.choice(velocidade))
            a6 = obj6.carro
        else:
            a6.movimentacao()
        
        #mostrando os carros    
        tela.blit(a1.imagem, (a1.posicaox, a1.posicaoy)) #rua 1
        tela.blit(a2.imagem, (a2.posicaox, a2.posicaoy)) #rua 2
        tela.blit(a3.imagem, (a3.posicaox, a3.posicaoy)) #rua 3
        tela.blit(a4.imagem, (a4.posicaox, a4.posicaoy)) #rua 4
        tela.blit(a5.imagem, (a5.posicaox, a5.posicaoy)) #rua 5
        tela.blit(a6.imagem, (a6.posicaox, a6.posicaoy)) #rua 6
        
        #definindo os limites do cenário
        if raposa_objeto.posicaox > 1072:
            raposa_objeto.posicaox = 1072
        elif raposa_objeto.posicaoy > 516:
            raposa_objeto.posicaoy = 514
        elif raposa_objeto.posicaox < 48:
            raposa_objeto.posicaox = 48 
        elif raposa_objeto.posicaoy < 0:
            raposa_objeto.posicaoy = 2

        #detectando colisão com os carros
        if raposa_objeto.retangulo.colliderect(a1.retangulo):
            colisao_sound() #implementando o som da colisão com os carros
            vida -= 1 #perdendo vida
            if vida <= 0.2:
                jogo = False 
        elif raposa_objeto.retangulo.colliderect(a2.retangulo):
            colisao_sound() #implementando o som da colisão com os carros
            vida -= 1 #perdendo vida
            if vida <= 0.2:
                jogo = False 
        elif raposa_objeto.retangulo.colliderect(a3.retangulo):
            colisao_sound() #implementando o som da colisão com os carros
            vida -= 1 #perdendo vida
            if vida <= 0.2:
                jogo = False 
        elif raposa_objeto.retangulo.colliderect(a4.retangulo):
            colisao_sound() #implementando o som da colisão com os carros
            vida -= 1 #perdendo vida
            if vida <= 0.2:
                jogo = False 
        elif raposa_objeto.retangulo.colliderect(a5.retangulo):
            colisao_sound() #implementando o som da colisão com os carros
            vida -= 1 #perdendo vida
            if vida <= 0.2:
                jogo = False 
        elif raposa_objeto.retangulo.colliderect(a6.retangulo):
            colisao_sound() #implementando o som da colisão com os carros
            vida -= 1 #perdendo vida
            if vida <= 0.2:
                jogo = False 

        pygame.display.update() #atualizando a tela

    #Loop do game over
    game_over = True
    while game_over:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE): #evento de quit do jogo
                Foxer = False
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN or evento.key == pygame.K_KP_ENTER: #evento de restart do jogo
                    enter_sound() #implementando o som do reinício do jogo
                    abacaxi_objeto = Frutas(random.choice(lista_abacaxi))
                    game_over = False 
        
        tela.fill(PRETO)
        tela.blit(telafinal,(0,0))        
        textsurface = fonte.render(str(score), False, PRETO)
        tela.blit(textsurface, (470,348)) #Mostrando o score final do jogo
        pygame.display.update() #atualizando a tela