listvalor = []
a = 1
while a<=100:
  num = int(input())
  listvalor.append(num)
  a += 1
maior = max(listvalor)
posicao = listvalor.index(maior)+1
print(maior)
print(posicao)