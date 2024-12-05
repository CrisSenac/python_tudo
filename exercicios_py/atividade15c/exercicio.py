# Crie um programa que solicite ao usuário um número inteiro n e imprima um quadrado de asteriscos (*) de tamanho n x n.


n = int(input("Digite um número inteiro para o tamanho do quadrado: "))

for i in range(n):
    print('* ' * n)
