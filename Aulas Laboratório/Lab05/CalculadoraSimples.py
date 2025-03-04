print('Escolha uma operação matemática usando a tabela abaixo')
print('+ para adição')
print('- para subtração')
print('* para multiplicação')
print('/ para divição')
operacao = input('Digite sua escolha de operação: ') 
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
if operacao == '+':
    final = num1 + num2
if operacao == '-':
    final = num1 - num2
if operacao == '*':
    final = num1 * num2
if operacao == '/':
    final = num1 / num2
print(final)