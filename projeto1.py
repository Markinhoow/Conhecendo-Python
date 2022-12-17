# Fatorial de um número
'''
Criar um programa que recebe um número e imprime o seu fatorial
'''
numero = int (input("Digite o número que você deseja mostrar o fatorial:"))
if numero > 0:
  fatorial = 1
  for item in range(1,numero +1): #vai ser passado pra variavel item, o numero q irá rodar no laço de repetição
    fatorial = (fatorial * item)
  print(fatorial)
else:
   print("O numero digitado é invalido")