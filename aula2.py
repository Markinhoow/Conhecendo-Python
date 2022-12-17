# Condicionais 
#if, elif e else
# ' ' ' em cima e embaixo é comentario em bloco
#elif so é executado caso os outros if's não tenham sido executados
'''
trabalho_terminado = True
if trabalho_terminado == True: 
  print ("opa, bora dar um rolê então")
else:
  print("vish, miou então")
'''


'''
estou_disponivel = False
if estou_disponivel == True: 
  print("Sim, posso ajudar")
else:
  print("Pede pro teu tio")
'''

'''
numero_de_atrasos = 1
if numero_de_atrasos >= 3 :
  print("Você está suspenso")
elif numero_de_atrasos == 1:
  print("Ok,pode entrar mas se chegar mais 2 vezes atrasdados, ja era")
elif numero_de_atrasos == 2:
  print("Ok, mas cuidado...você está na berlinda")
else:
  print("Entra")
'''

numero1 = input("Digite o primeiro numero:")
numero2 = input("Digite o segundo numero:")
if int(numero1)>int(numero2):
  print("O Primeiro numero é maior")
elif numero1 == numero2:
  print("Os numeros tem o mesmo peso")
else:
  print("O segundo numero é maior")