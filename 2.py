def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def condicao_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Acima do peso"
    else:
        return "Obeso"

def main():
    print("Calculadora de IMC")
    
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))
    
    imc = calcular_imc(peso, altura)
    
    condicao = condicao_imc(imc)
    
    print(f"\nSeu IMC é: {imc:.2f}")
    print(f"Sua condição é: {condicao}")

if __name__ == "__main__":
    main()