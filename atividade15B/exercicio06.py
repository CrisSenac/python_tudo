#Adicione ao programa anterior a exibição do maior número digitado.

num = []
contador = 0
 
while contador < 3:
    numero = int(input("Digite um número: "))
    num.append(numero)
    contador += 1
 
menor_numero = min(num)
maior_numero = max(num)
 
print("Você digitou os números:", num)
print("O menor número é:", menor_numero)
print("O maior número é:", maior_numero)