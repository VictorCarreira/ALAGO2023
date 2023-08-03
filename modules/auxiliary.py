import os
import sys
import numpy as np
import pandas as pd
import random


#--------------------------------#
#          Rescale               #
#--------------------------------#


def d2ln(x):
    '''
    Retorna lista ou array na base log natural. 
    Input:
    x, lista ou array na base decimal
    Output:
    y, lista ou array em base log natural 
    '''
    y = np.log(x)

    return y


#-------------------------------#
#         Debuger               #
#-------------------------------#

def pause():
    '''
    FORTRANIC logical debugging.
    Just for fortranic beings.
    '''
    programPause = input("Press the <ENTER> key to continue...")
    return

def stop():
    '''
    FORTRANIC logical debugging.
    Just for fortranic beings.
    '''
    sys.exit('Stop here!')
    return

#-------------------------------#
# Gerador de dados aleatórios   #
#-------------------------------#

def generate_data(distribution, size):
    '''
    Geração de dados aleatórios sintéticos com várias distribuições.
    Argumentos:
       distribution {str} -- Tipo de distribuição dos dados desejada.
       size {int} -- Tamanho da amostra de dados aleatórios.
    Retorna:
       data {array} -- Array contendo a amostra de dados aleatórios gerada.
    '''
    data = None

    #Gerar dados aleatórios com distribuição normal
    if distribution == 'normal':
        data = np.random.normal(size=size)
    #Gerar dados aleatórios com distribuição uniforme
    elif distribution == 'uniforme':
        data = np.random.uniform(size=size)
    #Gerar dados aleatórios com distribuição exponencial
    elif distribution == 'exponencial':
        data = np.random.exponential(size=size)
    #Gerar dados aleatórios com distribuição Poisson
    elif distribution == 'poisson':
        data = np.random.poisson(size=size)
    #Gerar dados aleatórios com distribuição binomial
    elif distribution == 'binomial':
        data = np.random.binomial(n=1000, p=0.5, size=size)


    return data

def dados_aleatorios(n, distribuicao, semente):
    '''
    Geração de dados aleatórios sintéticos com várias distribuições. E
    com controle do sorteio de números aleatórios através de uma semente fixa. 
    Argumentos:
       distribuicao {str} -- Tipo de distribuição dos dados desejada.
       n {int} -- Tamanho da amostra de dados aleatórios.
       semente {int} -- semente do sorteio aleatório
    Retorna:
       data {array} -- Array contendo a amostra de dados aleatórios gerada.
    '''
    #Definimos a semente
    random.seed(semente)
    #Criamos os dados aleatórios usando a distribuição selecionada
    if distribuicao == 'binomial':
        dados = [np.random.binomial(n,0.5) for item in range(n)]
    elif distribuicao == 'poisson':
       dados = [np.random.poisson(5.5) for item in range(n)]
    elif distribuicao == 'normal':
         dados = [random.gauss(0,1) for item in range(n)]
    elif distribuicao == 'exponencial':
         dados = [random.expovariate(2) for item in range(n)]
    elif distribuicao == 'uniforme':
         y = float(input('Indique o valor máximo da variação uniforme:'))
         dados = [np.random.uniform(0.0,y) for item in range(n)]

    return dados

