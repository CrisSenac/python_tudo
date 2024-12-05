#Modifique o programa anterior para que o usuário determine qual o intervalo da contagem.

inicio = int(input("Digite o número inicial: "))
fim = int(input("Digite o número final: "))
 
num = inicio
 
while num <= fim:
    if num % 2 != 0:    
        print(num)
    num = num + 1