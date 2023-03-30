maiorPeso = 0 #variavel que vai receber o maior peso
menorPeso = 0 #variavel que vai receber o menor peso
for pessoas in range(1,5):#laço de repetição com a variavel PESSOAS que vai perguntar o peso de 4 pessoas
  peso = float(input('Digite o peso da {}º pessoa: '.format(pessoas))) #variavel que vai receber o peso da 1º,2º,3º,4º pessoa
  if pessoas == 1: #a primeira pessoa sempre vai ser a mais pesada e tambem a mais leve
    maiorPeso = pessoas # a primeira pessoa que digitar o peso vai ser a mais pesada
    menorPeso = pessoas#a primeira pessoa que digitar o peso vai ser a a mais leve
  else: # se não for a primeira pessoa a mais pesada quando o loop passar de novo e essa segunda pessoa for a mais pesada, tanto quanto a mais leve
    if peso > maiorPeso: # se o peso for maior que o primeiro peso digitado no loop anterior
      maiorPeso = peso #a variavel que antes tinha o maior peso agora vai passar para segunda que tem o maior peso
    if peso < menorPeso:# se o peso da primeira pessoa do loop for menor
      menorPeso=peso#o menor peso agora vai passar a pertencer a segunda pessoa do loop que vai ter agora o menor peso
print('A pessoa mais pesada foi {}'.format(maiorPeso))
print('A pessoa mais magra foi {}'.format(menorPeso))