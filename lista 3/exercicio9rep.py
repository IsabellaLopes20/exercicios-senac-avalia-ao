# exercicio 9 lista de repeticao

total_de_pessoas = int(input("Toatal de pessoas:"))
preço = 150
total_hotel = 0

for i in range(total_de_pessoas):
    nome = input("Nome do cliente:")
    diaria = float(input("Número de dias:"))

    if diaria < 15:
        taxa = 8 
    elif diaria == 15:
        taxa = 6.3
    else:
        taxa = 5


    conta = diaria * (preço + taxa)

    total_hotel = total_hotel + conta

    print(f"Cliente: {nome}")
    print(f"Conta: R$ {conta:.2f}")
print(f"Total ganho pelo hotel: R${total_hotel:.2f}")