# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

num = []

for i in range(5):
    valor = int(input(f"Digite o número {i+1}: "))
    num.append(valor)  

soma = 0
multiplicacao = 1

for numero in num:
    soma += numero  
    multiplicacao *= numero 

print(f"Números digitados: {num}")
print(f"Soma dos números: {soma}")
print(f"Multiplicação dos números: {multiplicacao}")

