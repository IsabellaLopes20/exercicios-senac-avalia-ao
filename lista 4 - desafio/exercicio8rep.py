# exercicio 8 lista repetiçao

idades = []
alturas = []

#entrada de dados
for i in range(45):
    idade = int(input("Digite a idade: "))
    altura = float(input("Digite a altura: "))
    
    idades.append(idade)
    alturas.append(altura)

#idade média com altura < 1.70
soma_idade = 0
cont1 = 0

for i in range(45):
    if alturas[i] < 1.70:
        soma_idade += idades[i]
        cont1 += 1

if cont1 > 0:
    media_idade = soma_idade / cont1
    print("Idade média (altura < 1.70):", media_idade)
else:
    print("Nenhum aluno com altura < 1.70")

#altura média com idade > 20
soma_altura = 0
cont2 = 0

for i in range(45):
    if idades[i] > 20:
        soma_altura += alturas[i]
        cont2 += 1

if cont2 > 0:
    media_altura = soma_altura / cont2
    print("Altura média (idade > 20):", media_altura)
else:
    print("Nenhum aluno com mais de 20 anos")