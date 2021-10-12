#array : lista com algumas restrições/ listas com o mesmo tipo
import numpy as np
a = np.array([1, 2, 3])
print(a)
--------------------------------------------------------------------
b = np.array([(2, 5, 7),(5, 3, 9), (4, 6, 5)]) #estrutura array <=
print(b)
#R:[[2 5 7]
 [5 3 9]
 [4 6 5]]
------------------------------------------------------------------------
#
#c = np.ones([4,3]) #Dimensões da matriz: 4 linhas e 3 colunas de números um
c = np.zeros([4,3]) #Dimensões da matriz: 4 linhas e 3 colunas de números zeros
print(c)
#R:[[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]
------------------------------------------------------------------------------
#
c = np.eye(4) #cria uma raiz quadrada do número dentro do parenteses
print(c)
#R:[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]
----------------------------------------------------------------------------
#outras funções
#b.min() #seleciona o valor mínimo dentro do array
#b.max() #seleciona o valor máximo dentro do array
#b.mean() #calcula a média dentro de uma array