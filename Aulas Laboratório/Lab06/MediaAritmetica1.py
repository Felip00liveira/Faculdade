soma = 0
contador = 0
while contador < 10:
  notas = int(input(f'Digite a {contador + 1}º nota: '))
  if notas < 1 or notas > 10:
    print('Número invalido')
  else:
    soma = soma + notas
    contador = contador + 1
  media = soma/10
print('A média aritmética é:',media)