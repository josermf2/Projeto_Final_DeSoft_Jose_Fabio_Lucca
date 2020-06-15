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

#Criando listas de automóveis
automoveis_baixo_cima = ['car1', 'busao', 'racingcar', 'car2', 'caminhão']
automoveis_cima_baixo = ['car1invertido', 'busaoinvertido', 'racingcarinvertido', 'car2invertido','caminhãoinvertido']

#Criando posições iniciais de cada rua
i1 = [944,838]
i2 = [816,-128]
i3 = [560,838]
i4 = [432, -128]
i5 = [304, 838]
i6 = [176, -128]

#Criando a classe de Automóveis
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
    
    #Criando a função de movimento
    def movimentacao(self):
        if self.rua == 1 or self.rua == 3 or self.rua == 5: 
            self.posicaoy -= self.velocidade
            self.retangulo.top = self.posicaoy 
        elif self.rua == 2 or self.rua == 4 or self.rua == 6: 
            self.posicaoy += self.velocidade
            self.retangulo.top = self.posicaoy 

    #Criando a classe da rua 1
class Rua1:
    def __init__(self,velocidade):
        self.velocidade = velocidade
        self.carro = Automoveis(1, velocidade)
        self.carro.movimentacao()

#Criando a classe da rua 2
class Rua2:
    def __init__(self,velocidade): 
        self.velocidade = velocidade
        self.carro = Automoveis(2, velocidade)
        self.carro.movimentacao()

#Criando a classe da rua 3
class Rua3:
    def __init__(self,velocidade): 
        self.velocidade = velocidade
        self.carro = Automoveis(3, velocidade)
        self.carro.movimentacao()

#Criando a classe da rua 4
class Rua4:
    def __init__(self,velocidade): 
        self.velocidade = velocidade
        self.carro = Automoveis(4, velocidade)
        self.carro.movimentacao() 

#Criando a classe da rua 5
class Rua5:
    def __init__(self,velocidade): 
        self.velocidade = velocidade
        self.carro = Automoveis(5, velocidade)
        self.carro.movimentacao()

#Criando a classe da rua 6
class Rua6:
    def __init__(self,velocidade): 
        self.velocidade = velocidade
        self.carro = Automoveis(6, velocidade)
        self.carro.movimentacao()   