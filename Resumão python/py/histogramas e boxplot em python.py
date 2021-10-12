#criando histogramas em Python 
#Cria um número de ocorrênicas, criando faixas de valores
#https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results/version/2
import pandas as pd
dados = pd.read_csv('C:/Users/mlsil/OneDrive/Documentos/DidaticaTech/athlete_events.csv')
dados.head()

#hist: comando do pandas para criar histogramas
import matplotlib.pyplot as plt
dados.hist(column='Weight', bins=100) #coluna para filtrar e o número de linhas 
plt.show()

----------------------------------------------------------------------------------------
#criando boxplot usando Python 
#
#https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results/version/2
import pandas as pd
dados = pd.read_csv('C:/Users/mlsil/OneDrive/Documentos/DidaticaTech/athlete_events.csv')
dados.head()

#
import matplotlib.pyplot as plt
#dados.boxplot(column='Age') #mostrar 1 coluna
dados.boxplot(column=['Age', 'Height', 'Weight']) #mostrar vários boxplots usando arrays
plt.show()
--------------------------------------------------------------------------------------------