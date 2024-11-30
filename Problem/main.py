import os
from sympy import symbols, Matrix, simplify

# Função para calcular o determinante de uma matriz numérica
def determinante_matriz(M):
    if len(M) == 2:  # Caso base para matriz 2x2
        return M[0][0] * M[1][1] - M[0][1] * M[1][0]
    else:  # Expansão de Laplace
        det = 0
        for coluna in range(len(M)):
            sub_matriz = [linha[:coluna] + linha[coluna+1:] for linha in M[1:]]
            det += ((-1) ** coluna) * M[0][coluna] * determinante_matriz(sub_matriz)
        return det

# Função para construir a matriz (A - λI)
def A_menos_lambda(M, lamb):
    n = len(M)
    M_lambda = []
    for i in range(n):
        linha = []
        for j in range(n):
            if i == j:
                linha.append(M[i][j] - lamb)  # Subtração de λ na diagonal
            else:
                linha.append(M[i][j])
        M_lambda.append(linha)
    return Matrix(M_lambda)

# Função para gerar o polinômio característico
def polinomio_caracteristico(M):
    lamb = symbols('lambda')  # Definição do símbolo λ
    M_lambda = A_menos_lambda(M, lamb)  # Matriz (A - λI)
    det = M_lambda.det()  # Determinante de (A - λI) usando SymPy
    return simplify(det)  # Simplificação do polinômio

# Função para encontrar autovalores chutando valores inteiros
def encontrar_autovalores_por_chute(polinomio, intervalo):
    lamb = symbols('lambda')
    autovalores = []
    for valor in intervalo:
        resultado = polinomio.subs(lamb, valor)
        if resultado == 0:
            autovalores.append(valor)
            print(f"Autovalor encontrado: λ = {valor}")
    return autovalores

# Função para calcular os autovetores
def calcular_autovetores(M, autovalores):
    lamb = symbols('lambda')
    autovetores = {}
    for autovalor in autovalores:
        # Construir A - λI
        A_lambda = A_menos_lambda(M, autovalor)
        
        # Resolver o sistema (A - λI)v = 0
        null_space = A_lambda.nullspace()  # Espaço nulo da matriz
        if null_space:
            autovetores[autovalor] = null_space
        else:
            print(f"Não há autovetores para λ = {autovalor}")
    return autovetores

# Matriz 4x4
M = [[2, 0, 4, 2],
     [0, 4, 8, 0],
     [0, 0, 2, 2],
     [0, 0, 0, 6]]

# Gerando o polinômio característico
polinomio = polinomio_caracteristico(M)
print(f"\nPolinômio Característico: {polinomio}")

# Encontrando autovalores no intervalo de -100 a 100
intervalo_chutes = range(-100, 101)
autovalores = encontrar_autovalores_por_chute(polinomio, intervalo_chutes)
print(f"\nAutovalores encontrados: {autovalores}\n")

# Calculando autovetores
autovetores = calcular_autovetores(M, autovalores)


for autovalor, vetores in autovetores.items():
    print(f"Autovetores para λ = {autovalor}:")
    for vetor in vetores:
        print(vetor)
