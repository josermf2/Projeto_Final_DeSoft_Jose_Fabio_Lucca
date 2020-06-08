"""Foxer"""
#Importando bibliotecas
import os
import sys
import pygame
import random
import numpy

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
    if lista1[0] == lista2[0] and lista1[1] == lista2[1]:
        return True
    else:
        return False


automoveis_baixo_cima = [car1, busao, racingcar, car2]
automoveis_cima_baixo = [car1invertido, busaoinvertido, racingcarinvertido, car2invertido]
i1 = [944,838]
i2 = [816,-128]
i3 = [560,838]
i4 = [432, -128]
i5 = [304, 838]
i6 = [176, -128]
class Automoveis:
    def __init__(self):
        self.posicaox = 0
        self.posicaoy = 0
    
    rua = random.randint(1, 6)

    if rua == 1 or rua == 3 or rua == 5: 
        sprite == random.choice(automoveis_baixo_cima)
        if sprite == car1:
            imagem = pygame.image.load(os.path.join("Imagens",'Car1.png')).convert_alpha()
        elif sprite == busao:
            imagem = pygame.image.load(os.path.join("Imagens",'Busão.png')).convert_alpha()
        elif sprite == racingcar:
            imagem = pygame.image.load(os.path.join("Imagens",'RacingCar.png')).convert_alpha()
        elif sprite == car2:
            imagem = pygame.image.load(os.path.join("Imagens",'Car2.png')).convert_alpha()

    elif rua == 2 or rua == 4 or rua == 6: 
        sprite == random.choice(automoveis_cima_baixo)
        if sprite == car1invertido:
            imagem = pygame.image.load(os.path.join("Imagens",'Car1_1.png')).convert_alpha()
        elif sprite == busaoinvertido:
            imagem = pygame.image.load(os.path.join("Imagens",'Busão2.png')).convert_alpha()
        elif sprite == racingcarinvertido:
            imagem = pygame.image.load(os.path.join("Imagens",'RacingCar2.png')).convert_alpha()
        elif sprite == car2invertido:
            imagem = pygame.image.load(os.path.join("Imagens",'Car2_1.png')).convert_alpha()

    if rua == 1:
        self.posicaox = i1[0]
        self.posicaoy = i1[1]
    
    elif rua == 2:
        self.posicaox = i2[0]
        self.posicaoy = i2[1]
            
    elif rua == 3:
        self.posicaox = i3[0]
        self.posicaoy = i3[1]
            
    elif rua == 4:
        self.posicaox = i4[0]
        self.posicaoy = i4[1]
            
    elif rua == 5:
        self.posicaox = i5[0]
        self.posicaoy = i5[1]
            
    elif rua == 6:
        self.posicaox = i6[0]
        self.posicaoy = i6[1]

    def sobe_carro(self):
        self.posicaoy -=10
    def desce_carro(self):
        self.posicaoy += 10


raposaimg = pygame.image.load(os.path.join('Imagens','Raposa_1.png')).convert_alpha()
abacaxiimg =pygame.image.load(os.path.join('Imagens','Abacaxi64.png')).convert_alpha()
raposa2img = pygame.image.load(os.path.join('Imagens','Raposa_11.png')).convert_alpha()
raposa3img = pygame.image.load(os.path.join('Imagens','Raposa_2.png')).convert_alpha()
raposa4img = pygame.image.load(os.path.join('Imagens','Raposa_3.png')).convert_alpha()


relogio = pygame.time.Clock()

'''
car1_pronto = Automoveis(i1)
busao1_pronto = Automoveis(i1)
racingcar1_pronto = Automoveis(i1)
car21_pronto = Automoveis(i1)
car2_pronto = Automoveis(i2)
busao2_pronto = Automoveis(i2)
racingcar2_pronto = Automoveis(i2)
car22_pronto = Automoveis(i1)
car3_pronto = Automoveis(i3)
busao3_pronto = Automoveis(i3)
racingcar3_pronto = Automoveis(i3)
car23_pronto = Automoveis(i1)
car4_pronto = Automoveis(i4)
busao4_pronto = Automoveis(i4)
racingcar4_pronto = Automoveis(i4)
car24_pronto = Automoveis(i1)
car5_pronto = Automoveis(i5)
busao5_pronto = Automoveis(i5)
racingcar5_pronto = Automoveis(i5)
car25_pronto = Automoveis(i1)
car6_pronto = Automoveis(i6)
busao6_pronto = Automoveis(i6)
racingcar6_pronto = Automoveis(i6)
car26_pronto = Automoveis(i1)
'''

lista_objetos_rua1 = [car1_pronto,busao1_pronto,racingcar1_pronto]
lista_objetos_rua2 = [car2_pronto,busao2_pronto,racingcar2_pronto]
lista_objetos_rua3 = [car3_pronto,busao3_pronto,racingcar3_pronto]
lista_objetos_rua4 = [car4_pronto,busao4_pronto,racingcar4_pronto]
lista_objetos_rua5 = [car5_pronto,busao5_pronto,racingcar5_pronto]
lista_objetos_rua6 = [car6_pronto,busao6_pronto,racingcar6_pronto]
lista_abacaxix = numpy.arange(112,1216,128)
lista_abacaxiy = numpy.arange(64,764,128)
lista_abacaxi = []

for i in lista_abacaxix:
    for u in lista_abacaxiy:
        lista_abacaxi.append([i,u])




'''def Rua1():
    d = random.choice(lista0)
    if d == car1_pronto:
        return tela.blit(car1img, (d.posicaox,d.posicaoy)), d.sobe_carro()
        
    
    if d == busao1_pronto:
        return tela.blit(busaoimg, (d.posicaox,d.posicaoy)), d.sobe_carro()
    
    else:
        return tela.blit(racingcarimg, (d.posicaox,d.posicaoy)), d.sobe_carro()'''

score = 0
raposa_objeto = Raposa([1072,286])
abacaxi_objeto = Frutas([1088,636-64])
j = True

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
    
    colisao_abacaxi = colisao([raposa_objeto.posicaox,raposa_objeto.posicaoy], [abacaxi_objeto.posicaox,abacaxi_objeto.posicaoy])
    if colisao_abacaxi == True:
        score += 1
        abacaxi_objeto = Frutas(random.choice(lista_abacaxi))
        tela.blit(abacaxiimg, (abacaxi_objeto.posicaox,abacaxi_objeto.posicaoy))  

    else:
        tela.blit(abacaxiimg, (abacaxi_objeto.posicaox,abacaxi_objeto.posicaoy))

    carro = Automoveis()
    tela.blit(carro.imagem, (carro.posicaox, carro.posicaoy))
    '''
    #Rua 1
    rua1 = random.choice(lista_objetos_rua1)
    if rua1 == car1_pronto:
        tela.blit(car1img, (rua1.posicaox,rua1.posicaoy))
        rua1.sobe_carro()
    
    elif rua1 == busao1_pronto:
        tela.blit(busaoimg, (rua1.posicaox,rua1.posicaoy))
        rua1.sobe_carro()

    elif rua1 == car21_pronto:
        tela.blit(car2img, (rua1.posicaox,rua1.posicaoy))
        rua1.sobe_carro()
    
    else:
        tela.blit(racingcarimg, (rua1.posicaox,rua1.posicaoy))
        rua1.sobe_carro()

    #Rua 2
    rua2 = random.choice(lista_objetos_rua2)
    if rua2 == car2_pronto:
        tela.blit(car1_img, (rua2.posicaox,rua2.posicaoy))
        rua2.desce_carro()
    
    elif rua2 == busao2_pronto:
        tela.blit(busao_img, (rua2.posicaox,rua2.posicaoy))
        rua2.desce_carro()
        
    elif rua2 == car22_pronto:
        tela.blit(car2_img, (rua2.posicaox,rua2.posicaoy))
        rua2.desce_carro()
    else:
        tela.blit(racingcar_img, (rua2.posicaox,rua2.posicaoy))
        rua2.desce_carro()

    #Rua 3   
    rua3 = random.choice(lista_objetos_rua3)
    if rua3 == car3_pronto:
        tela.blit(car1img, (rua3.posicaox,rua3.posicaoy))
        rua3.sobe_carro()
    
    elif rua3 == busao3_pronto:
        tela.blit(busaoimg, (rua3.posicaox,rua3.posicaoy))
        rua3.sobe_carro()
        
    elif rua1 == car21_pronto:
        tela.blit(car2img, (rua1.posicaox,rua1.posicaoy))
        rua1.sobe_carro()
    else:
        tela.blit(racingcarimg, (rua3.posicaox,rua3.posicaoy))
        rua3.sobe_carro()
    
    #Rua 4
    rua4 = random.choice(lista_objetos_rua4)
    if rua4 == car4_pronto:
        tela.blit(car1_img, (rua4.posicaox,rua4.posicaoy))
        rua4.desce_carro()
    
    elif rua4 == busao4_pronto:
        tela.blit(busao_img, (rua4.posicaox,rua4.posicaoy))
        rua4.desce_carro()
        
    elif rua4 == car24_pronto:
        tela.blit(car2_img, (rua4.posicaox,rua4.posicaoy))
        rua4.desce_carro()
    else:
        tela.blit(racingcar_img, (rua4.posicaox,rua4.posicaoy))
        rua4.desce_carro()

    #Rua 5
    rua5 = random.choice(lista_objetos_rua5)
    if rua5 == car5_pronto:
        tela.blit(car1img, (rua5.posicaox,rua5.posicaoy))
        rua5.sobe_carro()
    
    elif rua5 == busao5_pronto:
        tela.blit(busaoimg, (rua5.posicaox,rua5.posicaoy))
        rua5.sobe_carro()
        
    elif rua5 == car25_pronto:
        tela.blit(car2img, (rua5.posicaox,rua5.posicaoy))
        rua5.sobe_carro()
    else:
        tela.blit(racingcarimg, (rua5.posicaox,rua5.posicaoy))
        rua5.sobe_carro()

    #Rua 6
    rua6 = random.choice(lista_objetos_rua6)
    if rua6 == car6_pronto:
        tela.blit(car1_img, (rua6.posicaox,rua6.posicaoy))
        rua6.desce_carro()
    
    elif rua6 == busao6_pronto:
        tela.blit(busao_img, (rua6.posicaox,rua6.posicaoy))
        rua6.desce_carro()
        
    elif rua6 == car26_pronto:
        tela.blit(car2_img, (rua6.posicaox,rua6.posicaoy))
        rua6.desce_carro()
    else:
        tela.blit(racingcar_img, (rua6.posicaox,rua6.posicaoy))
        rua6.desce_carro()
    ''' 

    #xrua2 = 816
    #yrua2 += 10
    #tela.blit(rua2, (xrua2, yrua2))
    

    pygame.display.update() #atualizando a tela
    
    relogio.tick(60)

