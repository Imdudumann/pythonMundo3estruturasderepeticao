from random import randint


numRandomico = randint(1,10)
tentativas = 0
minhaTentativa = int(input('Digite um número para saber se acertou: '))
while minhaTentativa != numRandomico:
    tentativas+=1
    minhaTentativa = int(input('Digite outro número: '))
print('você escolheu {} e o computador escolheu {}'.format(minhaTentativa,numRandomico))
print('Você tentou {} vezes até acertar'.format(tentativas))