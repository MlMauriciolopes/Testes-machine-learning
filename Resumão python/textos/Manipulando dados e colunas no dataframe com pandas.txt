#
import pandas as pd
#https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results/version/2
dados = pd.read_csv('C:/Users/mlsil/OneDrive/Documentos/DidaticaTech/athlete_events.csv')
dados.head()

#alterar dados de uma tabela usando pandas
dados.rename(columns={'Name':'Nome','Sex':'Sexo','Age':'Idade'})

#Selecionar os dados de uma tabela e contar os valores iguais selecionados
dados['Medal'].value_counts()

#Mostrando os dados do campo 'City'
dados['City'].value_counts()

#Mostra vários dados importantes da tabela
dados.describe()
------------------------------------------------------------------------------------------
#Excluir linhas e colunas no Dataframe
import pandas as pd
#https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results/version/2
dados = pd.read_csv('C:/Users/mlsil/OneDrive/Documentos/DidaticaTech/athlete_events.csv')
dados.head()
#
dados.drop('ID', axis = 1, inplace=True) #"axis = 0" são linhas e "axis = 1" são clounas
dados.drop('Season', axis = 1, inplace=True)
dados.drop('City', axis = 1, inplace=True)
dados.head()
--------------------------------------------------------------------------------------------