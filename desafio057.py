sexo = str(input('Digite M para masculino e F para feminino: ')).upper()
while sexo != 'M' or sexo != 'F':
    print('Sexo invalido!')
    sexo =str(input('Digite M para masculino e F para feminino: ')).upper()
    if sexo == 'M':
        print('Sexo masculino registrado com sucesso!')
        break
    if sexo == 'F':
        print('Sexo feminino registrado com sucesso!')
        break