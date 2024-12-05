# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

lista_consoantes = []
lista_vogais = ['a','e','i','o','u']

for n in range(10):
    v = (input('Digite um caractere: '))
    if not v in lista_vogais:
        lista_consoantes.append(v)
    

    print(f"Foram lidas {lista_consoantes} consoantes")


#     lista_consoantes = []
#     lista_vogais = []


# for i in range(10):
#     i = input()