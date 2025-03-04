l=int(input('Digite a quantidade de litros vendidos: '))
t=float(input('Digite 1 para gasolina ou digite 2 se for álcool'))
if t==1 :
  print('Gasolina')
  if 20>=l :
    vr= l*5
    vd= vr*4/100
    vf=vr-vd
    print('O valor a ser pago é: ', vf)
  else:
    vr= l*5
    vd=vr*6/100
    vf=vr-vd
    print('O valor a ser pago é: ', vf)
if t==2 :
  print('Álcool')
  if 20>=l :
    vr=l*3
    vd=vr*3/100
    vf=vr-vd
    print('O valor a ser pago é: ', vf)
  else:
    vr= l*3
    vd=vr*5/100
    vf=vr-vd
    print('O valor a ser pago é: ', vf)
#vr = valor real, vd = valor com desconto, vf = valor final