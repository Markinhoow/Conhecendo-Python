#Variáveis

#Números
velocidade_internet = 10
print(velocidade_internet)
nota_filme = 8.5 #float = real
#Valores boleanos = logica
esta_aberto = True
#Strings
nome_do_dono_do_pc = 'Marco Antonio' #pode usar aspas simples ou duplas no python

#Como variáveis seriam usadas em um programada real?
#Problema 1 - valor por hora
#Escreva um programa que retorna o valor hora de um funcionário com base no seu salário mensal e horas trabalhadas por mês.
salario_mensal = input("quanto você recebe por mês?")
print(salario_mensal)
horas_trabalhadas_no_mes = input("quantas horas você trabalhou neste mês?")
print(horas_trabalhadas_no_mes)
valor_hora = int (salario_mensal) / int (horas_trabalhadas_no_mes)
print("O valor hora que você recebeu neste mês foi:", valor_hora)