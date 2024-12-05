#Escreva um programa que pergunte ao usuário 3 números usando o while.

numeros = []
contador = 0
 
while contador < 3:
    numero = int(input("Digite um número: "))
    # numeros.append(numero)
    contador += 1
 
print("Você digitou os números:", numeros)