#Manipular dados faltantes(NaN) em um Dataset
import pandas as pd
#https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results/version/2
dados = pd.read_csv('C:/Users/mlsil/OneDrive/Documentos/DidaticaTech/athlete_events.csv')
dados.head()

#mostrando dados de linhas com todos do valores de campos completos
dados2 = dados.dropna()
dados2.shape

#prencher dados faltantes com alguma informação
enulo = dados.isnull()

faltantes = dados.isnull().sum()
print(faltantes)

#Calcular o percentual dos Datasets
faltantes_percentual = (dados.isnull().sum() / len(dados['ID']))*100
print(faltantes_percentual)

#Substituir dados faltantes no Dataset
dados['Medal'].fillna('Nenhuma', inplace = True)
dados['Age'].fillna(dados['Age'].mean(), inplace = True)
dados['Height'].fillna(dados['Height'].mean(), inplace = True)
dados['Weight'].fillna(dados['Weight'].mean(), inplace = True)
dados.head(100)