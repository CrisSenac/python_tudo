#Modifique o programa anterior para exibir qual deles é o menor número.

num = []
contador = 0
 
while contador < 3:
    numero = int(input("Digite um número: "))
    # num.append(numero)
    contador += 1
 
menor_numero = min(num)
print("Você digitou os números:", num)
print("O menor número é:", menor_numero)