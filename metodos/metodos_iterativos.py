"""
MÉTODOS ITERATIVOS PARA SISTEMAS DE EQUAÇÕES LINEARES
Implementa: Jacobi, Gauss-Seidel, SOR (Successive Over-Relaxation)
"""

import numpy as np
from typing import Tuple, Optional


def verificar_convergencia_diagonal(A: np.ndarray) -> bool:
    """
    Verifica se a matriz é diagonalmente dominante
    (condição suficiente para convergência)
    
    Args:
        A: Matriz de coeficientes
    
    Returns:
        True se é diagonalmente dominante
    """
    n = A.shape[0]
    for i in range(n):
        diagonal = abs(A[i, i])
        soma_linha = sum(abs(A[i, j]) for j in range(n) if j != i)
        if diagonal <= soma_linha:
            return False
    return True


def metodo_jacobi(A: np.ndarray, b: np.ndarray, x0: Optional[np.ndarray] = None,
                  tol: float = 1e-6, max_iter: int = 1000) -> Tuple[np.ndarray, int, list]:
    """
    Resolve sistema linear Ax = b usando o método de Jacobi
    
    Args:
        A: Matriz de coeficientes (n x n)
        b: Vetor de termos independentes
        x0: Aproximação inicial (se None, usa vetor zero)
        tol: Tolerância para critério de parada
        max_iter: Número máximo de iterações
    
    Returns:
        x: Vetor solução
        num_iter: Número de iterações realizadas
        erros: Lista com histórico de erros
    """
    n = len(b)
    x = np.zeros(n) if x0 is None else x0.copy()
    x_new = np.zeros(n)
    erros = []
    
    for k in range(max_iter):
        for i in range(n):
            # Calcula soma de todos os termos exceto o diagonal
            soma = sum(A[i, j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - soma) / A[i, i]
        
        # Calcula erro relativo
        erro = np.linalg.norm(x_new - x) / np.linalg.norm(x_new)
        erros.append(erro)
        
        # Verifica convergência
        if erro < tol:
            return x_new, k + 1, erros
        
        x = x_new.copy()
    
    print(f"Aviso: Número máximo de iterações ({max_iter}) atingido")
    return x_new, max_iter, erros


def metodo_gauss_seidel(A: np.ndarray, b: np.ndarray, x0: Optional[np.ndarray] = None,
                        tol: float = 1e-6, max_iter: int = 1000) -> Tuple[np.ndarray, int, list]:
    """
    Resolve sistema linear Ax = b usando o método de Gauss-Seidel
    
    Args:
        A: Matriz de coeficientes (n x n)
        b: Vetor de termos independentes
        x0: Aproximação inicial (se None, usa vetor zero)
        tol: Tolerância para critério de parada
        max_iter: Número máximo de iterações
    
    Returns:
        x: Vetor solução
        num_iter: Número de iterações realizadas
        erros: Lista com histórico de erros
    """
    n = len(b)
    x = np.zeros(n) if x0 is None else x0.copy()
    x_old = x.copy()
    erros = []
    
    for k in range(max_iter):
        for i in range(n):
            # Usa valores já atualizados na iteração atual
            soma = sum(A[i, j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i] - soma) / A[i, i]
        
        # Calcula erro relativo
        erro = np.linalg.norm(x - x_old) / np.linalg.norm(x)
        erros.append(erro)
        
        # Verifica convergência
        if erro < tol:
            return x, k + 1, erros
        
        x_old = x.copy()
    
    print(f"Aviso: Número máximo de iterações ({max_iter}) atingido")
    return x, max_iter, erros


def metodo_sor(A: np.ndarray, b: np.ndarray, omega: float = 1.25,
               x0: Optional[np.ndarray] = None, tol: float = 1e-6,
               max_iter: int = 1000) -> Tuple[np.ndarray, int, list]:
    """
    Resolve sistema linear Ax = b usando o método SOR
    (Successive Over-Relaxation)
    
    Args:
        A: Matriz de coeficientes (n x n)
        b: Vetor de termos independentes
        omega: Fator de relaxação (1 < omega < 2 para sobre-relaxação)
        x0: Aproximação inicial (se None, usa vetor zero)
        tol: Tolerância para critério de parada
        max_iter: Número máximo de iterações
    
    Returns:
        x: Vetor solução
        num_iter: Número de iterações realizadas
        erros: Lista com histórico de erros
    """
    n = len(b)
    x = np.zeros(n) if x0 is None else x0.copy()
    x_old = x.copy()
    erros = []
    
    for k in range(max_iter):
        for i in range(n):
            # Calcula valor de Gauss-Seidel
            soma = sum(A[i, j] * x[j] for j in range(n) if j != i)
            x_gs = (b[i] - soma) / A[i, i]
            
            # Aplica fator de relaxação
            x[i] = omega * x_gs + (1 - omega) * x[i]
        
        # Calcula erro relativo
        erro = np.linalg.norm(x - x_old) / np.linalg.norm(x)
        erros.append(erro)
        
        # Verifica convergência
        if erro < tol:
            return x, k + 1, erros
        
        x_old = x.copy()
    
    print(f"Aviso: Número máximo de iterações ({max_iter}) atingido")
    return x, max_iter, erros


def calcular_residuo(A: np.ndarray, x: np.ndarray, b: np.ndarray) -> float:
    """
    Calcula o resíduo ||Ax - b||
    
    Args:
        A: Matriz de coeficientes
        x: Vetor solução
        b: Vetor de termos independentes
    
    Returns:
        Norma do resíduo
    """
    return np.linalg.norm(np.dot(A, x) - b)


def teste_metodos_iterativos():
    """Testa os métodos iterativos com exemplos"""
    print("=" * 60)
    print("TESTE DOS MÉTODOS ITERATIVOS")
    print("=" * 60)
    
    # Sistema de exemplo (diagonalmente dominante)
    A = np.array([[10, -1, 2, 0],
                  [-1, 11, -1, 3],
                  [2, -1, 10, -1],
                  [0, 3, -1, 8]], dtype=float)
    
    b = np.array([6, 25, -11, 15], dtype=float)
    
    print("\nSistema Linear:")
    print("A =")
    print(A)
    print("\nb =", b)
    
    # Verifica dominância diagonal
    if verificar_convergencia_diagonal(A):
        print("\n✓ A matriz é diagonalmente dominante (convergência garantida)")
    else:
        print("\n⚠ A matriz não é diagonalmente dominante")
    
    # Método de Jacobi
    print("\n" + "-" * 60)
    print("1. MÉTODO DE JACOBI")
    print("-" * 60)
    x_jacobi, iter_jacobi, erros_jacobi = metodo_jacobi(A, b, tol=1e-6)
    print(f"Solução: {x_jacobi}")
    print(f"Iterações: {iter_jacobi}")
    print(f"Resíduo final: {calcular_residuo(A, x_jacobi, b):.2e}")
    print(f"Erro final: {erros_jacobi[-1]:.2e}")
    
    # Método de Gauss-Seidel
    print("\n" + "-" * 60)
    print("2. MÉTODO DE GAUSS-SEIDEL")
    print("-" * 60)
    x_gs, iter_gs, erros_gs = metodo_gauss_seidel(A, b, tol=1e-6)
    print(f"Solução: {x_gs}")
    print(f"Iterações: {iter_gs}")
    print(f"Resíduo final: {calcular_residuo(A, x_gs, b):.2e}")
    print(f"Erro final: {erros_gs[-1]:.2e}")
    
    # Método SOR
    print("\n" + "-" * 60)
    print("3. MÉTODO SOR (ω = 1.1)")
    print("-" * 60)
    x_sor, iter_sor, erros_sor = metodo_sor(A, b, omega=1.1, tol=1e-6)
    print(f"Solução: {x_sor}")
    print(f"Iterações: {iter_sor}")
    print(f"Resíduo final: {calcular_residuo(A, x_sor, b):.2e}")
    print(f"Erro final: {erros_sor[-1]:.2e}")
    
    # Comparação
    print("\n" + "-" * 60)
    print("COMPARAÇÃO DE CONVERGÊNCIA")
    print("-" * 60)
    print(f"{'Método':<20} {'Iterações':<12} {'Resíduo':<15}")
    print("-" * 60)
    print(f"{'Jacobi':<20} {iter_jacobi:<12} {calcular_residuo(A, x_jacobi, b):<15.2e}")
    print(f"{'Gauss-Seidel':<20} {iter_gs:<12} {calcular_residuo(A, x_gs, b):<15.2e}")
    print(f"{'SOR (ω=1.1)':<20} {iter_sor:<12} {calcular_residuo(A, x_sor, b):<15.2e}")
    
    # Teste com diferentes valores de omega para SOR
    print("\n" + "-" * 60)
    print("4. TESTE SOR COM DIFERENTES ω")
    print("-" * 60)
    omegas = [0.5, 0.8, 1.0, 1.2, 1.5, 1.8]
    print(f"{'ω':<10} {'Iterações':<12} {'Resíduo':<15}")
    print("-" * 60)
    for omega in omegas:
        x_sor_test, iter_test, _ = metodo_sor(A, b, omega=omega, tol=1e-6)
        residuo_test = calcular_residuo(A, x_sor_test, b)
        print(f"{omega:<10.1f} {iter_test:<12} {residuo_test:<15.2e}")


if __name__ == "__main__":
    teste_metodos_iterativos()
