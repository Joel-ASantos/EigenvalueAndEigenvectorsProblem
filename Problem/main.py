import math
from sympy import symbols,diff,simplify

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

# Matriz 4x4
M = [[2,0,4,2],
    [0,4,8,0],
    [0,0,2,2],
    [0,0,0,6]]

det_polinomio = polinomio(M)
print(f"Polinômio Caractéristico: {det_polinomio}")

# AutoValor
def autovalores(polinomio):
    lamb = symbols('lambda')
    coeficientes = polinomio.as_poly(lamb).all_coeffs()
    coeficientes = [float(c) for c in coeficientes]
    grau = len(coeficientes) - 1

    print(f"Coeficientes: {coeficientes}, Grau: {grau}")

    if grau == 1:
        a, b = coeficientes
        print("Resolvendo grau 1")
        return [-b / a]
    elif grau == 2:
        a, b, c = coeficientes
        print("Resolvendo grau 2")
        discriminante = b**2 - 4*a*c
        if discriminante < 0:
            return []
        elif discriminante == 0:
            return [-b / (2*a)]
        else:
            raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
            raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
            return [raiz1, raiz2]
    else:
        raizes = []
        d_polinomio = diff(polinomio, lamb)

        def newton_raphson(poly, d_poly, x0, tol=1e-6, max_iter=100):
            x = x0
            for i in range(max_iter):
                fx = poly.subs(lamb, x)
                dfx = d_poly.subs(lamb, x)
                print(f"Iteração {i}: x = {x}, f(x) = {fx}, f'(x) = {dfx}")
                if abs(dfx) < 1e-10:
                    break
                x_new = x - fx / dfx
                if abs(x_new - x) < tol:
                    print(f"Convergiu para: {x_new}")
                    return x_new
                x = x_new
            return x

        for i in range(grau):
            x0 = i + 1
            print(f"Procurando raiz {i+1} com x0 = {x0}")
            raiz = newton_raphson(polinomio, d_polinomio, x0)
            raiz = simplify(raiz)
            print(f"Raiz encontrada: {raiz}")
            raizes.append(raiz)

            polinomio = simplify(polinomio / (lamb - raiz))
            d_polinomio = diff(polinomio, lamb)
            print(f"Polinômio reduzido: {polinomio}")

        return raizes
autovalores_encontrados = autovalores(det_polinomio)
print(f"Autovalores: {autovalores_encontrados}")