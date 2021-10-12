#Pandas com Numpy
#Criar uma tabela no excel e depois importar dentro do py com o passo abaixo
import pandas as pd
dados = pd.read_excel('C:/Users/mlsil/OneDrive/Documentos/DidaticaTech/arquivo1.xlsx')
dados.head(10) #variável do comando pandas

#https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results/version/2
dados2 = pd.read_csv('C:/Users/mlsil/OneDrive/Documentos/DidaticaTech/athlete_events.csv')
dados2.head(50)