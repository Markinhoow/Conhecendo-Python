# Laços de reptição + Listas
# maneiras de executar o mesmo comando varias vezes
for palavra in range(1,4): #em parenteses quer dizer de x até y, (1,4), ele nao inclui o ultimo numero(quantidade)
  print ('carregando')

   
'''
for item in coleção: 
  espressão
'''
''''
for item in range(1,21):
 print(item)
for item in range(1,20,2): #o ultimo numero é q quantidade de pulos q ele vai da, no caso de 2 em 2
 print(item)

nomes = ['jon', 'cris', 'roberto', 'camila']
for nome in nomes:
  print(nome)
'''

#Problema 1 a N - imprime os valores de 1 a N
valor_maximo= int(input('digite o valor maximo:'))
valor_inicial = 1
for numero in range(valor_inicial, valor_maximo + 1): #colocou o +1 para poder imprimir o valor final tambem
  print(numero)