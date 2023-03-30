n1= int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
escolha = int(input('Digite 1 para continuar e 2 para sair: '))
while escolha == 1:
    print('A soma de {} + {} = {}'.format(n1,n2,n1+n2))
    escolha = int(input('Digite 1 para continuar e 2 para sair: '))
    if escolha == 2:
        break
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
print('Seu programa terminou!')