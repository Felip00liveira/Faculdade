#Exercício 02
conta = 0
tentativas = 5
while conta <5:
  senha=input('Digite a senha: ')
  if senha == 'Python123':
    print('Acesso concedido!')
    break
  print(f'Senha incorreta. Tentativas restantes: {tentativas - 1}')
  tentativas -= 1
  conta += 1