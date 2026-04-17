#exercicio 11 lista repeticao

def soma_pg():
    termo = 3
    soma = 0

    while termo <= 6561:
        soma += termo
        termo *= 3  # gera o próximo termo

    return soma


resultado = soma_pg()
print("Soma dos termos:", resultado)