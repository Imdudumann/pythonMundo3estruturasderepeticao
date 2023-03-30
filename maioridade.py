lista_maiores = []
lista_menores = []
ano_atual = 2023
for x in range(0,7):
    ano_nascimento = int(input('Digite o ano de nascimento: '))
    if ano_atual - ano_nascimento > 18:
        lista_maiores.append(ano_nascimento)
    elif ano_atual - ano_nascimento < 18:
        lista_menores.append(ano_nascimento)
print('Os maiores de idade são {} pessoas'.format(len(lista_maiores)))
print('Os menores de idade são {} pessoas'.format(len(lista_menores)))
