ano_nacimento = int(input(" Digite seu ano de nacimento :"))
ano_atual = int(input(" Digite o ano atual :"))
idade_anos = ano_atual - ano_nacimento
idade_meses = idade_anos * 12 
idade_dias = idade_anos * 365
idade_semanas = idade_dias // 7
print(f" A idade da pessoa em anos : {idade_anos} anos")
print(f" A idade da pessoa em meses: {idade_meses} meses")
print(f" A idade da pessoa em dias {idade_dias} dias")
print (f" A idade da pessoa em semanas {idade_semanas} semanas")