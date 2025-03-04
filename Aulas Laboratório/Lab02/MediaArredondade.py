import math
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
soma_notas = nota1+nota2
media_ponderada=soma_notas/2
media_arredondada=math.ceil(media_ponderada)
print('Sua média arredondada é:',media_arredondada)