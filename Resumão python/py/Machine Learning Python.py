#exemplo de listas encadeadas = comando select
lista2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
select = lista2[1] 
print(select) # R:[4, 5, 6]
type(select) #R: list

select = lista2[0][1]
print(select) #R: 2
type(select) #r: int

#função choice
import random
cidades = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Porto Alegre', 'Salvador', 'Florianópolis']
escolhida = random.choice(cidades)
print('A cidade escolhida é: ', escolhida)

#função append
a = [1 ,2, 3, 4, 5, 6, 7, 8, 9, 10]
a.append(15)
print(a) #R:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 15]

b =[20, 30, 40, 50, 60]
for item in b:
    a.append(item)
print(a) #R:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 15, 20, 30, 40, 50, 60]

#Exercício: Transformar int em float, a adicionar eles na lista
x = [2, 4, 10, 6, 8, 25, 50, 100]
nova = []
for i in x:
    nova.append(float(i))
print(nova) #R:[2.0, 4.0, 10.0, 6.0, 8.0, 25.0, 50.0, 100.0]

**********************tupla**********************************
#tupla (É uma lista que não pode ser alterada de nenhuma forma
tupla = (10, 20, 30, 40, 50)
print(tupla)

#Transformando listas em tuplas
lista = [20, 40, 60, 80, 100]
novaTupla = tuple(lista)
print(novaTupla)
*********************dicionario******************************
#Dicionário: são índices de chave e valor, utilizando as chaves como interpretador
dicionario = {'Curso': 'Python para ML', 'Produtor': 'Didatica Tech', 'Preço': 'Gratuito', 'Nota':10}
a = dicionario['Preço']
print(a)
#alterar valores dentro do dicionário
dicionario['Preço'] = 'Rs 300,00'
print(dicionario) #R:{'Curso': 'Python para ML', 'Produtor': 'Didatica Tech', 'Preço': 'Rs 300,00', 'Nota': 10}
#alterar valores dentro do dicionário
dicionario['Preço'] = 'Rs 300,00'
print(dicionario)

#comandos adicionais
dicionario.keys() #mostra os índices do dicionario
dicionario.values() #mostra os valores do índices do dicionário
dicionario.items() #mostra os índices e os valores do dicionário
dicionario.clear() #apaga tudo dentro do dicionario
 
*********************comandos adicionais***********************
#manipular strings = comandos
frase = 'Estou gostando do curso'

#frase[:10] #mostra o número de letras até o número desejado
#frase[2:13:3] #mostra onde começa, onde termina (1 e 2) e o terceiro valor mostra qtas casas o programa vai pular
#frase[0:] #mostra o número de letras do início até o final, sem interrupção

frase.count(' ') #espaços
frase.count('d') #letras

len(frase)

frase.replace('curso', 'aprendizado')#substitui strings 

*************************função lambda***************************
#função def
def somaQuadrados(a,b):
    somaQ = a**2 +b**2
    return somaQ

#lambda = forma resumida de definir uma função 'def'
somaQuadrados2 = lambda a, b: a**2 + b**2
somaQuadrados2(2,3)

*************************função map*************************
#convertendo Km/h por MPH
kmh = [20, 40, 60, 80, 100, 120, 140, 160, 180]
mph = []
for i in kmh:
    mph.append(i/1.61)
print(mph)

#função map
kmh = [20, 40, 60, 80, 100, 120, 140, 160, 180]
mph = list(map(lambda x: x/1.61,kmh))
print(mph)

***************List comprehension*****************************
#função list comprehension
#cria uma função de diz onde vai ser aplicada
#tem uma função na esquerda, e um for na direita
#comando for varrendo todos os elementos de uma função
kmh = [20, 40, 60, 80, 100, 120, 140, 160, 180]
mph = [x/1.61 for x in kmh]
print(mph) #R:[12.422360248447204, 24.844720496894407, 37.267080745341616, 49.689440993788814, 62.11180124223602, 74.53416149068323, 86.95652173913042, 99.37888198757763, 111.80124223602483]

#exemplo 2 list comprehension
caracteres = [i for i in 'Mauricio Lopes da Silva']
print(caracteres) #R:['M', 'a', 'u', 'r', 'i', 'c', 'i', 'o', ' ', 'L', 'o', 'p', 'e', 's', ' ', 'd', 'a', ' ', 'S', 'i', 'l', 'v', 'a']