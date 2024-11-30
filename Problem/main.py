from sympy import symbols, simplify

# Função para calcular o determinante de uma matriz
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
        linha = [simplify(value) for value in linha]
        M_lambda.append(linha)
    return M_lambda

# Função para gerar o polinômio característico
def polinomio_caracteristico(M):
    lamb = symbols('lambda')  # Definição do símbolo λ
    M_lambda = A_menos_lambda(M, lamb)  # Matriz (A - λI)
    det = determinante_matriz(M_lambda)  # Determinante de (A - λI)
    return simplify(det)  # Simplificação do polinômio

# Função para encontrar raízes chutando valores inteiros
def encontrar_raizes_por_chute(polinomio, intervalo):
    lamb = symbols('lambda')
    raizes = []
    for valor in intervalo:
        resultado = polinomio.subs(lamb, valor)
        if resultado == 0:
            raizes.append(valor)
            print(f"Raiz encontrada: λ = {valor}")
    return raizes

# Matriz 4x4
M = [[2, 0, 4, 2],
     [0, 4, 8, 0],
     [0, 0, 2, 2],
     [0, 0, 0, 6]]

# Gerando o polinômio característico
polinomio = polinomio_caracteristico(M)
print(f"Polinômio Característico: {polinomio}")

# Encontrando raízes por chutes no intervalo 1 a 10
intervalo_chutes = range(-100, 100)  # Intervalo de valores para tentar
autovalores = encontrar_raizes_por_chute(polinomio, intervalo_chutes)
print(f"Autovalores encontrados: {autovalores}")
