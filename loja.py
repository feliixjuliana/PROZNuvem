lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores'] 
print(lista_produtos, 'esse é o seu começo')


lista_produtos[1], lista_produtos[4] = 'rímel', 'cremes hidratantes'

lista_produtos.pop()

print(lista_produtos, 'Essa é a lista final')

#Desafio
lista_produtos.append('esfoliantes')
lista_produtos.append('esmaltes')
print(lista_produtos, 'adicionado dois novos produtos')