#Exercício 3
num = int(input('Digite um número inteiro positivo: '))
while num < 0:
    print('Número invalido')
    num = int(input('Digite um número inteiro positivo: '))
fatorial = 1
for i in range(1 , num +1):
        fatorial *= i
print(f'O fatorial de {num} é {fatorial}')