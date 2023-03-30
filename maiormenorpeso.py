numPess = 1
lista_gordo = []
for x in range(0,6):
    peso = float(input('Digite o peso da {}º pessoa: '.format(numPess)))
    lista_gordo.append(peso)
    numPess+=1
print('A pessoa mais gorda da lista tem {} kg'.format(max(lista_gordo)))
print('A pessoa mais magra da lista tem {} kg!'.format(min(lista_gordo)))