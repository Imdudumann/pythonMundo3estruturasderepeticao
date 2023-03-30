num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))
print('''Escolha um valor para iniciar o programa: 
[1] Somar
[2] Multiplicar
[3] Maior valor
[4] Novos números
[5] Sair do programa''')
escolha = int(input())
while escolha !=5:
    if escolha == 1:
        print('A soma de {} + {} é {}'.format(num1,num2,num1+num2))
        num1 = float(input('Digite o primeiro valor: '))
        num2 = float(input('Digite o segundo valor: '))
        print('''Escolha um valor para iniciar o programa: 
        [1] Somar
        [2] Multiplicar
        [3] Maior valor
        [4] Novos números
        [5] Sair do programa''')
        escolha = int(input())
