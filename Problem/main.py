import math
from sympy import symbols

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
    
def A_Menos_lambda(M,lamb):
    n = len(M)
    M_lambda = []
    
    for i in range(n):
        linha = []
        for j in range(n):
            if i == j:
                value = M[i][j]-lamb
            else:
                value = M[i][j]
            linha.append(value)
        M_lambda.append(linha)
    return M_lambda

def polinomio(M):
    lamb = symbols('lambda')
    M_lambda = A_Menos_lambda(M,lamb)
    det_MLambda = determinante_Matriz(M_lambda)
    return det_MLambda

# Matriz 4x4 to
M = [[2,0,4,2],
    [0,4,8,0],
    [0,0,2,2],
    [0,0,0,6]]

det_polinomio = polinomio(M)
print(f"Polinômio Caractéristico: {det_polinomio}")

# AutoValor
def autovalor():
    print()