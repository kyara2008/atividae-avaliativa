tempo = float(input("Qual o tempo (em minutos) telefonado?"))

conta = 50
if tempo > 100:
    conta2 =  conta + ((tempo-100)*2)
    print(f"Sua conta ficara por {conta2}")
else:
    print(f"Sua conta ficara por {conta}")