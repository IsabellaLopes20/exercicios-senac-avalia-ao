#questao 11 lista sequencial

preco_de_custo = float(input("Informe o preço de custo: "))
percentual = float(input("Informe o percentual de acréscimo: "))

valor_de_venda = preco_de_custo + (preco_de_custo * (percentual / 100))

print(f"Valor de venda: R$ {valor_de_venda:.2f}")