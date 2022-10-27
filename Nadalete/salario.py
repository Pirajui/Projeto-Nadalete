salario = float(input('Qual seu salario fixo: '))
vendas = float(input('Quantos de venda foi realizado: '))
vendas_temp = vendas

if vendas <= 99:
    vendas *= 0.05
else:
    vendas *= 0.05
    vendas += 0.07*(vendas_temp - 99)

final  = salario + vendas

print(final)