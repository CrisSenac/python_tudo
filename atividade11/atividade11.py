#1-Construa programa que determine(imprima) se um dado número N inteiro é PAR ou IMPAR.

# numero = int(input("Digite um número inteiro: "))

# if numero % 2 == 0:  
#     print(f"O número {numero} é PAR.")
# else:
#     print(f"O número {numero} é ÍMPAR.")

#-----------------------------------------------------------------------

#2- Escreva um programa que leia um  número e informe se ele é divisivel por 10, 5 ou por 2, ou se não é divisivel por nenhum deles

# numero = int(input('Digite um número: '))
# if numero % 10 == 0:
#     print(f"O número {numero} é divisivel por 10")
# elif numero % 5 == 0:
#     print(f"O número {numero} é divisivel por 5")
# elif numero % 2 == 0:
#     print(f"O número {numero} é divisivel por 2")
# else:                                                                                                     
#     print(f"O número {numero} não é divisivel por 2, 5, nem 10")

#-----------------------------------------------------------------------

#3- Faça um algoritmo que dado o valor total em reais e o nú                                                                                                                                            mero de prestações desejadas, calcule o valor de cada prestação. O número mínimo de prestações deve ser 12. Se o número de prestações for maior ou igual a 24, adicione 10% de juros ao valor total, se for maior ou igual 36, adicione 15% de juros ao valor total.

# valor = float(input('Digite um número: '))

# prestacoes = int(input("Digite o número de prestações desejadas: "))
# if prestacoes < 12:
#                                                                                                                                                                       print("O número minimo de prestações é 12.")
#     prestacoes = 12
# if prestacoes >= 24 and prestacoes < 36:
#     valor += valor * 0.10
#     print("Será adicionado 10% de juros ao valor total.")
# elif prestacoes >= 36:
#     valor += valor * 0.15
# print("Será adiciondo 15% de juros ao valor total.")
# prestacoes = valor / prestacoes
# print("Valor de cada prestação será: ")

#outra forma de fazer:
 
valorTotal = float(input("Qual  valor da compra? "))
parcela = int(input("Quantas parcelas? "))
# juros = 0
if parcela < 12:
    print("Não pode emprestar!")
else : 
    if parcela >= 12 and parcela < 24:
        juros = 0
    elif parcela >= 24 and parcela < 36:
        juros = (valorTotal*10)/100
    elif parcela >= 36:
        juros = (valorTotal*15)/100

    valorTotal = valorTotal + juros
    valorParcela = valorTotal / parcela
    print(f"O valor a pagar é {valorParcela}")

