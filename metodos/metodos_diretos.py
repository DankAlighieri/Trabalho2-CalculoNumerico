"""
MÉTODOS DIRETOS PARA SISTEMAS DE EQUAÇÕES LINEARES
Implementa: Eliminação de Gauss, Decomposição LU
"""

import numpy as np
from typing import Tuple, Optional


def eliminacao_gauss(A: np.ndarray, b: np.ndarray, pivoteamento: bool = True) -> np.ndarray:

    n = len(b)
    # Cria matriz aumentada
    Ab = np.column_stack([A.astype(float), b.astype(float)])
    
    # Fase de eliminação
    for k in range(n-1):
        # Pivoteamento parcial
        if pivoteamento:
            max_idx = np.argmax(np.abs(Ab[k:n, k])) + k
            if max_idx != k:
                Ab[[k, max_idx]] = Ab[[max_idx, k]]
        
        # Verifica pivô zero
        if abs(Ab[k, k]) < 1e-10:
            raise ValueError(f"Pivô zero encontrado na linha {k}")
        
        # Eliminação
        for i in range(k+1, n):
            fator = Ab[i, k] / Ab[k, k]
            Ab[i, k:] -= fator * Ab[k, k:]
    
    # Substituição regressiva
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (Ab[i, -1] - np.dot(Ab[i, i+1:n], x[i+1:n])) / Ab[i, i]
    
    return x

def decomposicao_lu(A: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:

    n = A.shape[0]
    L = np.eye(n)
    U = A.astype(float).copy()
    
    for k in range(n-1):
        if abs(U[k, k]) < 1e-10:
            raise ValueError(f"Pivô zero encontrado na posição ({k},{k})")
        
        for i in range(k+1, n):
            fator = U[i, k] / U[k, k]
            L[i, k] = fator
            U[i, k:] -= fator * U[k, k:]
    
    return L, U


def resolver_lu(L: np.ndarray, U: np.ndarray, b: np.ndarray) -> np.ndarray:

    n = len(b)
    
    # Resolve Ly = b (substituição progressiva)
    y = np.zeros(n)
    for i in range(n):
        y[i] = (b[i] - np.dot(L[i, :i], y[:i])) / L[i, i]
    
    # Resolve Ux = y (substituição regressiva)
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]
    
    return x

def teste_metodos_diretos():
    """Testa os métodos diretos com exemplos"""
    print("=" * 60)
    print("TESTE DOS MÉTODOS DIRETOS")
    print("=" * 60)
    
    # Sistema de exemplo
    A = np.array([[4, -1, 0, 0],
                  [-1, 4, -1, 0],
                  [0, -1, 4, -1],
                  [0, 0, -1, 3]], dtype=float)
    
    b = np.array([15, 10, 10, 10], dtype=float)
    
    print("\nSistema Linear:")
    print("A =")
    print(A)
    print("\nb =", b)
    
    # Eliminação de Gauss
    print("\n" + "-" * 60)
    print("1. ELIMINAÇÃO DE GAUSS")
    print("-" * 60)
    x_gauss = eliminacao_gauss(A.copy(), b.copy())
    print(f"Solução: {x_gauss}")
    print(f"Verificação Ax = {np.dot(A, x_gauss)}")
    print(f"Erro: {np.linalg.norm(np.dot(A, x_gauss) - b):.2e}")
    
    # Gauss-Jordan
    print("\n" + "-" * 60)
    print("2. GAUSS-JORDAN")
    print("-" * 60)
    x_gj = gauss_jordan(A.copy(), b.copy())
    print(f"Solução: {x_gj}")
    print(f"Verificação Ax = {np.dot(A, x_gj)}")
    print(f"Erro: {np.linalg.norm(np.dot(A, x_gj) - b):.2e}")
    
    # Decomposição LU
    print("\n" + "-" * 60)
    print("3. DECOMPOSIÇÃO LU")
    print("-" * 60)
    L, U = decomposicao_lu(A.copy())
    print("L =")
    print(L)
    print("\nU =")
    print(U)
    print(f"\nVerificação LU = A:")
    print(f"Erro: {np.linalg.norm(np.dot(L, U) - A):.2e}")
    
    x_lu = resolver_lu(L, U, b)
    print(f"\nSolução: {x_lu}")
    print(f"Erro: {np.linalg.norm(np.dot(A, x_lu) - b):.2e}")

if __name__ == "__main__":
    teste_metodos_diretos()
