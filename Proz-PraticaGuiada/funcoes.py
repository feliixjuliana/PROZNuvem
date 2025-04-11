def escrever_multiplicacao (num1,num2): #Definindo a função
        resultado = num1 * num2
        #resultado1 = str(num1) + " x " + str(num2) + " = " + str(resultado)
        return resultado #Retornando o resultado da função

print(escrever_multiplicacao(10, 11)) #Definindo os valores dos valores e imprimindo seu resultado sem salvar em uma variável

res = escrever_multiplicacao(10, 11)
print("O resultado da multiplicação foi", res)