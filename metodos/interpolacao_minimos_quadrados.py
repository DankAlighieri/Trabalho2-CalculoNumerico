"""
INTERPOLAÇÃO POLINOMIAL E MÍNIMOS QUADRADOS
Implementa: Interpolação de Lagrange, Newton, Ajuste de Mínimos Quadrados
"""

import numpy as np
from typing import Tuple, Callable
import matplotlib.pyplot as plt


def interpolacao_lagrange(x_pontos: np.ndarray, y_pontos: np.ndarray) -> Callable:
    """
    Cria função de interpolação usando polinômios de Lagrange
    
    Args:
        x_pontos: Pontos x conhecidos
        y_pontos: Valores f(x) conhecidos
    
    Returns:
        Função que interpola os pontos
    """
    n = len(x_pontos)
    
    def L(k: int, x: float) -> float:
        """Polinômio de Lagrange L_k(x)"""
        resultado = 1.0
        for i in range(n):
            if i != k:
                resultado *= (x - x_pontos[i]) / (x_pontos[k] - x_pontos[i])
        return resultado
    
    def P(x):
        """Polinômio interpolador P(x)"""
        if np.isscalar(x):
            return sum(y_pontos[k] * L(k, x) for k in range(n))
        else:
            return np.array([sum(y_pontos[k] * L(k, xi) for k in range(n)) for xi in x])
    
    return P


def diferencas_divididas(x_pontos: np.ndarray, y_pontos: np.ndarray) -> np.ndarray:
    """
    Calcula a tabela de diferenças divididas para interpolação de Newton
    
    Args:
        x_pontos: Pontos x conhecidos
        y_pontos: Valores f(x) conhecidos
    
    Returns:
        Tabela de diferenças divididas
    """
    n = len(x_pontos)
    tabela = np.zeros((n, n))
    tabela[:, 0] = y_pontos
    
    for j in range(1, n):
        for i in range(n - j):
            tabela[i, j] = (tabela[i+1, j-1] - tabela[i, j-1]) / (x_pontos[i+j] - x_pontos[i])
    
    return tabela


def interpolacao_newton(x_pontos: np.ndarray, y_pontos: np.ndarray) -> Tuple[Callable, np.ndarray]:
    """
    Cria função de interpolação usando polinômios de Newton
    
    Args:
        x_pontos: Pontos x conhecidos
        y_pontos: Valores f(x) conhecidos
    
    Returns:
        Função que interpola os pontos e tabela de diferenças divididas
    """
    tabela = diferencas_divididas(x_pontos, y_pontos)
    coeficientes = tabela[0, :]  # Primeira linha contém os coeficientes
    
    def P(x):
        """Polinômio interpolador de Newton P(x)"""
        if np.isscalar(x):
            resultado = coeficientes[0]
            produto = 1.0
            for i in range(1, len(coeficientes)):
                produto *= (x - x_pontos[i-1])
                resultado += coeficientes[i] * produto
            return resultado
        else:
            return np.array([P(xi) for xi in x])
    
    return P, coeficientes


def minimos_quadrados_linear(x_pontos: np.ndarray, y_pontos: np.ndarray) -> Tuple[float, float]:
    """
    Ajuste linear por mínimos quadrados: y = ax + b
    
    Args:
        x_pontos: Pontos x conhecidos
        y_pontos: Valores y conhecidos
    
    Returns:
        Coeficientes (a, b) da reta
    """
    n = len(x_pontos)
    soma_x = np.sum(x_pontos)
    soma_y = np.sum(y_pontos)
    soma_x2 = np.sum(x_pontos ** 2)
    soma_xy = np.sum(x_pontos * y_pontos)
    
    # Sistema normal
    a = (n * soma_xy - soma_x * soma_y) / (n * soma_x2 - soma_x ** 2)
    b = (soma_y - a * soma_x) / n
    
    return a, b


def minimos_quadrados_polinomial(x_pontos: np.ndarray, y_pontos: np.ndarray, 
                                  grau: int) -> np.ndarray:
    """
    Ajuste polinomial por mínimos quadrados: y = a_n*x^n + ... + a_1*x + a_0
    
    Args:
        x_pontos: Pontos x conhecidos
        y_pontos: Valores y conhecidos
        grau: Grau do polinômio
    
    Returns:
        Coeficientes do polinômio [a_0, a_1, ..., a_n]
    """
    n = len(x_pontos)
    m = grau + 1
    
    # Monta sistema normal: A^T * A * c = A^T * y
    A = np.zeros((n, m))
    for i in range(n):
        for j in range(m):
            A[i, j] = x_pontos[i] ** j
    
    # Resolve sistema normal
    ATA = np.dot(A.T, A)
    ATy = np.dot(A.T, y_pontos)
    coeficientes = np.linalg.solve(ATA, ATy)
    
    return coeficientes


def avaliar_polinomio(coeficientes: np.ndarray, x) -> np.ndarray:
    """
    Avalia polinômio com coeficientes dados
    
    Args:
        coeficientes: [a_0, a_1, ..., a_n]
        x: Ponto(s) para avaliar
    
    Returns:
        Valor(es) do polinômio
    """
    if np.isscalar(x):
        return sum(coeficientes[i] * x**i for i in range(len(coeficientes)))
    else:
        return np.array([sum(coeficientes[i] * xi**i for i in range(len(coeficientes))) 
                        for xi in x])


def calcular_erro_quadratico(y_real: np.ndarray, y_ajustado: np.ndarray) -> float:
    """
    Calcula o erro quadrático médio
    
    Args:
        y_real: Valores reais
        y_ajustado: Valores ajustados
    
    Returns:
        Erro quadrático médio
    """
    return np.sqrt(np.mean((y_real - y_ajustado) ** 2))


def coeficiente_determinacao(y_real: np.ndarray, y_ajustado: np.ndarray) -> float:
    """
    Calcula o coeficiente de determinação R²
    
    Args:
        y_real: Valores reais
        y_ajustado: Valores ajustados
    
    Returns:
        Coeficiente R² (0 a 1, quanto mais próximo de 1, melhor o ajuste)
    """
    y_media = np.mean(y_real)
    ss_tot = np.sum((y_real - y_media) ** 2)
    ss_res = np.sum((y_real - y_ajustado) ** 2)
    return 1 - (ss_res / ss_tot)


def teste_interpolacao_minimos_quadrados():
    """Testa os métodos de interpolação e mínimos quadrados"""
    print("=" * 60)
    print("TESTE DE INTERPOLAÇÃO E MÍNIMOS QUADRADOS")
    print("=" * 60)
    
    # Dados para interpolação
    x_interp = np.array([0, 1, 2, 3, 4])
    y_interp = np.array([1, 2.7, 5.8, 11, 18.2])
    
    print("\n" + "-" * 60)
    print("1. INTERPOLAÇÃO DE LAGRANGE")
    print("-" * 60)
    print(f"Pontos conhecidos:")
    for i in range(len(x_interp)):
        print(f"  ({x_interp[i]}, {y_interp[i]})")
    
    P_lagrange = interpolacao_lagrange(x_interp, y_interp)
    
    # Testa interpolação em pontos intermediários
    x_teste = np.array([0.5, 1.5, 2.5, 3.5])
    print(f"\nInterpolação em pontos intermediários:")
    for x_val in x_teste:
        print(f"  P({x_val}) = {P_lagrange(x_val):.4f}")
    
    print("\n" + "-" * 60)
    print("2. INTERPOLAÇÃO DE NEWTON")
    print("-" * 60)
    P_newton, coef_newton = interpolacao_newton(x_interp, y_interp)
    
    print("Coeficientes (diferenças divididas):")
    print(coef_newton)
    
    print(f"\nInterpolação em pontos intermediários:")
    for x_val in x_teste:
        print(f"  P({x_val}) = {P_newton(x_val):.4f}")
    
    # Verifica que Lagrange e Newton dão o mesmo resultado
    print(f"\nVerificação: Lagrange e Newton são equivalentes?")
    dif = np.max(np.abs(P_lagrange(x_teste) - P_newton(x_teste)))
    print(f"  Diferença máxima: {dif:.2e}")
    
    # Mínimos Quadrados
    print("\n" + "-" * 60)
    print("3. MÍNIMOS QUADRADOS - AJUSTE LINEAR")
    print("-" * 60)
    
    # Dados com ruído (não passam exatamente por uma reta)
    x_dados = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    y_dados = np.array([2.1, 3.9, 6.2, 8.1, 9.8, 12.3, 14.1, 16.2, 17.9, 20.1])
    
    print("Dados experimentais:")
    print(f"x = {x_dados}")
    print(f"y = {y_dados}")
    
    a, b = minimos_quadrados_linear(x_dados, y_dados)
    print(f"\nReta ajustada: y = {a:.4f}x + {b:.4f}")
    
    y_ajustado_linear = a * x_dados + b
    erro_linear = calcular_erro_quadratico(y_dados, y_ajustado_linear)
    r2_linear = coeficiente_determinacao(y_dados, y_ajustado_linear)
    
    print(f"Erro quadrático médio: {erro_linear:.4f}")
    print(f"R² = {r2_linear:.6f}")
    
    print("\n" + "-" * 60)
    print("4. MÍNIMOS QUADRADOS - AJUSTE POLINOMIAL")
    print("-" * 60)
    
    # Testa diferentes graus
    for grau in [2, 3]:
        print(f"\nPolinômio de grau {grau}:")
        coef = minimos_quadrados_polinomial(x_dados, y_dados, grau)
        
        # Monta string do polinômio
        termos = []
        for i in range(len(coef)-1, -1, -1):
            if i == 0:
                termos.append(f"{coef[i]:.4f}")
            elif i == 1:
                termos.append(f"{coef[i]:.4f}x")
            else:
                termos.append(f"{coef[i]:.4f}x^{i}")
        
        print(f"P(x) = {' + '.join(termos)}")
        
        y_ajustado = avaliar_polinomio(coef, x_dados)
        erro = calcular_erro_quadratico(y_dados, y_ajustado)
        r2 = coeficiente_determinacao(y_dados, y_ajustado)
        
        print(f"Erro quadrático médio: {erro:.4f}")
        print(f"R² = {r2:.6f}")
    
    print("\n" + "-" * 60)
    print("5. COMPARAÇÃO: INTERPOLAÇÃO vs AJUSTE")
    print("-" * 60)
    
    # Dados com alguns pontos
    x_comp = np.array([0, 1, 2, 3, 4])
    y_comp = np.array([1, 2, 1.5, 3, 5])
    
    print("Pontos de dados:")
    for i in range(len(x_comp)):
        print(f"  ({x_comp[i]}, {y_comp[i]})")
    
    # Interpolação (passa por todos os pontos)
    P_interp = interpolacao_lagrange(x_comp, y_comp)
    
    # Ajuste linear (minimiza erro quadrático)
    a_ajuste, b_ajuste = minimos_quadrados_linear(x_comp, y_comp)
    
    x_plot = np.array([0, 1, 2, 3, 4])
    print(f"\nComparação em x = {x_plot}:")
    print(f"{'x':<6} {'Dados':<10} {'Interpolação':<15} {'Ajuste Linear':<15}")
    print("-" * 50)
    for x_val in x_plot:
        idx = np.where(x_comp == x_val)[0]
        if len(idx) > 0:
            y_real = y_comp[idx[0]]
        else:
            y_real = None
        
        y_int = P_interp(x_val)
        y_aj = a_ajuste * x_val + b_ajuste
        
        if y_real is not None:
            print(f"{x_val:<6.1f} {y_real:<10.2f} {y_int:<15.4f} {y_aj:<15.4f}")
        else:
            print(f"{x_val:<6.1f} {'-':<10} {y_int:<15.4f} {y_aj:<15.4f}")


if __name__ == "__main__":
    teste_interpolacao_minimos_quadrados()
