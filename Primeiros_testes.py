"""Foxer"""
#Importando bibliotecas
import os
import sys
import pygame
from pygame import mixer
import random
import math
import numpy as np

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
tela = pygame.display.set_mode((1200, 644))

#Imagens das telas
telainicial1 = pygame.image.load(os.path.join("Imagens", "Tela_inicial_final.png"))
telafinal = pygame.image.load(os.path.join("Imagens", "Tela_final1.png"))



#Criando telas
cenario1 = pygame.image.load(os.path.join("Imagens", "Foxercenariofinal.png")).convert()
#cenario2 = pygame.image.load(os.path.join("Imagens", "Cenario_2.png")).convert()


"""Classes"""
class Raposa():
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

class Frutas:
    def __init__(self,posicao):
        self.posicaox = posicao[0]
        self.posicaoy = posicao[1]

def colisao(lista1,lista2):
    distancia = math.sqrt((lista1[0]-lista2[0])**2 + (lista1[1]-lista2[1])**2)

    if distancia <= 74:
        return True
    else:
        return False

score = 0
myfont = pygame.font.SysFont('SuperMario256',90)

automoveis_baixo_cima = ['car1', 'busao', 'racingcar', 'car2', 'caminhão']
automoveis_cima_baixo = ['car1invertido', 'busaoinvertido', 'racingcarinvertido', 'car2invertido','caminhãoinvertido']
i1 = [944,838]
i2 = [816,-128]
i3 = [560,838]
i4 = [432, -128]
i5 = [304, 838]
i6 = [176, -128]

class Automoveis:
    def __init__(self, rua,velocidade):
        self.velocidade = velocidade
        self.rua = rua
        if  self.rua == 1:
            self.posicaox = i1[0]
            self.posicaoy = i1[1]
    
        elif self.rua == 2:
            self.posicaox = i2[0]
            self.posicaoy = i2[1]
            
        elif self.rua == 3:
            self.posicaox = i3[0]
            self.posicaoy = i3[1]
                
        elif self.rua == 4:
            self.posicaox = i4[0]
            self.posicaoy = i4[1]
                
        elif self.rua == 5:
            self.posicaox = i5[0]
            self.posicaoy = i5[1]
                
        elif self.rua == 6:
            self.posicaox = i6[0]
            self.posicaoy = i6[1]    
        if self.rua == 1 or self.rua == 3 or self.rua == 5: 
            sprite = random.choice(automoveis_baixo_cima)
            if sprite == 'car1':
                self.imagem = pygame.image.load(os.path.join("Imagens",'Car1.png')).convert_alpha()
                self.retangulo = pygame.Rect((self.posicaox, self.posicaoy), (128, 170))
            elif sprite == 'busao':
                self.imagem = pygame.image.load(os.path.join("Imagens",'Busão.png')).convert_alpha()
                self.retangulo = pygame.Rect((self.posicaox, self.posicaoy), (128, 212))
            elif sprite == 'racingcar':
                self.imagem = pygame.image.load(os.path.join("Imagens",'RacingCar.png')).convert_alpha()
                self.retangulo = pygame.Rect((self.posicaox, self.posicaoy), (128, 184))
            elif sprite == 'car2':
                self.imagem = pygame.image.load(os.path.join("Imagens",'Car2.png')).convert_alpha()
                self.retangulo = pygame.Rect((self.posicaox, self.posicaoy), (128, 178))
            elif sprite == 'caminhão':
                self.imagem = pygame.image.load(os.path.join("Imagens",'Caminhão.png')).convert_alpha()
                self.retangulo = pygame.Rect((self.posicaox, self.posicaoy), (128, 180))
        elif self.rua == 2 or self.rua == 4 or self.rua == 6: 
            sprite = random.choice(automoveis_cima_baixo)
            if sprite == 'car1invertido':
                self.imagem = pygame.image.load(os.path.join("Imagens",'Car1_1.png')).convert_alpha()
                self.retangulo = pygame.Rect((self.posicaox, self.posicaoy), (128, 170))
            elif sprite == 'busaoinvertido':
                self.imagem = pygame.image.load(os.path.join("Imagens",'Busão2.png')).convert_alpha()
                self.retangulo = pygame.Rect((self.posicaox, self.posicaoy), (128, 212))
            elif sprite == 'racingcarinvertido':
                self.imagem = pygame.image.load(os.path.join("Imagens",'RacingCar2.png')).convert_alpha()
                self.retangulo = pygame.Rect((self.posicaox, self.posicaoy), (128, 184))
            elif sprite == 'car2invertido':
                self.imagem = pygame.image.load(os.path.join("Imagens",'Car2_1.png')).convert_alpha()
                self.retangulo = pygame.Rect((self.posicaox, self.posicaoy), (128, 178))
            elif sprite == 'caminhãoinvertido':
                self.imagem = pygame.image.load(os.path.join("Imagens",'Caminhão2.png')).convert_alpha()
                self.retangulo = pygame.Rect((self.posicaox, self.posicaoy), (128, 180))   
    
    def movimentacao(self):
        if self.rua == 1 or self.rua == 3 or self.rua == 5: 
            self.posicaoy -= self.velocidade
            self.retangulo.top = self.posicaoy 
        elif self.rua == 2 or self.rua == 4 or self.rua == 6: 
            self.posicaoy += self.velocidade
            self.retangulo.top = self.posicaoy 


class Rua1:
    def __init__(self,velocidade):
        self.velocidade = velocidade
        self.carro = Automoveis(1,velocidade)
        self.carro.movimentacao()

class Rua2:
    def __init__(self,velocidade): 
        self.velocidade = velocidade
        self.carro = Automoveis(2,velocidade)
        self.carro.movimentacao()

class Rua3:
    def __init__(self,velocidade): 
        self.velocidade = velocidade
        self.carro = Automoveis(3,velocidade)
        self.carro.movimentacao()

class Rua4:
    def __init__(self,velocidade): 
        self.velocidade = velocidade
        self.carro = Automoveis(4,velocidade)
        self.carro.movimentacao() 

class Rua5:
    def __init__(self,velocidade): 
        self.velocidade = velocidade
        self.carro = Automoveis(5,velocidade)
        self.carro.movimentacao()

class Rua6:
    def __init__(self,velocidade): 
        self.velocidade = velocidade
        self.carro = Automoveis(6,velocidade)
        self.carro.movimentacao()   



raposaimg = pygame.image.load(os.path.join('Imagens','Raposa_1.png')).convert_alpha()
abacaxiimg = pygame.image.load(os.path.join('Imagens','Abacaxi64.png')).convert_alpha()
raposa2img = pygame.image.load(os.path.join('Imagens','Raposa_11.png')).convert_alpha()
raposa3img = pygame.image.load(os.path.join('Imagens','Raposa_2.png')).convert_alpha()
raposa4img = pygame.image.load(os.path.join('Imagens','Raposa_3.png')).convert_alpha()
vidaimg = pygame.image.load(os.path.join('Imagens','vida.png')).convert_alpha()


relogio = pygame.time.Clock()

velocidade = [2,3]
lista_abacaxix = np.arange(80,1216,128)
lista_abacaxiy = np.arange(34,650,128)
lista_abacaxi = []
v = 4

for i in lista_abacaxix:
    for u in lista_abacaxiy:
        lista_abacaxi.append([i,u])


del lista_abacaxi[0]
del lista_abacaxi[4]
del lista_abacaxi[12]
del lista_abacaxi[12]
del lista_abacaxi[20]
del lista_abacaxi[25]
del lista_abacaxi[33]
del lista_abacaxi[33]

raposa_objeto = Raposa([1072,258])
abacaxi_objeto = Frutas(random.choice(lista_abacaxi))
j = True

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
telainicial = True


#Sons
def abacaxi_sound():
    mixer.init()
    abacaxi = mixer.Sound(os.path.join('Musicas e Efeitos Sonoros','abacaxi.ogg'))
    abacaxi.play()


mixer.init()
mixer.music.load(os.path.join('Musicas e Efeitos Sonoros','musica_de_fundo.mp3'))
mixer.music.set_volume(0.2)
mixer.music.play(-1)


def colisao_sound():
    mixer.init()
    colisao = mixer.Sound(os.path.join('Musicas e Efeitos Sonoros','colisao.ogg'))
    colisao.play()

def enter_sound():
    mixer.init()
    enter = mixer.Sound(os.path.join('Musicas e Efeitos Sonoros','enter.ogg'))
    enter.play()




"""Game Loop"""
#Loop para rodar o jogo
Foxer = True
while Foxer:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE): 
            Foxer = False
            sys.exit()

    telainicial = True
    while telainicial:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE): 
                Foxer = False
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN or evento.key == pygame.K_KP_ENTER:

                    enter_sound()
                    abacaxi_objeto = Frutas(random.choice(lista_abacaxi)) 
                    score = 0
                    v = 5
                    velocidade = [3,4]
                    raposa_objeto.posicaox = 1072
                    raposa_objeto.posicaoy = 258
                    raposa_objeto.retangulo.left = 1072
                    raposa_objeto.retangulo.top = 258
                    vida = 3
                    Timer = True
                    telainicial = False
        tela.fill(PRETO)
        tela.blit(telainicial1, (0,0))
        pygame.display.update() #atualizando a tela

    
    jogo = True
    while jogo:
        deltat = relogio.tick(60)
        tela.fill(PRETO)
        tela.blit(cenario1, (0,0))
        textsurface = myfont.render(str(score), False, PRETO)
        tela.blit(textsurface,(70,60))
        tela.blit(abacaxiimg, (abacaxi_objeto.posicaox,abacaxi_objeto.posicaoy))


        if j == True and raposa_objeto.posicaox != 48:
            tela.blit(raposaimg, (raposa_objeto.posicaox,raposa_objeto.posicaoy))
        elif j == False and raposa_objeto.posicaox == 1072:
            tela.blit(raposaimg, (raposa_objeto.posicaox,raposa_objeto.posicaoy))
        else:
            tela.blit(raposa2img, (raposa_objeto.posicaox,raposa_objeto.posicaoy))

        
        
        #Eventos do jogo
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE): 
                Foxer = False
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    raposa_objeto.sobe_raposa()
                    if raposa_objeto.posicaox == 48 and raposa_objeto.posicaoy == 2:
                        raposa_objeto.desce_raposa()
                    else:
                        pass
                if evento.key == pygame.K_DOWN:
                    raposa_objeto.desce_raposa()                
                if evento.key == pygame.K_RIGHT:
                    raposa_objeto.direita()
                    j = False
                if evento.key == pygame.K_LEFT:
                    raposa_objeto.esquerda()
                    if raposa_objeto.posicaox == 48 and raposa_objeto.posicaoy == 2:
                        raposa_objeto.direita()
                    else:
                        pass                
                    j = True

        if vida == 3:
            tela.blit(vidaimg, (1085, 15))
            tela.blit(vidaimg, (1120, 15))
            tela.blit(vidaimg, (1155, 15))
        elif vida == 2:
            raposa_objeto.posicaox = 1072
            raposa_objeto.posicaoy = 258
            raposa_objeto.retangulo.left = 1072
            raposa_objeto.retangulo.top = 258
            vida += 0.10
        elif vida == 2.1:
            tela.blit(vidaimg, (1120, 15))
            tela.blit(vidaimg, (1155, 15))
        elif vida == 1.1:
            raposa_objeto.posicaox = 1072
            raposa_objeto.posicaoy = 258
            raposa_objeto.retangulo.left = 1072
            vida += 0.10            
        elif vida >= 1.2 and vida <=1.3:
            tela.blit(vidaimg, (1155, 15))

        if colisao([raposa_objeto.posicaox,raposa_objeto.posicaoy], [abacaxi_objeto.posicaox,abacaxi_objeto.posicaoy]) == True:
            abacaxi_sound()
            score += 1
            if score%2 == 0 and score != 0 and velocidade[-1] < 12:
                    velocidade.append(v)
                    v += 0.1
            o = random.choice(lista_abacaxi)
            abacaxi_objeto.posicaox = o[0]
            abacaxi_objeto.posicaoy = o[1]

        
        if a1.posicaoy < -129:        
            a1.posicaoy = 838 
            obj1 = Rua1(random.choice(velocidade))
            a1 = obj1.carro
        else:
            a1.movimentacao()

        if a2.posicaoy > 829:
            a2.posicaoy = -138 
            obj2 = Rua2(random.choice(velocidade))
            a2 = obj2.carro
        else:
            a2.movimentacao()

        if a3.posicaoy < -129:
            a3.posicaoy = 838 
            obj3 = Rua3(random.choice(velocidade))
            a3 = obj3.carro
        else:
            a3.movimentacao()

        if a4.posicaoy > 829:
            a4.posicaoy = -138 
            obj4 = Rua4(random.choice(velocidade))
            a4 = obj4.carro
        else:
            a4.movimentacao()

        if a5.posicaoy < -129:
            a5.posicaoy = 838 
            obj5 = Rua5(random.choice(velocidade))
            a5 = obj5.carro
        else:
            a5.movimentacao()

        if a6.posicaoy > 829:
            a6.posicaoy = -138 
            obj6 = Rua6(random.choice(velocidade))
            a6 = obj6.carro
        else:
            a6.movimentacao()
            
        tela.blit(a1.imagem, (a1.posicaox, a1.posicaoy))
        tela.blit(a2.imagem, (a2.posicaox, a2.posicaoy))
        tela.blit(a3.imagem, (a3.posicaox, a3.posicaoy))
        tela.blit(a4.imagem, (a4.posicaox, a4.posicaoy))
        tela.blit(a5.imagem, (a5.posicaox, a5.posicaoy))
        tela.blit(a6.imagem, (a6.posicaox, a6.posicaoy))
        
        if raposa_objeto.posicaox > 1072:
            raposa_objeto.posicaox = 1072
        elif raposa_objeto.posicaoy > 516:
            raposa_objeto.posicaoy = 514
        elif raposa_objeto.posicaox < 48:
            raposa_objeto.posicaox = 48 
        elif raposa_objeto.posicaoy < 0:
            raposa_objeto.posicaoy = 2

        if raposa_objeto.retangulo.colliderect(a1.retangulo):
            colisao_sound()
            vida -= 1
            if vida <= 0.2:
                jogo = False 
        elif raposa_objeto.retangulo.colliderect(a2.retangulo):
            colisao_sound()
            vida -= 1
            if vida <= 0.2:
                jogo = False 
        elif raposa_objeto.retangulo.colliderect(a3.retangulo):
            colisao_sound()
            vida -= 1
            if vida <= 0.2:
                jogo = False 
        elif raposa_objeto.retangulo.colliderect(a4.retangulo):
            colisao_sound()
            vida -= 1
            if vida <= 0.2:
                jogo = False 
        elif raposa_objeto.retangulo.colliderect(a5.retangulo):
            colisao_sound()
            vida -= 1
            if vida <= 0.2:
                jogo = False 
        elif raposa_objeto.retangulo.colliderect(a6.retangulo):
            colisao_sound()
            vida -= 1
            if vida <= 0.2:
                jogo = False 


        pygame.display.update() #atualizando a tela


    game_over = True
    while game_over:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE): 
                Foxer = False
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN or evento.key == pygame.K_KP_ENTER:
                    enter_sound()
                    abacaxi_objeto = Frutas(random.choice(lista_abacaxi))
                    game_over = False 
        
        tela.fill(PRETO)
        tela.blit(telafinal,(0,0))        
        textsurface = myfont.render(str(score), False, PRETO)
        tela.blit(textsurface, (470,348))  
        pygame.display.update() #atualizando a tela