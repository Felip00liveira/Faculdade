#Exercício 01
soma_positivos = 0
while True:
  num = int(input('Digite números inteiros: '))
  soma = num + num
  if num == -1:
    break
  elif num > 0:
    soma_positivos += num
  else:
    continue
print(f'A soma dos números positivos é {soma_positivos}')