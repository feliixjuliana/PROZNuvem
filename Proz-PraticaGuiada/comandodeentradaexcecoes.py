
"""
def mostrar_numero(): #Função
    numeroEscolhido = int(input("Escreva um numero menor ou igual a 100: "))

    if(numeroEscolhido > 100):
      print("O número precisa ser menor ou igual a 100")

    else:
       print("Boa, você escolheu um número!!!!! Ele foi o", numeroEscolhido)

mostrar_numero()
"""

"""
def mostrar_numero(): #Função com While para não pausar quando o usuário não colocou o número correto.
    numero_valido = False

    while(numero_valido == False):

      numeroEscolhido = int(input("Escreva um numero menor ou igual a 100: "))

      if(numeroEscolhido > 100):
        print("O número precisa ser menor ou igual a 100")

      else:
        print("Boa, você escolheu um número!!!!! Ele foi o", numeroEscolhido)
        numero_valido = True



mostrar_numero()
"""

def mostrar_numero(): #Função com Try/Except para identificar se o usuário colocou um tipo de dado diferente do que foi pedido
    numero_valido = False

    while(numero_valido == False):
      try:
          numeroEscolhido = int(input("Escreva um numero menor ou igual a 100: "))

          if(numeroEscolhido > 100):
            print("O número precisa ser menor ou igual a 100")

          else:
            print("Boa, você escolheu um número!!!!! Ele foi o", numeroEscolhido)
            numero_valido = True

      except:
            print("O valor inserido deve ser um número inteiro.")



mostrar_numero()