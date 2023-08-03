#Pacotes
# -*- coding: utf-8 -*-

#####Programa Fuzzy_lakes#######


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from skfuzzy import control as ctrl

#modulos internos
import sys
sys.path.insert(0,'../modules')
import  auxiliary as ax

#lendo os arquivos de entrada

dfd = pd.read_excel(open('../input/Lake_regras_fuzzy_RN.xlsx', 'rb'),
                    sheet_name='Discurso_RN2', index_col=0, header = 0)

print(dfd)




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
GRA = ctrl.Antecedent(np.arange(0,2000,0.002), 'Granulometria')
#Consequentes
COT = ctrl.Consequent(np.arange(dfd.COT[0],dfd.COT[1],dfd.COT[2]), 'Conteúdo orgânico total')

#Leitura automática dos intervalos de dados da tabela

dfi = pd.read_excel(open('../input/Lake_regras_fuzzy_RN.xlsx', 'rb'), sheet_name='Intervalos_RN2', index_col=0, header = 0)


print(dfi)

#Intervalos manuais da tabela (entradas)

PP['Baixo'] = fuzz.trimf(PP.universe, [0,dfi.Mínimos[0],dfi.Máximos[0]])
PP['Médio'] = fuzz.trimf(PP.universe, [0,dfi.Mínimos[1],dfi.Máximos[1]])
PP['Alto'] = fuzz.trimf(PP.universe, [0,dfi.Mínimos[2],dfi.Máximos[2]])

O2['Anóxico'] = fuzz.trimf(O2.universe, [0,dfi.Mínimos[3],dfi.Máximos[3]])
O2['Misto'] = fuzz.trimf(O2.universe, [0,dfi.Mínimos[4],dfi.Máximos[4]])
O2['Óxido'] = fuzz.trimf(O2.universe, [0,dfi.Mínimos[5],dfi.Máximos[5]])


TS['Baixo'] = fuzz.trimf(TS.universe, [0,dfi.Mínimos[6],dfi.Máximos[6]])
TS['Médio'] = fuzz.trimf(TS.universe, [0,dfi.Mínimos[7],dfi.Máximos[7]])
TS['Alto'] = fuzz.trimf(TS.universe, [0,dfi.Mínimos[8],dfi.Máximos[8]])

GRA['Lama'] = fuzz.trimf(GRA.universe, [0,dfi.Mínimos[9],dfi.Máximos[9]])
GRA['Areia'] = fuzz.trimf(GRA.universe, [0,dfi.Mínimos[10],dfi.Máximos[10]])

#Intervalos numéricos manuais para o COT (saída)
COT['Muito baixo'] = fuzz.trimf(COT.universe, [0,dfi.Mínimos[11],dfi.Máximos[11]])
COT['Baixo'] = fuzz.trimf(COT.universe, [0,dfi.Mínimos[12],dfi.Máximos[12]])
COT['Médio'] = fuzz.trimf(COT.universe, [0,dfi.Mínimos[13],dfi.Máximos[13]])
COT['Alto'] = fuzz.trimf(COT.universe, [0,dfi.Mínimos[14],dfi.Máximos[14]])
COT['Muito alto'] = fuzz.trimf(COT.universe, [9,dfi.Mínimos[15],dfi.Máximos[15]])

#Visualização dos conjuntos Fuzzy

#O2.view()
#plt.show()


 
#Regras:

regra1  = ctrl.Rule(PP['Baixo']  & O2['Óxido']     & TS['Baixo'] &    GRA['Lama']     , COT['Muito baixo'])
regra2  = ctrl.Rule(PP['Baixo']  & O2['Óxido']     & TS['Baixo'] |    GRA['Areia']    , COT['Muito baixo'])
regra3  = ctrl.Rule(PP['Baixo']  & O2['Óxido']     | TS['Médio'] &    GRA['Lama']     , COT['Muito baixo'])
regra4  = ctrl.Rule(PP['Baixo']  & O2['Óxido']     | TS['Médio'] |    GRA['Areia']    , COT['Muito baixo'])
regra5  = ctrl.Rule(PP['Baixo']  & O2['Óxido']     | TS['Alto']  &    GRA['Lama']     , COT['Muito baixo'])
regra6  = ctrl.Rule(PP['Baixo']  & O2['Óxido']     | TS['Alto']  |    GRA['Areia']    , COT['Muito baixo'])
regra7  = ctrl.Rule(PP['Baixo']  & O2['Anóxico']   & TS['Baixo'] &    GRA['Lama']     , COT['Médio'])
regra8  = ctrl.Rule(PP['Baixo']  & O2['Anóxico']   & TS['Baixo'] &    GRA['Areia']    , COT['Muito baixo'])
regra9  = ctrl.Rule(PP['Baixo']  & O2['Anóxico']   & TS['Médio'] &    GRA['Lama']     , COT['Muito baixo'])
regra10 = ctrl.Rule(PP['Baixo']  & O2['Anóxico']   & TS['Médio'] |    GRA['Areia']    , COT['Muito baixo'])
regra11 = ctrl.Rule(PP['Baixo']  & O2['Anóxico']   & TS['Alto']  &    GRA['Lama']     , COT['Muito baixo'])
regra12 = ctrl.Rule(PP['Baixo']  & O2['Anóxico']   & TS['Alto']  |    GRA['Areia']    , COT['Muito baixo'])
regra13 = ctrl.Rule(PP['Médio']  & O2['Óxido']     & TS['Baixo'] &    GRA['Lama']     , COT['Muito baixo'])
regra14 = ctrl.Rule(PP['Médio']  & O2['Óxido']     & TS['Baixo'] |    GRA['Areia']    , COT['Muito baixo'])
regra15 = ctrl.Rule(PP['Médio']  & O2['Óxido']     & TS['Médio'] &    GRA['Lama']     , COT['Muito baixo'])
regra16 = ctrl.Rule(PP['Médio']  & O2['Óxido']     & TS['Médio'] |    GRA['Areia']    , COT['Muito baixo'])
regra17 = ctrl.Rule(PP['Médio']  & O2['Óxido']     & TS['Alto']  &    GRA['Lama']     , COT['Baixo'])
regra18 = ctrl.Rule(PP['Médio']  & O2['Óxido']     & TS['Alto']  |    GRA['Areia']    , COT['Muito baixo'])
regra19 = ctrl.Rule(PP['Médio']  & O2['Anóxico']   & TS['Baixo'] &    GRA['Lama']     , COT['Alto'])
regra20 = ctrl.Rule(PP['Médio']  & O2['Anóxico']   & TS['Baixo'] &    GRA['Areia']    , COT['Muito baixo'])
regra21 = ctrl.Rule(PP['Médio']  & O2['Anóxico']   & TS['Médio'] &    GRA['Lama']     , COT['Médio'])
regra22 = ctrl.Rule(PP['Médio']  & O2['Anóxico']   & TS['Médio'] &    GRA['Areia']    , COT['Muito baixo'])
regra23 = ctrl.Rule(PP['Médio']  & O2['Anóxico']   & TS['Alto']  &    GRA['Lama']     , COT['Baixo'])
regra24 = ctrl.Rule(PP['Médio']  & O2['Anóxico']   & TS['Alto']  &    GRA['Areia']    , COT['Muito baixo'])
regra25 = ctrl.Rule(PP['Alto']   & O2['Óxido']     & TS['Baixo'] &    GRA['Lama']     , COT['Muito baixo'])
regra26 = ctrl.Rule(PP['Alto']   & O2['Óxido']     & TS['Baixo'] |    GRA['Areia']    , COT['Muito baixo'])
regra27 = ctrl.Rule(PP['Alto']   & O2['Óxido']     & TS['Médio'] &    GRA['Lama']     , COT['Baixo'])
regra28 = ctrl.Rule(PP['Alto']   & O2['Óxido']     & TS['Médio'] &    GRA['Areia']    , COT['Muito baixo'])
regra29 = ctrl.Rule(PP['Alto']   & O2['Óxido']     & TS['Alto']  &    GRA['Lama']     , COT['Médio'])
regra30 = ctrl.Rule(PP['Alto']   & O2['Óxido']     & TS['Alto']  &    GRA['Areia']   , COT['Muito baixo'])
regra31 = ctrl.Rule(PP['Alto']   & O2['Anóxico']   & TS['Baixo'] &    GRA['Lama']     , COT['Muito alto'])
regra32 = ctrl.Rule(PP['Alto']   & O2['Anóxico']   & TS['Baixo'] &    GRA['Areia']    , COT['Baixo'])
regra33 = ctrl.Rule(PP['Alto']   & O2['Anóxico']   & TS['Médio'] &    GRA['Lama']     , COT['Alto'])
regra34 = ctrl.Rule(PP['Alto']   & O2['Anóxico']   & TS['Médio'] &    GRA['Areia']    , COT['Baixo'])
regra35 = ctrl.Rule(PP['Alto']   & O2['Anóxico']   & TS['Alto']  &    GRA['Lama']     , COT['Médio'])
regra36 = ctrl.Rule(PP['Alto']   & O2['Anóxico']   & TS['Alto']  &    GRA['Areia']    , COT['Muito baixo'])


#Sistema de Controle
#Condicional proposto pelo André em 29.03.23

#Regra de ouro
COT_ctrl = ctrl.ControlSystem([regra1,regra2,regra3,regra4,regra5,
                               regra6,regra7,regra8,regra9,regra10,
                               regra11,regra12,regra13,regra14,regra15,
                               regra16,regra17,regra18,regra19,regra20,
                               regra21,regra22,regra23,regra24,
                               regra25,regra26,regra27, regra28,regra29,
                               regra30,regra31,regra32,regra33,regra34,regra35,
                               regra36])


#Simulação
COT_simulado = ctrl.ControlSystemSimulation(COT_ctrl)


#Passando novos valores de entrada para o sistema de controle. 
# No futuro essa etapa vai er substituida por 6 arquivos de dados variando com a profundidade
COT_simulado.input['Produtividade primária'] = 264.00
COT_simulado.input['Oxigênio dissolvido'] = 11.76
COT_simulado.input['Taxa de sedimentação'] = 8.0
COT_simulado.input['Granulometria'] = 0.1

#COT_simulado.input['Profundidade'] = 500
#COT_simulado.input['Granulometria'] = 0.2
#COT_simulado.input['Seleção'] = 0.8





#Computando novos valores da simulação
COT_simulado.compute()

#Resultado
print('COT_calc = ', COT_simulado.output['Conteúdo orgânico total'])
COT.view(sim=COT_simulado)
plt.show()


# Calculo do Erro
COT_observado = 7.14
Erro = COT_observado - COT_simulado.output['Conteúdo orgânico total']
print("Erro = ", Erro)