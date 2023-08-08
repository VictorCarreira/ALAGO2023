#Pacotes
# -*- coding: utf-8 -*-

#####Programa Fuzzy_lakes#######


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
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

#Leitura automática dos intervalos de dados da tabela

dfi = pd.read_excel(open('../input/Lake_regras_fuzzy.xlsx', 'rb'), sheet_name='Intervalos', index_col=0, header = 0)


print(dfi)


membro = input('Escolha a função de pertinência(triangular ou trapezoidal):')

if membro == 'triangular':
    #Intervalos manuais da tabela (entradas) função de pertinência triangular 
    PP['Muito baixo'] = fuzz.trimf(PP.universe, [0,dfi.Mínimos[0],dfi.Máximos[0]])  
    PP['Baixo'] = fuzz.trimf(PP.universe, [0,dfi.Mínimos[1],dfi.Máximos[1]])
    PP['Médio'] = fuzz.trimf(PP.universe, [0,dfi.Mínimos[2],dfi.Máximos[2]])
    PP['Alto'] = fuzz.trimf(PP.universe, [0,dfi.Mínimos[3],dfi.Máximos[3]])
    PP['Muito alto'] = fuzz.trimf(PP.universe, [0,dfi.Mínimos[4],dfi.Máximos[4]])

    O2['Anóxico'] = fuzz.trimf(O2.universe, [0,dfi.Mínimos[5],dfi.Máximos[5]])
    O2['Misto'] = fuzz.trimf(O2.universe, [0,dfi.Mínimos[6],dfi.Máximos[6]])
    O2['Óxido'] = fuzz.trimf(O2.universe, [0,dfi.Mínimos[7],dfi.Máximos[7]])

    TS['Muito baixo'] = fuzz.trimf(TS.universe, [0,dfi.Mínimos[8],dfi.Máximos[8]])
    TS['Baixo'] = fuzz.trimf(TS.universe, [0,dfi.Mínimos[9],dfi.Máximos[9]])
    TS['Médio'] = fuzz.trimf(TS.universe, [0,dfi.Mínimos[10],dfi.Máximos[10]])
    TS['Alto'] = fuzz.trimf(TS.universe, [0,dfi.Mínimos[11],dfi.Máximos[11]])
    TS['Muito alto'] = fuzz.trimf(TS.universe, [0,dfi.Mínimos[12],dfi.Máximos[12]])

    Z['Raso'] = fuzz.trimf(Z.universe, [0,dfi.Mínimos[13],dfi.Máximos[13]])
    Z['Médio'] = fuzz.trimf(Z.universe, [0,dfi.Mínimos[14],dfi.Máximos[14]])
    Z['Profundo'] = fuzz.trimf(Z.universe, [0,dfi.Mínimos[15],dfi.Máximos[15]])
    Z['Muito profundo'] = fuzz.trimf(Z.universe, [0,dfi.Mínimos[16],dfi.Máximos[16]])
    Z['Ultra profundo'] = fuzz.trimf(Z.universe, [0,dfi.Mínimos[17],dfi.Máximos[17]])

    GRA['Lama'] = fuzz.trimf(GRA.universe, [0,dfi.Mínimos[18],dfi.Máximos[18]])
    GRA['Areia fina'] = fuzz.trimf(GRA.universe, [0,dfi.Mínimos[19],dfi.Máximos[19]])
    GRA['Areia média'] = fuzz.trimf(GRA.universe, [0,dfi.Mínimos[20],dfi.Máximos[20]])
    GRA['Areia grossa'] = fuzz.trimf(GRA.universe, [0,dfi.Mínimos[21],dfi.Máximos[21]])
    GRA['Seixo'] = fuzz.trimf(GRA.universe, [0,dfi.Mínimos[22],dfi.Máximos[22]])
    GRA['Matacões'] = fuzz.trimf(GRA.universe, [0,dfi.Mínimos[23],dfi.Máximos[23]])

    SEL['Pessimamente'] = fuzz.trimf(SEL.universe, [0,dfi.Mínimos[24],dfi.Máximos[24]])
    SEL['Mal'] = fuzz.trimf(SEL.universe, [0,dfi.Mínimos[25],dfi.Máximos[25]])
    SEL['Moderadamente'] = fuzz.trimf(SEL.universe, [0,dfi.Mínimos[26],dfi.Máximos[26]])
    SEL['Bem'] = fuzz.trimf(SEL.universe, [0,dfi.Mínimos[27],dfi.Máximos[27]])
    SEL['Muito bem'] = fuzz.trimf(SEL.universe, [0,dfi.Mínimos[28],dfi.Máximos[28]])

    #Intervalos numéricos manuais para o COT (saída)
    COT['Muito baixo'] = fuzz.trimf(COT.universe, [0,dfi.Mínimos[29],dfi.Máximos[29]])
    COT['Baixo'] = fuzz.trimf(COT.universe, [0,dfi.Mínimos[30],dfi.Máximos[30]])
    COT['Médio'] = fuzz.trimf(COT.universe, [0,dfi.Mínimos[31],dfi.Máximos[31]])
    COT['Alto'] = fuzz.trimf(COT.universe, [0,dfi.Mínimos[32],dfi.Máximos[32]])
    COT['Muito alto'] = fuzz.trimf(COT.universe, [9,dfi.Mínimos[33],dfi.Máximos[33]])

else:
    #Intervalos manuais da tabela (entradas) função de pertinência trapezoidal
    PP['Muito baixo'] = fuzz.trapmf(PP.universe, [0,dfi.Mínimos[0],dfi.Máximos[0],dfi.Máximos[0]])  
    PP['Baixo'] = fuzz.trapmf(PP.universe, [0,dfi.Mínimos[1],dfi.Máximos[1],dfi.Máximos[1]])
    PP['Médio'] = fuzz.trapmf(PP.universe, [0,dfi.Mínimos[2],dfi.Máximos[2],dfi.Máximos[2]])
    PP['Alto'] = fuzz.trapmf(PP.universe, [0,dfi.Mínimos[3],dfi.Máximos[3],dfi.Máximos[3]])
    PP['Muito alto'] = fuzz.trapmf(PP.universe, [0,dfi.Mínimos[4],dfi.Máximos[4],dfi.Máximos[4]])

    O2['Anóxico'] = fuzz.trapmf(O2.universe, [0,dfi.Mínimos[5],dfi.Máximos[5],dfi.Máximos[5]])
    O2['Misto'] = fuzz.trapmf(O2.universe, [0,dfi.Mínimos[6],dfi.Máximos[6],dfi.Máximos[6]])
    O2['Óxido'] = fuzz.trapmf(O2.universe, [0,dfi.Mínimos[7],dfi.Máximos[7],dfi.Máximos[7]])

    TS['Muito baixo'] = fuzz.trapmf(TS.universe, [0,dfi.Mínimos[8],dfi.Máximos[8],dfi.Máximos[8]])
    TS['Baixo'] = fuzz.trapmf(TS.universe, [0,dfi.Mínimos[9],dfi.Máximos[9],dfi.Máximos[9]])
    TS['Médio'] = fuzz.trapmf(TS.universe, [0,dfi.Mínimos[10],dfi.Máximos[10],dfi.Máximos[10]])
    TS['Alto'] = fuzz.trapmf(TS.universe, [0,dfi.Mínimos[11],dfi.Máximos[11],dfi.Máximos[11]])
    TS['Muito alto'] = fuzz.trapmf(TS.universe, [0,dfi.Mínimos[12],dfi.Máximos[12],dfi.Máximos[12]])

    Z['Raso'] = fuzz.trapmf(Z.universe, [0,dfi.Mínimos[13],dfi.Máximos[13],dfi.Máximos[13]])
    Z['Médio'] = fuzz.trapmf(Z.universe, [0,dfi.Mínimos[14],dfi.Máximos[14],dfi.Máximos[14]])
    Z['Profundo'] = fuzz.trapmf(Z.universe, [0,dfi.Mínimos[15],dfi.Máximos[15],dfi.Máximos[15]])
    Z['Muito profundo'] = fuzz.trapmf(Z.universe, [0,dfi.Mínimos[16],dfi.Máximos[16],dfi.Máximos[16]])
    Z['Ultra profundo'] = fuzz.trapmf(Z.universe, [0,dfi.Mínimos[17],dfi.Máximos[17],dfi.Máximos[17]])

    GRA['Lama'] = fuzz.trapmf(GRA.universe, [0,dfi.Mínimos[18],dfi.Máximos[18],dfi.Máximos[18]])
    GRA['Areia fina'] = fuzz.trapmf(GRA.universe, [0,dfi.Mínimos[19],dfi.Máximos[19],dfi.Máximos[19]])
    GRA['Areia média'] = fuzz.trapmf(GRA.universe, [0,dfi.Mínimos[20],dfi.Máximos[20],dfi.Máximos[20]])
    GRA['Areia grossa'] = fuzz.trapmf(GRA.universe, [0,dfi.Mínimos[21],dfi.Máximos[21],dfi.Máximos[21]])
    GRA['Seixo'] = fuzz.trapmf(GRA.universe, [0,dfi.Mínimos[22],dfi.Máximos[22],dfi.Máximos[22]])
    GRA['Matacões'] = fuzz.trapmf(GRA.universe, [0,dfi.Mínimos[23],dfi.Máximos[23],dfi.Máximos[23]])

    SEL['Pessimamente'] = fuzz.trapmf(SEL.universe, [0,dfi.Mínimos[24],dfi.Máximos[24],dfi.Máximos[24]])
    SEL['Mal'] = fuzz.trapmf(SEL.universe, [0,dfi.Mínimos[25],dfi.Máximos[25],dfi.Máximos[25]])
    SEL['Moderadamente'] = fuzz.trapmf(SEL.universe, [0,dfi.Mínimos[26],dfi.Máximos[26],dfi.Máximos[26]])
    SEL['Bem'] = fuzz.trapmf(SEL.universe, [0,dfi.Mínimos[27],dfi.Máximos[27],dfi.Máximos[27]])
    SEL['Muito bem'] = fuzz.trapmf(SEL.universe, [0,dfi.Mínimos[28],dfi.Máximos[28],dfi.Máximos[28]])

    #Intervalos numéricos manuais para o COT (saída)
    COT['Muito baixo'] = fuzz.trapmf(COT.universe, [0,dfi.Mínimos[29],dfi.Máximos[29],dfi.Máximos[29]])
    COT['Baixo'] = fuzz.trapmf(COT.universe, [0,dfi.Mínimos[30],dfi.Máximos[30],dfi.Máximos[30]])
    COT['Médio'] = fuzz.trapmf(COT.universe, [0,dfi.Mínimos[31],dfi.Máximos[31],dfi.Máximos[31]])
    COT['Alto'] = fuzz.trapmf(COT.universe, [0,dfi.Mínimos[32],dfi.Máximos[32],dfi.Máximos[32]])
    COT['Muito alto'] = fuzz.trapmf(COT.universe, [9,dfi.Mínimos[33],dfi.Máximos[33],dfi.Máximos[33]])


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
COT_ctrl = ctrl.ControlSystem([regraA,regraB,regra1,regra2,regra3,regra4,regra5,regra6,regra7,regra8,regra9,regra10,regra11,regra12,regra13,regra14,regra15,regra16,regra17,regra18])


#Simulação
COT_simulado = ctrl.ControlSystemSimulation(COT_ctrl)


#Passando novos valores de entrada para o sistema de controle. No futuro essa etapa vai er substituida por 6 arquivos de dados variando com a profundidade
#COT baixo: Kivu
COT_simulado.input['Produtividade primária'] = 264
COT_simulado.input['Oxigênio dissolvido'] = 11.76
COT_simulado.input['Taxa de sedimentação'] = 8
COT_simulado.input['Profundidade'] = 480
COT_simulado.input['Granulometria'] = 0.002
COT_simulado.input['Seleção'] =1





#Computando novos valores da simulação
COT_simulado.compute()

#Resultado
print(COT_simulado.output['Conteúdo orgânico total'])
COT.view(sim=COT_simulado)
plt.show()
#plt.savefig('../images/COT_Edward_triangular.png', format='png')

#Calculo do erro:
COT_calc_T = [4.67,4.79] 
COT_calc_V = [10.87,10.14]
COT_calc_K = [7.67,10.72]

COT_obs_T = [4.81,4.81] 
COT_obs_V = [11.23,11.23] 
COT_obs_K = [7.14,7.14]

lake_T = ['Triangular','Trapezoidal'] 
lake_V = ['Triangular','Trapezoidal'] 
lake_K = ['Triangular','Trapezoidal']





def rms(a,b):
    '''
    Root mean square error.
    Inputs {a,b}: Observed and predicted data
    Returns {list}: RMS
    '''
    MSE = np.square(np.subtract(a,b)).mean()
    RMSE = math.sqrt(MSE)
    print('Root Mean Square Error:\n')
    print(RMSE)

    return RMSE
  

def phi(a,b):
    '''
    Error function calculation. Calculates the difference between the calculated model and predicted model in absolute terms.
    Returns {list}: error 
    '''
    erro = []
    for i in range(np.size(a)):
        error = abs(a[i]-b[i])
        erro.append(error)

    return erro


#erro = phi(COT_calc_T,COT_obs_T)
#print('erro=',erro)

erro = rms(COT_obs_T,COT_calc_T)

plt.figure(figsize=(5,5))

plt.errorbar(COT_calc_T, COT_obs_T, yerr=erro, fmt="o", color="r")
plt.bar(COT_calc_T, COT_obs_T,width = 0.01)
plt.xticks(COT_calc_T, lake_T)
plt.title('Lago Tanganyika - COT')
plt.show()


erro = rms(COT_calc_V,COT_obs_V)
print('erro=',erro)


plt.errorbar(COT_calc_V, COT_obs_V, yerr=erro, fmt="o", color="r")
plt.bar(COT_calc_V, COT_obs_V,width = 0.1)
plt.xticks(COT_calc_V, lake_V)
plt.title('Lago Victoria - COT')
plt.show()


erro = rms(COT_calc_K,COT_obs_K)
print('erro=',erro)


plt.errorbar(COT_calc_K, COT_obs_K, yerr=erro, fmt="o", color="r")
plt.bar(COT_calc_K, COT_obs_K,width = 0.5)
plt.xticks(COT_calc_K, lake_K)
plt.title('Lago Kivu - COT')
plt.show()


