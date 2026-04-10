# exercicio 14 lista condicional
diarias = int(input("Informe o número de diárias: "))
valor_diaria = 80


if diarias > 15:
    taxa = 5.50
elif diarias == 15:
    taxa = 6.00
else:
    taxa = 8.00


total = diarias * (valor_diaria + taxa)

print(f"Valor total: R$ {total:.2f}")