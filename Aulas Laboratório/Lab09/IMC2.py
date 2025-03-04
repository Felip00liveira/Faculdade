def calcular_imc(a, b):
    imc = a / (b**2)
    return imc
def determinar_categoria(a):
    if a < 18.5:
        a = 'Abaixo do peso'
        return a
    elif 18.5 <= a < 24.99:
         a ='Peso normal'
         return a
    elif 25.0 <= a < 29.99:
         a = 'Sobrepeso'
         return a
    elif 30.0 <= a < 34.99:
         a = 'Obesidade Grau 1'
         return a
    elif 35.0 <= a <39.99:
         a ='Obesidade Grau 2'
         return a
    else:
          a = 'Obesidade Grau 3 (mórbida)'
          return a
peso = int(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))
IMC = calcular_imc(peso, altura)
categoria = determinar_categoria(IMC)
print(f'Seu IMC é: {IMC:.2f}')
print(f'Categoria: {categoria}')