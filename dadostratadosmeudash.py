# -*- coding: utf-8 -*-
"""dadosTratadosMeuDash.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jyALQ_5I915YeM3pctmQx6qOHxqm4JWn
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#importando CSV
dadosMeuDash = pd.read_csv('/content/drive/MyDrive/AgentesDataDash/dadosJosue.csv',)
dadosMeuDash

#filtrando a coluna
dadosMeuDash.loc[:, '__sub_status__1'].to_frame()

dadosMeuDash.rename(columns={'__sub_status__1': 'status'}, inplace = True)
dadosMeuDash

contagemDeStatus = dadosMeuDash["status"].value_counts().to_frame().reset_index()
contagemDeStatus.columns = ["status","total"]

contagemDeStatus

#soma total da coluna
totalStatus = dadosMeuDash['status'].value_counts()
totalGeral = totalStatus.sum()

#Soma status implementados
totalImplemented = totalStatus.loc['so - verified']
totalImplemented2 = totalStatus.loc['so - unverified']
totalImplemented3 = totalStatus.loc['so - verification not needed']

#soma total Inativados
totalNotReady = totalStatus.loc['in - not ready']
totalNotReachable = totalStatus.loc['in - not reachable']
totalNotInterested = totalStatus.loc['in - not interested']

#soma em andamento
totalAwaitingValidation = totalStatus.loc['ni - awaiting validation']
totalReschedulle = totalStatus.loc['as - reschedule 1']
totalAwaitingInputs = totalStatus.loc['ni - awaiting inputs']

#condições
totaldeImplementados = totalImplemented + totalImplemented2 + totalImplemented3
totaldeInactives = totalNotReady + totalNotReachable + totalNotInterested
totalEmAndamento = totalAwaitingValidation + totalReschedulle + totalAwaitingInputs

total_Outros = totalGeral - totaldeImplementados

totaldeImplementados

substatus = {
    'substatus' : ['Implemented','Inactive','Andamento'],
    'total' : [totaldeImplementados, totaldeInactives, totalEmAndamento]
}

plt.figure(figsize=(14,10))
plt.savefig('comparacao.png')
substatus = pd.DataFrame(substatus)
sns.barplot(x='substatus',y='total', data = substatus,).set(title='Casos Fechados')

#salvando o CSV
substatusinAgente.to_csv('/content/drive/MyDrive/AgentesDataDash/substatusInFinal.csv')

#salvando o CSV
substatusin.to_csv('/content/drive/MyDrive/AgentesDataDash/substatus.csv')