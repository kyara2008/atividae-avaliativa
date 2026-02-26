num1 = float(input("Digite o primeiro número:"))
num2 = float(input("Digite o segundo número:"))
num3 = float(input("Digite o terceiro número:"))

if num2 > num1 and num3 > num1:
    print(f"O menor número é {num1:g}")
else:
    if num1 > num2 and num3 > num2:
        print(f"O menor número é {num2:g}")
    else:  
      print(f"O menor número é {num3:g}")
