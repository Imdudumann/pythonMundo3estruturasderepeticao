l = []
n1 = 0
for x in range(0,167):
    x=x*3
    if x % 2 ==1:
        l.append(x)
soma = sum(l)
qte = len(l)
print('Ao todos são {} números e a sua soma é {}'.format(qte,soma))