#você vai ter que fazer um programa que peça um número e depois por qual número esse primeiro número vai ser multiplicado, e no final mostrar de quantas em quantas casas esse número pulou!
primeiro_termo = int(input('Digite o primeiro termo: '))
razao_pa = int(input('Digite a razão dessa PA: '))
multiplicador = primeiro_termo*(10-1)
for x in range(primeiro_termo,multiplicador,razao_pa):
    print(x, end=' - ')