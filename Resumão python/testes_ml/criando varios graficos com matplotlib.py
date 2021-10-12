#
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-1000, 1000, 1)
y = x**2
plt.plot(x,y)
plt.show()

#Criar vários gráficos ao mesmo tempo
#Subplot divide uma região em linhas e colunas
y1 = x**2
y2 = x**3
y3 = -x**2
y4 = -x**3
plt.subplot(2,2,1)
plt.plot(x, y1)
plt.subplot(2,2,2)
plt.plot(x, y2)
plt.subplot(2,2,3)
plt.plot(x, y3)
plt.subplot(2,2,4)
plt.plot(y, y4)
plt.show()

#
y1 = x**2
y2 = x**3
y3 = -x**2
y4 = -x**3

figura = plt.figure(figsize=(10,10))

figura.add_subplot(2,2,1)
plt.plot(x, y1)
figura.add_subplot(2,2,2)
plt.plot(x, y2)
figura.add_subplot(2,2,3)
plt.plot(x, y3)
figura.add_subplot(2,2,4)
plt.plot(x, y4)
plt.show()

#Criar vários gráficos com o loop for
y1 = x**2
y2 = x**3
y3 = -x**2
y4 = -x**3
y = [y1, y2, y3, y4]

figura = plt.figure(figsize=(10,10))
for i in range(4):
    figura.add_subplot(2,2,i+1)
    plt.plot(x, y[i])
plt.show()

#imagens em blocos
#Carregar uma imagem em bloco
from skimage.io import imread
imagem = imread('C:/Users/mlsil/OneDrive/Documentos/DidaticaTech/imagem9.jpg')
plt.imshow(imagem)
plt.show()


#criar vários blocos com diversas imagens

#criar um diretório
endereco = 'C:/Users/mlsil/OneDrive/Documentos/DidaticaTech/'
imagens = []
for i in range(9):
    imagem = imread(endereco+'imagem'+str(i+1)+'.jpg')
    imagens.append(imagem)
 
figura = plt.figure(figsize=(15,8))
for i in range(9):
    figura.add_subplot(3,3,i+1)
    plt.imshow(imagens[i])
plt.show()