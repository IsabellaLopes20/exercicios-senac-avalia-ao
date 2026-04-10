#questao 22 da lista sequencial

salario_minimo = float(input("informe o valor do salario minimo: "))
quantidade_kw_por_residencia = float(input("informe a quantidade de kw consumida por residencia: "))
um_kw = 0.2 * salario_minimo
quantidade_em_real = quantidade_kw_por_residencia * um_kw
desconto = quantidade_em_real * 0.15
valor_desconto = quantidade_em_real - desconto
print(f"um_kw: {um_kw:.2f}")
print(f"quantidade_em_real: {quantidade_em_real:.2f}")
print(f"valor_desconto: {valor_desconto:.2f}")