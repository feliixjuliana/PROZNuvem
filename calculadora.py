num1 = float(input("Informe um número: "))
num2 = float(input("Informe um segundo número: "))
fazer = int(input("Me informe o número do que deseja fazer:\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\nQual deseja? "))

if fazer == 1:
    soma = num1 + num2
    print(soma)

elif fazer == 2:
    subtracao = num1 - num2
    print(subtracao)

elif fazer == 3:
    multiplicao = num1 * num2
    print(multiplicao)

elif fazer == 4:
    divisao = num1 / num2
    print(divisao)

else:
    print("0")