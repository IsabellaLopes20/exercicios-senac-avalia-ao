# exercicio 20 lista condicional

valor1 = int(input("Informe o primeiro valor: "))
valor2 = int(input("Informe o segundo valor: "))

if valor1 % valor2 == 0 or valor2 % valor1 == 0:
    print("São múltiplos")
else:
    print("Não são múltiplos")