l = []
for x in range(0,6):
    number = int(input('Digite um valor: '))
    if number % 2 == 0:
        l.append(number)
soma = sum(l)
print('A soma de todos os números pares é {}'.format(soma))
