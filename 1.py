def calcular_valor(preco, condicao_pagamento):
    if condicao_pagamento == 1:
        return preco * 0.90
    elif condicao_pagamento == 2:
        return preco * 0.85
    elif condicao_pagamento == 3:
        return preco
    elif condicao_pagamento == 4:
        return preco * 1.10
    else:
        return "Código de condição de pagamento inválido"

def main():
    print("Bem-vindo ao calculador de pagamento!")
    
    preco = float(input("Digite o preço do produto: R$ "))
    
    print("\nEscolha a condição de pagamento:")
    print("1 - À vista em dinheiro ou cheque (10% de desconto)")
    print("2 - À vista no cartão de crédito (15% de desconto)")
    print("3 - Em duas vezes, preço normal de etiqueta")
    print("4 - Em duas vezes, preço normal com juros de 10%")
    
    condicao_pagamento = int(input("Digite o código da condição de pagamento: "))
    
    valor_final = calcular_valor(preco, condicao_pagamento)
    
    if isinstance(valor_final, float):
        print(f"\nO valor a ser pago é: R$ {valor_final:.2f}")
    else:
        print(valor_final)

if __name__ == "__main__":
    main()