num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
print('''Escolha um valor para iniciar o programa: 
[1] Somar
[2] Multiplicar
[3] Maior valor
[4] Novos números
[5] Sair do programa''')
escolha = int(input())
while escolha != 5:
    if escolha == 1:
        print('A soma de {} + {} = {}'.format(num1,num2,num1+num2))
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite outro número: '))
        print('''Escolha um valor para iniciar o programa: 
        [1] Somar
        [2] Multiplicar
        [3] Maior valor
        [4] Novos números
        [5] Sair do programa''')
        escolha = int(input())
    if escolha == 2:
        print('A multiplicação de {} x {} = {}'.format(num1,num2,num1*num2))
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite outro número: '))
        print('''Escolha um valor para iniciar o programa: 
        [1] Somar
        [2] Multiplicar
        [3] Maior valor
        [4] Novos números
        [5] Sair do programa''')
        escolha = int(input())
    if escolha == 3:
        if num1 > num2:
            print('O maior número é {}'.format(num1))
        else:
            print('O maior número é {}'.format(num2))
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite outro número: '))
        print('''Escolha um valor para iniciar o programa: 
        [1] Somar
        [2] Multiplicar
        [3] Maior valor
        [4] Novos números
        [5] Sair do programa''')
        escolha = int(input())
    if escolha == 4:
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite outro número: '))
        print('''Escolha um valor para iniciar o programa: 
        [1] Somar
        [2] Multiplicar
        [3] Maior valor
        [4] Novos números
        [5] Sair do programa''')
        escolha = int(input())
    if escolha == 5:
        print('Obrigado por utilizar nossos serviços!')
        break