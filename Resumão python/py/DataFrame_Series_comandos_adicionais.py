#Criar um data frame com pandas
import pandas as pd
alunos = {'Nome':['Ricardo', 'Pedro', 'roberto', 'Carlos'],
         'Nota':[4, 7, 5.5, 9],
         'Aprovado':['Não', 'Sim', 'Não', 'Sim']}
dataframe = pd.DataFrame(alunos) #D e F em maiúsculo
print(dataframe)
#R:     Nome  Nota Aprovado
0  Ricardo   4.0      Não
1    Pedro   7.0      Sim
2  roberto   5.5      Não
3   Carlos   9.0      Sim
-------------------------------------------------------------------------------
#Series cria um array com índices
import pandas as pd
objeto1 = pd.Series([2, 6, 9, 10, 5])
print(objeto1)
#R:
0     2
1     6
2     9
3    10
4     5
dtype: int64
------------------------------------------------------------------------------
#
import numpy as np
array1 = np.array([2, 6, 9, 10, 5])
array2 = np.array([(2, 6, 9, 10, 5), (20, 40, 60, 80, 99)])
print(array1)
print(array2)
--------------------------------------------------------------------------
#transformar um array em um vetor
objeto2 = pd.Series(array1)
print(objeto2)
----------------------------------------------------------------------------
#Explorando o DataFrame
import pandas as pd
alunosDIC = {'Nome':['Ricardo', 'Pedro', 'roberto', 'Carlos'],
         'Nota':[4, 7, 5.5, 9],
         'Aprovado':['Não', 'Sim', 'Não', 'Sim']}
alunosDF = pd.DataFrame(alunosDIC)
print(alunosDF)
#funções adicionais
alunosDF.head() #mostrar em forma de tabela de índice
alunosDF.shape #Mostra o tamanho do dataframe em linhas e colunas
alunosDF.describe() #Mostra informações de tabela como, média, mínimo, máximo ...
alunosDF.loc[alunosDF['Nome']=='Pedro'] #localizas dois dados de uma mesma tabela
alunosDF.loc[alunosDF['Aprovado']=='Sim']
-----------------------------------------------------------------------------------
#Explorando o DataFrame
import pandas as pd
alunosDIC = {'Nome':['Ricardo', 'Pedro', 'roberto', 'Carlos'],
         'Nota':[4, 7, 5.5, 9],
         'Aprovado':['Não', 'Sim', 'Não', 'Sim']}
alunosDF = pd.DataFrame(alunosDIC)
print(alunosDF)

#Cria uma tabela nova/Dataframe e mandar os dados selecionados da tabela 1 para a tabela nova
primeirasLinhas = alunosDF.loc[0:2] #nome da tabela nova
print(primeirasLinhas)

#Exemplo de criar um novo Dataframe e filtrar/passar para a tabela nova, todos os valores, menos os com o número 9
novoDF = alunosDF.loc[alunosDF['Nota']!=9]
print(novoDF)

#Exemplo de criar um novo Dataframe e filtrar/passar para a tabela nova, todos osa valores, menos os com os aprovados
alunosReprovados = alunosDF.loc[alunosDF['Aprovado']!='sim']
print(alunosReprovados)
