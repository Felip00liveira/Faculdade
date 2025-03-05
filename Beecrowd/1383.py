def sudoku_valido(matriz):
    for i in range(9):
        if len(set(matriz[i])) != 9 or len(set(linha[i] for linha in matriz)) != 9:
            return False
    
    for linha_inicial in range(0, 9, 3):
        for coluna_inicial in range(0, 9, 3):
            regiao = []
            for r in range(3):
                for c in range(3):
                    regiao.append(matriz[linha_inicial + r][coluna_inicial + c])
            if len(set(regiao)) != 9:
                return False
    
    return True

n = int(input())
resultados = []

for instancia in range(1, n + 1):
    matriz = [list(map(int, input().split())) for _ in range(9)]
    if sudoku_valido(matriz):
        resultados.append(f"Instancia {instancia}\nSIM\n")
    else:
        resultados.append(f"Instancia {instancia}\nNAO\n")

print("\n".join(resultados))
