print('Bem-vindo ao Hipermercado Real')
print('Patinho 1')
print('Contra filé 2')
print('Filé mignon 3')
tipo_carne=int(input('Digite o tipo de carne comprado senguindo a tabela: '))
quantidade=float(input('Digite a quantidade em Kg comprada: '))
forma_pagamento=(int(input('Digite 1 se possuir o cartão real: ')))
if tipo_carne==1 :
  if quantidade<=5 :
    vr=quantidade*5.80
    tipo_carne='Patinho'
  else:
    vr=quantidade*4.90
    tipo_carne='Patinho'
elif tipo_carne==2 :
  if quantidade<=5 :
    vr=quantidade*6.80
    tipo_carne='Contra filé'
  else:
    vr=quantidade*5.90
    tipo_carne='Contra filé'
elif tipo_carne==3:
  if quantidade<=5 :
    vr=quantidade*7.80
    tipo_carne='Filé mignon'
  else:
    vr=quantidade*6.90
    tipo_carne='Filé mignon'
if forma_pagamento==1 :
  vd=vr*5/100
  vf=vr-vd
  tp='Cartão real'
else:
  vd=0
  vf=vr
  tp='Outra forma de pagamento'
print('Tipo de carne ', tipo_carne)
print('Quantidade de carne ', quantidade, 'Kg')
print('Preço total ', vr)
print('Tipo de pagamento', tp)
print('Valor do desconto ',vd)
print('Valor a pagar', vf)
#vr = valor real, vd = valor com desconto, vf = valor final