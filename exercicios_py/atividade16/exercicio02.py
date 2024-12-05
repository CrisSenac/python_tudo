# Faça um Programa que peça as quatro notas de 3 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0

medias = []

for aluno in range(3):
    soma_notas = 0
    print(f"Aluno {aluno + 1}:")

    for nota in range(4):
        nota_atual = int(input(f"Digite a nota {nota + 1} : "))

    media = sum(medias) / 4
    medias.append(media)

alu_media_sete = 0
for media in medias:
    if media >= 7:
        alu_media_sete += 1


print(f"\nAlunos com média maior ou igual a 7: {alu_media_sete}")
