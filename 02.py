precouni = float(input("Qual o valor do produto? "))
quantidade = float(input("Quantos produtos foram comprados?"))
pagamento = float(input("Quanto de dinheiro foi recebido?"))

total = precouni * quantidade

if pagamento > total:
    troco = pagamento - total
    print(f"Seu troco e de {troco:g}reais")
else:
    print(f"Tchau:)")