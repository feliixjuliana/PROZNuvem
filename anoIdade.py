def obter_ano():
    while True:
        try:
            ano = int(input("Digite seu ano de nascimento (entre 1922 e 2021): "))
            if 1922 < ano < 2021:
                return ano
            else:
                print("Ano incorreto, informe um ano entre 1922 e 2021.")
        except:
            print("Ano errado. Por favor, digite um número inteiro válido.")
    

nomeCompleto = input("Informe seu nome completo:")
anoNascimento = obter_ano()
idade = 2022 - anoNascimento

print("Sua idade, ", nomeCompleto, ", em 2022 será:", idade)
