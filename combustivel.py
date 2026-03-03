combustivel = input("para gasolina digite G para alcool digite A: ")
litros = float(input("quantos litros foram abastecidos? "))
preco = float(input("qual o preço do combustivel escolhido? "))

if combustivel == "A":
    if litros >= 20:
        valor = litros * (preco * 0.95)
    else:
        valor = litros * (preco * 0.97)
elif combustivel == "G":
    if litros >= 20:
        valor = litros * (preco * 0.94)
    else:
        valor = litros * (preco * 0.96)

print("O valor a pagar é", valor)