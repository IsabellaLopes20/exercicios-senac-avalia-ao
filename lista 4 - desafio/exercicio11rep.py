# exercicio 11 lista repetiçao

termo = 3
pg = []
soma = 0

while termo <= 6561:
    pg.append(termo)
    soma += termo
    termo *= 3

print("Termos:", pg)
print("Soma:", soma)