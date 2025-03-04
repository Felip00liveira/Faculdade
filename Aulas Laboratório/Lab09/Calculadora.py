def soma(a,b):
    soma = a+b
    return soma
def sub (a,b):
    sub = a-b
    return sub
def multi(a,b):
    multi = a * b
    return multi
def divisao(a,b):
    if b == 0:
        print('O divisor não pode ser zero')
    else:
        divisao = a / b
        return divisao
print('Selecione a operação: ')
print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')
conta = int(input('Digite sua escolha (1/2/3/4): '))
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
if conta == 1:
    resultado = soma(num1, num2)
    print(f'{num1} + {num2} = {resultado}')
elif conta == 2:
    resultado = sub(num1, num2)
    print(f'{num1} - {num2} = {resultado}')
elif conta == 3:
    resultado = multi(num1, num2)
    print(f'{num1} × {num2} = {resultado}')
elif conta == 4:
    resultado =divisao(num1, num2)
    print(f'{num1} ÷ {num2} = {resultado}')
else:
    print('Número da operação invalido')