#Exercício 03
soma = 0
import random
numero_secreto = random.randint(1, 100)
print('Adivinhe o número entre 1 e 100: ')
while soma<10:
  num=int(input('Digite seu número: '))
  if numero_secreto>num:
    print('O número é maior que', num)
  elif numero_secreto<num:
    print('O número é menor que', num)
  else:
    print('Parabéns! Você acertou o número', num)
    break
  soma += 1