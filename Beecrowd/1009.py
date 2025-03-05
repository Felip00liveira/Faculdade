nome = input()
salario_fixo = float(input()) 
total_vendas = float(input())
salario_final = total_vendas * 0.15 + salario_fixo
print(f'TOTAL = R$ {salario_final:.2f}')