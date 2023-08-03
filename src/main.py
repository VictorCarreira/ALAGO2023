#Pacotes
# -*- coding: utf-8 -*-

#####Programa Fuzzy_lakes#######


import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from skfuzzy import control as ctrl


#Definindo os parâmetros do modelo:
#Deve-se compreender o universo de variáveis divididas em dois grupos e o universo do discurso de cada uma delas
#Antecedentes: compreende os parâmetros de entrada
#Consequentes: compreende os parâmetros de saída
#Lista de antecedentes: produtividade primária, O² dissolvido, taxa de sedimentação, profundidade, granulometria, seleção
#Lista de consequentes: conteúdo orgânico total



#Antecedentes
PP = ctrl.Antecedent(np.arange(0,6000,1), 'Produtividade primária')
O2 = ctrl.Antecedent(np.arange(0,10,0.5), 'Oxigênio dissolvido')
TS = ctrl.Antecedent(np.arange(0,500,0.5), 'Taxa de sedimentação')
Z  = ctrl.Antecedent(np.arange(0,1000,1), 'Profundidade')
GRA = ctrl.Antecedent(np.arange(0,2000,0.002), 'Granulometria')
SEL = ctrl.Antecedent(np.arange(0,200,0.00125),'Seleção')

#Consequentes
COT = ctrl.Consequent(np.arange(0,40,0.1), 'Conteúdo orgânico total')

intervalos=input('Escolha um intervalo automático ou manual: ')

if intervalos == 'automatico':
    #Intervalos numéricos com sete intervalos de classes automáticos: 3, 5 ou 7
    PP.automf(7)
    O2.automf(7)
    TS.automf(7)
    Z.automf(7)
    GRA.automf(7)
    SEL.automf(7)
    COT.automf(7)
    #No caso automático:
    regrabeta1 = ctrl.Rule(PP['poor'] | O2['poor'] | TS['poor'] | Z['poor'] | GRA['poor'] | SEL['poor'], COT['excellent'] )
    regrabeta2= ctrl.Rule(PP['excellent'] & TS['average'] | Z['average'] & GRA['dismal'] & SEL['excellent'], COT['excellent'])

elif intervalos == 'manual':
    #Intervalos manuais da tabela (entradas)
    PP['Muito baixo'] = fuzz.trimf(PP.universe, [0,0,50])  
    PP['Baixo'] = fuzz.trimf(PP.universe, [0,50,300])
    PP['Médio'] = fuzz.trimf(PP.universe, [0,300,600])
    PP['Alto'] = fuzz.trimf(PP.universe, [0,600,1000])
    PP['Muito alto'] = fuzz.trimf(PP.universe, [0,1000,1000])

    O2['Anóxico'] = fuzz.trimf(O2.universe, [0,0.5, 2])
    O2['Misto'] = fuzz.trimf(O2.universe, [0,0,0.5])
    O2['Óxido'] = fuzz.trimf(O2.universe, [0,2,2])

    TS['Muito baixo'] = fuzz.trimf(TS.universe, [0,0,0.9])
    TS['Baixo'] = fuzz.trimf(TS.universe, [0,0.9,2.8])
    TS['Médio'] = fuzz.trimf(TS.universe, [0,2.8,5.7])
    TS['Alto'] = fuzz.trimf(TS.universe, [0,5.7,8])
    TS['Muito alto'] = fuzz.trimf(TS.universe, [0,8,500])

    Z['Raso'] = fuzz.trimf(Z.universe, [0,0,30])
    Z['Médio'] = fuzz.trimf(Z.universe, [0,30,60])
    Z['Profundo'] = fuzz.trimf(Z.universe, [0,60,100])
    Z['Muito profundo'] = fuzz.trimf(Z.universe, [0,100,300])
    Z['Ultra profundo'] = fuzz.trimf(Z.universe, [0,300,1000])

    GRA['Lama'] = fuzz.trimf(GRA.universe, [0,0.002,0.06])
    GRA['Areia fina'] = fuzz.trimf(GRA.universe, [0,0.06,0.2])
    GRA['Areia média'] = fuzz.trimf(GRA.universe, [0,0.2,0.6])
    GRA['Areia grossa'] = fuzz.trimf(GRA.universe, [0,0.6,2])
    GRA['Seixo'] = fuzz.trimf(GRA.universe, [0,2,200])
    GRA['Matacões'] = fuzz.trimf(GRA.universe, [0,200,200])

    SEL['Pessimamente'] = fuzz.trimf(SEL.universe, [0,0,100])
    SEL['Mal'] = fuzz.trimf(SEL.universe, [0,0,50])
    SEL['Moderadamente'] = fuzz.trimf(SEL.universe, [0,0,25])
    SEL['Bem'] = fuzz.trimf(SEL.universe, [0,0,1])
    SEL['Muito bem'] = fuzz.trimf(SEL.universe, [0,0,0.125])

#Intervalos numéricos manuais para o COT (saída)
COT['Muito baixo'] = fuzz.trimf(COT.universe, [0,0.1,1])
COT['Baixo'] = fuzz.trimf(COT.universe, [0,1,6])
COT['Médio'] = fuzz.trimf(COT.universe, [0,6,9])
COT['Alto'] = fuzz.trimf(COT.universe, [0,9,20])
COT['Muito alto'] = fuzz.trimf(COT.universe, [9,20,20])

#Visualização dos conjuntos Fuzzy

#O2.view()
#plt.show()

#Regras:

#Regra de ouro:
regraA = ctrl.Rule(PP['Muito alto'] | O2['Anóxico'], COT['Muito alto'])
regraB = ctrl.Rule(PP['Alto'] | O2['Anóxico'], COT['Alto'])



#No caso manual:
regra1 = ctrl.Rule(PP['Muito baixo'] | O2['Óxido'] | TS['Muito baixo'] & Z['Raso'] & GRA['Matacões'] & SEL['Pessimamente'], COT['Muito baixo'])
regra2 = ctrl.Rule(PP['Muito baixo'] | O2['Misto'] | TS['Muito baixo'] & Z['Raso'] & GRA['Seixo'] & SEL['Pessimamente'], COT['Muito baixo'])
regra3 = ctrl.Rule(PP['Baixo'] | O2['Anóxico'] | TS['Muito alto'] & Z['Raso'] & GRA['Matacões'] & SEL['Pessimamente'], COT['Muito baixo'])
regra4 = ctrl.Rule(PP['Médio'] | O2['Óxido'] | TS['Baixo'] & Z['Raso'] & GRA['Areia grossa'] & SEL['Mal'], COT['Muito baixo'])
regra5 = ctrl.Rule(PP['Muito baixo'] | O2['Óxido'] | TS['Médio'] & Z['Médio'] & GRA['Areia média'] & SEL['Moderadamente'], COT['Baixo'])
regra6 = ctrl.Rule(PP['Alto'] | O2['Anóxico'] | TS['Alto'] & Z['Raso'] & GRA['Areia fina'] & SEL['Bem'], COT['Baixo'])
regra7 = ctrl.Rule(PP['Baixo'] | O2['Óxido'] | TS['Alto'] & Z['Médio'] & GRA['Lama'] & SEL['Muito bem'], COT['Baixo'])
regra8 = ctrl.Rule(PP['Alto'] | O2['Anóxico'] | TS['Alto'] & Z['Raso'] & GRA['Areia grossa'] & SEL['Bem'], COT['Médio'])
regra9 = ctrl.Rule(PP['Muito alto'] | O2['Óxido'] | TS['Baixo'] & Z['Médio'] & GRA['Areia fina'] & SEL['Bem'], COT['Médio'])
regra10 = ctrl.Rule(PP['Médio'] | O2['Misto'] | TS['Baixo'] & Z['Médio'] & GRA['Areia média'] & SEL['Muito bem'], COT['Médio'])
regra11 = ctrl.Rule(PP['Alto'] | O2['Anóxico'] | TS['Médio'] & Z['Profundo'] & GRA['Lama'] & SEL['Muito bem'], COT['Alto'])
regra12 = ctrl.Rule(PP['Alto'] | O2['Misto'] | TS['Alto'] & Z['Profundo'] & GRA['Lama'] & SEL['Muito bem'], COT['Alto'])
regra13 = ctrl.Rule(PP['Muito alto'] | O2['Óxido'] | TS['Médio'] & Z['Profundo'] & GRA['Lama'] & SEL['Muito bem'], COT['Alto'])
regra14 = ctrl.Rule(PP['Médio'] | O2['Anóxico'] | TS['Baixo'] & Z['Muito profundo'] & GRA['Lama'] & SEL['Muito bem'], COT['Alto'])
regra15 = ctrl.Rule(PP['Muito alto'] | O2['Anóxico'] | TS['Médio'] & Z['Profundo'] & GRA['Lama'] & SEL['Muito bem'], COT['Muito alto'])
regra16 = ctrl.Rule(PP['Alto'] | O2['Misto'] | TS['Baixo'] & Z['Ultra profundo'] & GRA['Lama'] & SEL['Muito bem'], COT['Muito alto'])
regra17 = ctrl.Rule(PP['Muito alto'] | O2['Anóxico'] | TS['Médio'] & Z['Muito profundo'] & GRA['Lama'] & SEL['Muito bem'], COT['Muito alto'])
regra18 = ctrl.Rule(PP['Alto'] | O2['Anóxico'] | TS['Médio'] & Z['Profundo'] & GRA['Lama'] & SEL['Bem'], COT['Muito alto'])


#Sistema de Controle
#Condicional proposto pelo André em 29.03.23

#Regra de ouro
COT_ctrl = ctrl.ControlSystem([regraA,regraB])


#Simulação
COT_simulado = ctrl.ControlSystemSimulation(COT_ctrl)








#Passando novos valores de entrada para o sistema de controle. No futuro essa etapa vai er substituida por 6 arquivos de dados variando com a profundidade
COT_simulado.input['Produtividade primária'] = 0.5
COT_simulado.input['Oxigênio dissolvido'] = 0.5
COT_simulado.input['Taxa de sedimentação'] = 10
COT_simulado.input['Profundidade'] = 500
COT_simulado.input['Granulometria'] = 0.2
COT_simulado.input['Seleção'] = 0.8





#Computando novos valores da simulação
COT_simulado.compute()

#Resultado
print(COT_simulado.output['Conteúdo orgânico total'])
COT.view(sim=COT_simulado)
plt.show()



