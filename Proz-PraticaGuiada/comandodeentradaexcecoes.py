def mostrar_numero(): #Função
    numeroEscolhido = int(input("Escreva um numero menor ou igual a 100: "))

    if(numeroEscolhido > 100):
      print("O número precisa ser menor ou igual a 100")

    else:
       print("Boa, você escolheu um número!!!!! Ele foi o", numeroEscolhido)


mostrar_numero()