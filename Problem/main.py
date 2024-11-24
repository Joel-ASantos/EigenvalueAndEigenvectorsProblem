import math
from sympy import symbols, solve

# Calculo do Determinante
def determinante_Matriz(M):
    if len(M) == 2:
        det = M[0][0] * M[1][1] - M[0][1] * M[1][0]
        return det
    else:
        det = 0
        for coluna in range(len(M)):
            sub_matrix = [linha[:coluna] + linha[coluna+1:] for linha in M[1:]]
            det += ((-1) ** coluna) * M[0][coluna] * determinante_Matriz(sub_matrix)
        return det
    
def autovalores(M):
    lamb = symbols('lambda')
    
    n = len(M)
    M_lambda = [] # Matriz - lambda
    
    for i in range(n):
        linha = []  # Linha atual da matriz
        for j in range(n):
            if i == j:
                value = M[i][j] - lamb
            else:
                value = M[i][j]
            linha.append(value)

        M_lambda.append(linha)
    
    det_M_lambda = determinante_Matriz(M_lambda)
    
    # Resolve o polinômio característico (det(A - lambda*I) = 0)
    autovalores = solve(det_M_lambda, lamb)
    return autovalores
    
    
# Matriz 4x4
M = [[2,0,4,2],
    [0,4,8,0],
    [0,0,2,2],
    [0,0,0,6]]

print(f"Determinante : {determinante_Matriz(M)}")
print(f"Autovalores : {autovalores(M)}")