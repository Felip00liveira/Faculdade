a = 0
b = 0
vetidade = []
c = True
while c:
    idade = int(input(''))
    if idade <= 0:
        c = False
    else:
       vetidade.append(idade)
       b += 1
    a += 1
soma = sum(vetidade)
total = soma/b
print(f'{total:.2f}')