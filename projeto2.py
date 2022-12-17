#Projeto - chute o numero
'''
Escreva um programa que, ao iniciar gera um valor aleatório de 1 a 10 e permite que o usuário chute um número até que o valor aleatório gerado no início do programa seja chutado corretamente.

O programa deve informar se o chute foi acima, abaixo ou igual ao valor aleatório gerado no início do programa.
'''
#gerar um valor aleatorio com a biblioteca random
import random

valor_aleatorio = random.randint(1, 10)
acertou = False
while acertou == False:
  numero = int(input("Chute um valor entre 1 a 10: "))
  if numero > valor_aleatorio:
    print("Valor maior que o valor gerado")
  elif numero < valor_aleatorio:
    print("Valor menor que valor gerado")
  elif numero == valor_aleatorio:
    acertou = True
    print("Parabéns!!! você acertou")
