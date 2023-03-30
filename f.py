listaNum = [1, 2, 3, 4, 5, 6, 7, 8, 9]
novaLista = []
for x in listaNum:
    print(x)
    if x % 2 == 0:
        novaLista.append(x)
print(novaLista)