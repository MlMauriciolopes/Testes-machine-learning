#Criar gráficos em Python em matplotlib
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

plt.scatter(x,y)
plt.show()

#função arrange preenche arrays automaticamente, digitando o valor inicial, o valor final, e o número de sequências
import numpy as np
x1 = np.arange(-1000,1000,1)
plt.plot(x1, x1**2)
plt.show()
--------------------------------------------------------------------------------------------
 #Exercício resolvido: Extrair da tabela atletas somente os dados de peso e altura de competidores masculinos
import pandas as pd
#https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results/version/2
dados = pd.read_csv('C:/Users/mlsil/OneDrive/Documentos/DidaticaTech/athlete_events.csv')
dados.head()

masculinos = dados.loc[dados['Sex']=='M']
a = masculinos['Height']
p = masculinos['Weight']

import matplotlib.pyplot as plt
plt.scatter(a,p)
plt.show()
---------------------------------------------------------------------------------------------------