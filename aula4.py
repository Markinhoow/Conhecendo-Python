# Coleções(listas)
preco_1 = 20
preco_2 = 50
preco_3 = 200
#listas
precos = [20,50,200]
#          0, 1, 2
print(precos[0])
print(precos.index(200)) #pede pro python ir até a lista e descobrir qual o indice do valor 

#Listas
diversidades = [15, 'jon', True]
print (diversidades[0])
print(diversidades[1])
print(diversidades[2])

#Laços em interáveis
for preco in precos:
  print(preco)

'''
#Exemplo - some os valores
Ddaos uma coleção de dados "idades" [15,46,75,34,23]
imprima na tela a soma desses valores
'''

idades = [15,46,75,34,23]
total = 0
for idade in idades:
  total = total + idade
print(total)
#valor temporario idade vai pra variavel, vai seguindo em ordem da coleção