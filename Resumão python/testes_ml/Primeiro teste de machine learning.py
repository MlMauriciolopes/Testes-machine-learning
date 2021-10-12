#Carregando o conjunto de dados
#https://www.kaggle.com/dell4010/wine-dataset/version/1
import pandas as pd
arquivo = pd.read_csv('C:/Users/mlsil/OneDrive/Documentos/DidaticaTech/wine_dataset.csv')
arquivo.head()

#Mudar variável da coluna style(string) para numérico
arquivo['style'] = arquivo['style'].replace('red', 0)
arquivo['style'] = arquivo['style'].replace('white', 1)

#Separando as variáveis entre preditoras e variáveis alvo
y = arquivo['style']
x = arquivo.drop('style', axis = 1)

from sklearn.model_selection import train_test_split

#Criando os conjuntos de dados de treino e teste
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size = 0.3) #escolhe x % dos dados para treino e teste

from sklearn.ensemble import ExtraTreesClassifier
#Criando do modelo:
modelo = ExtraTreesClassifier(n_estimators=100)
modelo.fit(x_treino, y_treino)

#Imprimindo resultados:
resultado = modelo.score(x_teste, y_teste)
print("Acurácia:", resultado)

y_teste[400:403]

x_teste[400:403]

previsoes = modelo.predict(x_teste[400:403])
previsoes