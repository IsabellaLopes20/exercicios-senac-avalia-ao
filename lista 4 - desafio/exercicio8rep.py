#exercicio 8 lista repeticao

class Aluno:
    def __init__(self, idade, altura):
        self.idade = idade
        self.altura = altura


# criando lista com 45 alunos (exemplo fixo)
alunos = [
    Aluno(18, 1.65), Aluno(22, 1.72), Aluno(19, 1.68),
    Aluno(25, 1.80), Aluno(21, 1.75)
] * 9  


# idade média dos alunos com altura < 1.70
soma_idade = 0
cont1 = 0

for aluno in alunos:
    if aluno.altura < 1.70:
        soma_idade += aluno.idade
        cont1 += 1

if cont1 > 0:
    media_idade = soma_idade / cont1
else:
    media_idade = 0


#altura média dos alunos com idade > 20
soma_altura = 0
cont2 = 0

for aluno in alunos:
    if aluno.idade > 20:
        soma_altura += aluno.altura
        cont2 += 1

if cont2 > 0:
    media_altura = soma_altura / cont2
else:
    media_altura = 0


print("Média das idades (altura < 1.70):", media_idade)
print("Média das alturas (idade > 20):", media_altura)