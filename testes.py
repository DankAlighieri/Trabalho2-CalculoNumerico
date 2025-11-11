"""
TESTES RÁPIDOS - Validação dos Módulos
Este arquivo executa testes rápidos para verificar se tudo está funcionando
"""

import numpy as np
import sys

print("=" * 70)
print("TESTES RÁPIDOS DE VALIDAÇÃO")
print("=" * 70)

testes_passou = 0
testes_total = 0

def testar(nome, funcao, esperado=True):
    """Executa um teste e reporta o resultado"""
    global testes_passou, testes_total
    testes_total += 1
    try:
        resultado = funcao()
        if resultado or esperado is None:
            print(f"✓ {nome}")
            testes_passou += 1
            return True
        else:
            print(f"✗ {nome} - FALHOU")
            return False
    except Exception as e:
        print(f"✗ {nome} - ERRO: {e}")
        return False

# =============================================================================
# TESTE 1: Importações
# =============================================================================
print("\n" + "-" * 70)
print("TESTE 1: Verificando importações...")
print("-" * 70)

testar("NumPy", lambda: __import__('numpy') is not None)
testar("Matplotlib", lambda: __import__('matplotlib') is not None)
testar("Métodos Diretos", lambda: __import__('metodos_diretos') is not None)
testar("Métodos Iterativos", lambda: __import__('metodos_iterativos') is not None)
testar("Interpolação", lambda: __import__('interpolacao_minimos_quadrados') is not None)
testar("Integração", lambda: __import__('integracao_numerica') is not None)

# =============================================================================
# TESTE 2: Métodos Diretos
# =============================================================================
print("\n" + "-" * 70)
print("TESTE 2: Métodos Diretos...")
print("-" * 70)

import metodos_diretos as md

# Sistema simples: 2x = 4, y = 3
A_simples = np.array([[2, 0], [0, 1]], dtype=float)
b_simples = np.array([4, 3], dtype=float)

def teste_gauss():
    x = md.eliminacao_gauss(A_simples.copy(), b_simples.copy())
    return np.allclose(x, [2, 3])

def teste_gauss_jordan():
    x = md.gauss_jordan(A_simples.copy(), b_simples.copy())
    return np.allclose(x, [2, 3])

def teste_lu():
    L, U = md.decomposicao_lu(A_simples.copy())
    x = md.resolver_lu(L, U, b_simples)
    return np.allclose(x, [2, 3])

testar("Eliminação de Gauss", teste_gauss)
testar("Gauss-Jordan", teste_gauss_jordan)
testar("Decomposição LU", teste_lu)

# =============================================================================
# TESTE 3: Métodos Iterativos
# =============================================================================
print("\n" + "-" * 70)
print("TESTE 3: Métodos Iterativos...")
print("-" * 70)

import metodos_iterativos as mi

# Sistema diagonalmente dominante
A_iter = np.array([[4, 1], [1, 4]], dtype=float)
b_iter = np.array([5, 5], dtype=float)

def teste_jacobi():
    x, _, _ = mi.metodo_jacobi(A_iter, b_iter, tol=1e-6)
    return np.allclose(np.dot(A_iter, x), b_iter, rtol=1e-5)

def teste_gauss_seidel():
    x, _, _ = mi.metodo_gauss_seidel(A_iter, b_iter, tol=1e-6)
    return np.allclose(np.dot(A_iter, x), b_iter, rtol=1e-5)

def teste_sor():
    x, _, _ = mi.metodo_sor(A_iter, b_iter, omega=1.1, tol=1e-6)
    return np.allclose(np.dot(A_iter, x), b_iter, rtol=1e-5)

testar("Método de Jacobi", teste_jacobi)
testar("Método de Gauss-Seidel", teste_gauss_seidel)
testar("Método SOR", teste_sor)

# =============================================================================
# TESTE 4: Interpolação
# =============================================================================
print("\n" + "-" * 70)
print("TESTE 4: Interpolação...")
print("-" * 70)

import interpolacao_minimos_quadrados as imq

x_interp = np.array([0, 1, 2])
y_interp = np.array([0, 1, 4])  # y = x^2

def teste_lagrange():
    P = imq.interpolacao_lagrange(x_interp, y_interp)
    # Deve passar pelos pontos originais
    return np.allclose([P(0), P(1), P(2)], [0, 1, 4])

def teste_newton():
    P, _ = imq.interpolacao_newton(x_interp, y_interp)
    return np.allclose([P(0), P(1), P(2)], [0, 1, 4])

def teste_minimos_quadrados():
    x_data = np.array([0, 1, 2, 3, 4])
    y_data = np.array([1, 3, 5, 7, 9])  # y = 2x + 1
    a, b = imq.minimos_quadrados_linear(x_data, y_data)
    return np.allclose([a, b], [2, 1], rtol=0.1)

testar("Interpolação de Lagrange", teste_lagrange)
testar("Interpolação de Newton", teste_newton)
testar("Mínimos Quadrados Linear", teste_minimos_quadrados)

# =============================================================================
# TESTE 5: Integração Numérica
# =============================================================================
print("\n" + "-" * 70)
print("TESTE 5: Integração Numérica...")
print("-" * 70)

import integracao_numerica as intn

# Integral de x de 0 a 1 = 0.5
f_linear = lambda x: x

def teste_trapezio():
    resultado = intn.regra_trapezio(f_linear, 0, 1, n=100)
    return np.allclose(resultado, 0.5, rtol=1e-3)

def teste_simpson13():
    resultado = intn.regra_simpson_1_3(f_linear, 0, 1, n=100)
    return np.allclose(resultado, 0.5, rtol=1e-6)

def teste_simpson38():
    resultado = intn.regra_simpson_3_8(f_linear, 0, 1, n=99)
    return np.allclose(resultado, 0.5, rtol=1e-6)

def teste_gauss():
    resultado = intn.quadratura_gauss_2pontos(f_linear, 0, 1)
    return np.allclose(resultado, 0.5, rtol=1e-10)

testar("Regra do Trapézio", teste_trapezio)
testar("Regra de Simpson 1/3", teste_simpson13)
testar("Regra de Simpson 3/8", teste_simpson38)
testar("Quadratura de Gauss", teste_gauss)

# =============================================================================
# TESTE 6: Casos Especiais
# =============================================================================
print("\n" + "-" * 70)
print("TESTE 6: Casos Especiais e Validações...")
print("-" * 70)

def teste_matriz_identidade():
    I = np.eye(3)
    b = np.array([1, 2, 3])
    x = md.eliminacao_gauss(I, b)
    return np.allclose(x, b)

def teste_convergencia_diagonal():
    A = np.array([[10, 1], [1, 10]], dtype=float)
    return mi.verificar_convergencia_diagonal(A)

def teste_interpolacao_linear():
    x = np.array([0, 1])
    y = np.array([0, 1])
    P = imq.interpolacao_lagrange(x, y)
    return np.allclose(P(0.5), 0.5)

def teste_integral_constante():
    f = lambda x: 1
    resultado = intn.regra_trapezio(f, 0, 5, n=10)
    return np.allclose(resultado, 5, rtol=1e-6)

testar("Matriz Identidade", teste_matriz_identidade)
testar("Verificação Convergência", teste_convergencia_diagonal)
testar("Interpolação Linear", teste_interpolacao_linear)
testar("Integral de Constante", teste_integral_constante)

# =============================================================================
# TESTE 7: Precisão Numérica
# =============================================================================
print("\n" + "-" * 70)
print("TESTE 7: Precisão Numérica...")
print("-" * 70)

def teste_residuo_pequeno():
    A = np.array([[2, 1], [1, 2]], dtype=float)
    b = np.array([3, 3], dtype=float)
    x = md.eliminacao_gauss(A, b)
    residuo = np.linalg.norm(np.dot(A, x) - b)
    return residuo < 1e-10

def teste_r2_perfeito():
    x = np.array([1, 2, 3, 4, 5])
    y = 2 * x + 1  # Relação linear perfeita
    a, b = imq.minimos_quadrados_linear(x, y)
    y_ajustado = a * x + b
    r2 = imq.coeficiente_determinacao(y, y_ajustado)
    return np.allclose(r2, 1.0)

def teste_integral_polinomio():
    # Gauss 2 pontos integra exatamente polinômios de grau ≤ 3
    f = lambda x: x**3
    resultado = intn.quadratura_gauss_2pontos(f, 0, 1)
    exato = 0.25
    return np.allclose(resultado, exato, rtol=1e-10)

testar("Resíduo Pequeno", teste_residuo_pequeno)
testar("R² Perfeito", teste_r2_perfeito)
testar("Gauss exato para polinômios", teste_integral_polinomio)

# =============================================================================
# RELATÓRIO FINAL
# =============================================================================
print("\n" + "=" * 70)
print("RELATÓRIO FINAL")
print("=" * 70)
print(f"\nTestes executados: {testes_total}")
print(f"Testes aprovados:  {testes_passou}")
print(f"Testes falhados:   {testes_total - testes_passou}")
print(f"Taxa de sucesso:   {100 * testes_passou / testes_total:.1f}%")

if testes_passou == testes_total:
    print("\n✅ TODOS OS TESTES PASSARAM!")
    print("O projeto está funcionando corretamente.")
    print("\nVocê pode executar:")
    print("  python main.py      - Para a interface interativa")
    print("  python exemplos.py  - Para ver exemplos práticos")
else:
    print(f"\n⚠️  {testes_total - testes_passou} teste(s) falharam.")
    print("Verifique as mensagens de erro acima.")
    sys.exit(1)

print("\n" + "=" * 70)
