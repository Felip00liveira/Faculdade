num1 = int(input(''))
num2 = int(input(''))
soma = 0
for i in range(num2+1, num1):
    if i %2 != 0:
        soma += i
print(soma)