peso = float(input("Digite o peso do saco (kg) :"))
quantidade = float(input("Digite a quantidade para cada gato :"))
peso_gramas = peso * 1000
consumo_diario = quantidade * 2 
consumo_5_dias = consumo_diario * 5
restante = peso_gramas - consumo_5_dias
print("após 5 dias restará",restante,"gramas de ração.")
