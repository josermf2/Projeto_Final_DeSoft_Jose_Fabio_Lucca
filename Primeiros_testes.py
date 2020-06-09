"""Foxer"""
#Importando bibliotecas
import os
import sys
import pygame
import random
import math
import numpy as np

# x=90 y=56

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
cenario1 = pygame.image.load(os.path.join("Imagens", "Foxercenariofinal.png")).convert()
#cenario2 = pygame.image.load(os.path.join("Imagens", "Cenario_2.png")).convert()


"""Classes"""
#posicoesx = np.arange(0,1200,128)
#posicoesy = np.arange(0,700,64)
class Raposa():
    def __init__(self,posicao):
        self.posicaox = posicao[0]
        self.posicaoy = posicao[1]
    def sobe_raposa(self):
        self.posicaoy -= 128
    def desce_raposa(self):
        self.posicaoy += 128
    def direita(self):
        self.posicaox += 128
    def esquerda(self):
        self.posicaox -= 128

class Frutas:
    def __init__(self,posicao):
        self.posicaox = posicao[0]
        self.posicaoy = posicao[1]

def colisao(lista1,lista2):
    distancia = math.sqrt((lista1[0]-lista2[0])**2 + (lista1[1]-lista2[1])**2)
    if distancia <= 80:
        return True
    else:
        return False

'''lista_abacaxix = np.arange(112,1328,128)
lista_abacaxiy = np.arange()
'''
automoveis_baixo_cima = ['car1', 'busao', 'racingcar', 'car2']
automoveis_cima_baixo = ['car1invertido', 'busaoinvertido', 'racingcarinvertido', 'car2invertido']
i1 = [944,838]
i2 = [816,-128]
i3 = [560,838]
i4 = [432, -128]
i5 = [304, 838]
i6 = [176, -128]

class Automoveis:
    def __init__(self, rua):
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
            elif sprite == 'busao':
                self.imagem = pygame.image.load(os.path.join("Imagens",'Busão.png')).convert_alpha()
            elif sprite == 'racingcar':
                self.imagem = pygame.image.load(os.path.join("Imagens",'RacingCar.png')).convert_alpha()
            elif sprite == 'car2':
                self.imagem = pygame.image.load(os.path.join("Imagens",'Car2.png')).convert_alpha()
        elif self.rua == 2 or self.rua == 4 or self.rua == 6: 
            sprite = random.choice(automoveis_cima_baixo)
            if sprite == 'car1invertido':
                self.imagem = pygame.image.load(os.path.join("Imagens",'Car1_1.png')).convert_alpha()
            elif sprite == 'busaoinvertido':
                self.imagem = pygame.image.load(os.path.join("Imagens",'Busão2.png')).convert_alpha()
            elif sprite == 'racingcarinvertido':
                self.imagem = pygame.image.load(os.path.join("Imagens",'RacingCar2.png')).convert_alpha()
            elif sprite == 'car2invertido':
                self.imagem = pygame.image.load(os.path.join("Imagens",'Car2_1.png')).convert_alpha()
    
    def movimentacao(self):
        if self.rua == 1 or self.rua == 3 or self.rua == 5: 
            self.posicaoy -= random.randint(9,28)
        elif self.rua == 2 or self.rua == 4 or self.rua == 6: 
            self.posicaoy += random.randint(9,28)


class Rua1:
    def __init__(self):
        self.carro = Automoveis(1)
        self.carro.movimentacao()

class Rua2:
    def __init__(self): 
        self.carro = Automoveis(2)
        self.carro.movimentacao()

class Rua3:
    def __init__(self): 
        self.carro = Automoveis(3)
        self.carro.movimentacao()

class Rua4:
    def __init__(self): 
        self.carro = Automoveis(4)
        self.carro.movimentacao() 

class Rua5:
    def __init__(self): 
        self.carro = Automoveis(5)
        self.carro.movimentacao()

class Rua6:
    def __init__(self): 
        self.carro = Automoveis(6)
        self.carro.movimentacao()   

contador = 0

raposaimg = pygame.image.load(os.path.join('Imagens','Raposa_1.png')).convert_alpha()
abacaxiimg =pygame.image.load(os.path.join('Imagens','Abacaxi64.png')).convert_alpha()
raposa2img = pygame.image.load(os.path.join('Imagens','Raposa_11.png')).convert_alpha()
raposa3img = pygame.image.load(os.path.join('Imagens','Raposa_2.png')).convert_alpha()
raposa4img = pygame.image.load(os.path.join('Imagens','Raposa_3.png')).convert_alpha()


relogio = pygame.time.Clock()


lista_abacaxix = np.arange(112,1216,128)
lista_abacaxiy = np.arange(64,636,1)
lista_abacaxi = []

for i in lista_abacaxix:
    for u in lista_abacaxiy:
        lista_abacaxi.append([i,u])

del lista_abacaxi[0]
score = 0
raposa_objeto = Raposa([1072,286])
abacaxi_objeto = Frutas([1088,636-64])
j = True

obj1 = Rua1()
a1 = obj1.carro
obj2 = Rua2()
a2 = obj2.carro
obj3 = Rua3()
a3 = obj3.carro  
obj4 = Rua4()
a4 = obj4.carro  
obj5 = Rua5()
a5 = obj5.carro  
obj6 = Rua6()
a6 = obj6.carro    

"""Game Loop"""
#Loop para rodar o jogo
rodando = True

while rodando:
    deltat = relogio.tick(30)
    tela.fill(PRETO)
    tela.blit(cenario1, (0,0))

    if j == True:
        tela.blit(raposaimg, (raposa_objeto.posicaox,raposa_objeto.posicaoy))
        tela.blit(raposa3img, (raposa_objeto.posicaox,raposa_objeto.posicaoy))
        tela.blit(raposa4img, (raposa_objeto.posicaox,raposa_objeto.posicaoy))

    else:
        tela.blit(raposa2img, (raposa_objeto.posicaox,raposa_objeto.posicaoy))
    
    #Eventos do jogo
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE): 
            rodando = False
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:
                raposa_objeto.sobe_raposa()
            if evento.key == pygame.K_DOWN:
                raposa_objeto.desce_raposa()                
            if evento.key == pygame.K_RIGHT:
                raposa_objeto.direita()
                j = False
            if evento.key == pygame.K_LEFT:
                raposa_objeto.esquerda()
                j = True
    

    if colisao([raposa_objeto.posicaox,raposa_objeto.posicaoy], [abacaxi_objeto.posicaox,abacaxi_objeto.posicaoy]) == True:
        score += 1
        abacaxi_objeto.posicaox = random.choice(lista_abacaxix)
        abacaxi_objeto.posicaoy = random.choice(lista_abacaxiy)

    tela.blit(abacaxiimg, (abacaxi_objeto.posicaox,abacaxi_objeto.posicaoy))
    
    if a1.posicaoy < -129:
        a1.posicaoy = 838 
        obj1 = Rua1()
        a1 = obj1.carro
    else:
        a1.movimentacao()

    if a2.posicaoy > 829:
        a2.posicaoy = -138 
        obj2 = Rua2()
        a2 = obj2.carro
    else:
        a2.movimentacao()

    if a3.posicaoy < -129:
        a3.posicaoy = 838 
        obj3 = Rua3()
        a3 = obj3.carro
    else:
        a3.movimentacao()

    if a4.posicaoy > 829:
        a4.posicaoy = -138 
        obj4 = Rua4()
        a4 = obj4.carro
    else:
        a4.movimentacao()

    if a5.posicaoy < -129:
        a5.posicaoy = 838 
        obj5 = Rua5()
        a5 = obj5.carro
    else:
        a5.movimentacao()

    if a6.posicaoy > 829:
        a6.posicaoy = -138 
        obj6 = Rua6()
        a6 = obj6.carro
    else:
        a6.movimentacao()

  
    tela.blit(a1.imagem, (a1.posicaox, a1.posicaoy))
    tela.blit(a2.imagem, (a2.posicaox, a2.posicaoy))
    tela.blit(a3.imagem, (a3.posicaox, a3.posicaoy))
    tela.blit(a4.imagem, (a4.posicaox, a4.posicaoy))
    tela.blit(a5.imagem, (a5.posicaox, a5.posicaoy))
    tela.blit(a6.imagem, (a6.posicaox, a6.posicaoy))
    
    '''if contador <= 41:
        obj2 = Rua1()
        a2 = obj2.carro  
        a2.movimentacao()
    else:
        a2.movimentacao()

    print(contador)
    contador +=1
    if contador == 145:
        contador = 0
    else:
        pass
    tela.blit(a2.imagem, (a2.posicaox, a2.posicaoy))'''

    
    pygame.display.update() #atualizando a tela
    
    relogio.tick(60)

