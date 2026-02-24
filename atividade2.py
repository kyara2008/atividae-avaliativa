#Kyara Pontes Dassoglio
salario_atual = float(input(" Digite seu salário :"))
valor_aumento = float(input( "Digite o auemnto (%):"))
aumento = salario_atual * (valor_aumento/100)
novo_salario = salario_atual + aumento
print(f"Seu novo salário e de {valor_aumento}% R$ {novo_salario:}")