def calculadora():

    while True:

      fazer = int(input("Me informe o número do que deseja fazer:\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n0 - Finalizar calculadora\nQual deseja? "))
      
      if fazer > 4:
        print("Escolha inválida, opte um número registrado na lista.")
        continue
    
      elif fazer == 0:
        print("Acabamos por aqui")
        break

      num1 = float(input("Informe um número: "))
      num2 = float(input("Informe um segundo número: "))

      if fazer == 1:
        resultado = num1 + num2
        print("Soma:", resultado)

      elif fazer == 2:
        resultado = num1 - num2
        print("Subtração:", resultado)

      elif fazer == 3:
        resultado = num1 * num2
        print("Multiplicação:", resultado)

      elif fazer == 4:
        resultado = num1 / num2
        print("Divisão:", resultado)

calculadora()