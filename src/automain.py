#Pacotes
# -*- coding: utf-8 -*-

#-------------Programa Fuzzy_lakes-------------#
# Determina o valor de COT através da lógica   #
#estocástica fuzzy com base em                 #
# dados de vários lagos conhecidos.            #
#----------------------------------------------#

#modulos externos
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import skfuzzy as fuzz
from skfuzzy import control as ctrl

#modulos internos
import sys
sys.path.insert(0,'../modules')
import  auxiliary as ax



#lendo os arquivos de entrada

dfd = pd.read_excel(open('../input/Lake_regras_fuzzy.xlsx', 'rb'), sheet_name='Discurso', index_col=0, header = 0)

print(dfd)

ax.pause()


#Definindo os parâmetros do modelo:
#Deve-se compreender o universo de variáveis divididas em dois grupos e o universo do discurso de cada uma delas
#Antecedentes: compreende os parâmetros de entrada
#Consequentes: compreende os parâmetros de saída
#Lista de antecedentes: produtividade primária, O² dissolvido, taxa de sedimentação, profundidade, granulometria, seleção
#Lista de consequentes: conteúdo orgânico total


#Antecedentes
PP = ctrl.Antecedent(np.arange(ax.d2ln(dfd.PP[0]),ax.d2ln(dfd.PP[1]),ax.d2ln(dfd.PP[2])), 'Produtividade primária')
O2 = ctrl.Antecedent(np.arange(dfd.O2[0],dfd.O2[1],dfd.O2[2]), 'Oxigênio dissolvido')
TS = ctrl.Antecedent(np.arange(dfd.TS[0],dfd.TS[1],dfd.TS[2]), 'Taxa de sedimentação')
Z  = ctrl.Antecedent(np.arange(ax.d2ln(dfd.Z[0]),ax.d2ln(dfd.Z[1]),ax.d2ln(dfd.Z[2])), 'Profundidade')
GRA = ctrl.Antecedent(np.arange(ax.d2ln(dfd.GRA[0]),ax.d2ln(dfd.GRA[1]),ax.d2ln(dfd.GRA[2])), 'Granulometria')
SEL = ctrl.Antecedent(np.arange(ax.d2ln(dfd.SEL[0]),ax.d2ln(dfd.SEL[1]),ax.d2ln(dfd.SEL[2])),'Seleção')

#Consequentes
COT = ctrl.Consequent(np.arange(dfd.COT[0],dfd.COT[1],dfd.COT[2]), 'Conteúdo orgânico total')

#intervalos=input('Insira o número dos intervalos de classe desejados (3, 5 ou 7):')

#print(type(intervalos))

#ax.stop()

PP.automf(7)
O2.automf(7)
TS.automf(7)
Z.automf(7)
GRA.automf(7)
SEL.automf(7)
COT.automf(7)
   
#Visualização dos conjuntos Fuzzy

#O2.view()
#plt.show()

#Regras: (OU = |  E = & ENTÃO = ,)

#Regra de ouro:
regraA = ctrl.Rule(PP['excellent'] | O2['dismal'], COT['excellent'])
regraB = ctrl.Rule(PP['good'] | O2['poor'], COT['decent'])

#Regras comuns:
regra1 = ctrl.Rule(PP['poor'] | O2['poor'] | TS['poor'] | Z['poor'] | GRA['poor'] | SEL['poor'], COT['excellent'] )
regra2 = ctrl.Rule(PP['excellent'] & TS['average'] | Z['average'] & GRA['dismal'] & SEL['excellent'], COT['average'])
regra3 = ctrl.Rule(PP['poor'] | TS['poor'] | Z['poor'] | GRA['poor'], COT['poor'])



#Sistema de Controle
#Condicional proposto pelo André em 29.03.23

#Cria um sistema de controle baseado nas regras de ouro e comum:


COT_ctrl = ctrl.ControlSystem([regraA,regraB,regra1,regra2,regra3])


#Simulação
COT_simulado = ctrl.ControlSystemSimulation(COT_ctrl)








#Passando novos valores de entrada para o sistema de controle. No futuro essa etapa vai er substituida por 6 arquivos de dados variando com a profundidade

#dados sintéticos

COT_simulado.input['Produtividade primária'] = 0.0001# ax.d2ln(ax.generate_data('exponencial',100))  
COT_simulado.input['Oxigênio dissolvido'] = 0.0001 #ax.generate_data('normal',100) 
COT_simulado.input['Taxa de sedimentação'] = 0.5 #ax.generate_data('normal',100) 
COT_simulado.input['Profundidade'] = 10 #ax.d2ln(ax.generate_data('exponencial',100)) 
COT_simulado.input['Granulometria'] = 20 #ax.d2ln(ax.generate_data('exponencial',100)) 
COT_simulado.input['Seleção'] = 12.5 #ax.d2ln(ax.generate_data('exponencial',100))  





#Computando novos valores da simulação
COT_simulado.compute()

#Resultado
print(COT_simulado.output['Conteúdo orgânico total'])
COT.view(sim=COT_simulado)
plt.show()



