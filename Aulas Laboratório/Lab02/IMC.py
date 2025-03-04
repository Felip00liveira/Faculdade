import math
peso = float(input('Seu peso: '))
altura = float(input('Sua altura: '))
altura_quadrado=altura**2
imc=peso/altura_quadrado
print('Seu IMC é: ', imc)