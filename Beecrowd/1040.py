lista = input().split()
num1 = float(lista[0])
num2 = float(lista[1])
num3 = float(lista[2])
num4 = float(lista[3])
pesonotas = 2+3+4+1
media = (num1 * 2 + num2 * 3 + num3 *4 + num4 * 1)/pesonotas
if media>=7.0 :
    print(f'Media: {media:.1f}')
    print('Aluno aprovado.')
elif media<5.0:
    print(f'Media: {media:.1f}')
    print('Aluno reprovado.')
elif media >= 5 and media <= 6.9:
    print('Media:', media)
    print('Aluno em exame.')
    notaexame = float(input())
    mediaexame = (notaexame + media)/2
    print(f'Nota do exame: {notaexame:.1f}')
    if mediaexame>=5.0:
        print('Aluno aprovado.')
        print(f'Media final: {mediaexame:.1f}')
        if mediaexame<5:
            print('Aluno reprovado.')
            print(f'Media final: {mediaexame:.1f}')