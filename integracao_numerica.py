"""
INTEGRAÇÃO NUMÉRICA
Implementa: Regra do Trapézio, Regra de Simpson (1/3 e 3/8), Quadratura de Gauss
"""

import numpy as np
from typing import Callable, Tuple
import math


def regra_trapezio(f: Callable, a: float, b: float, n: int = 1) -> float:
    """
    Integração numérica usando a Regra do Trapézio
    
    Args:
        f: Função a ser integrada
        a: Limite inferior
        b: Limite superior
        n: Número de subintervalos
    
    Returns:
        Aproximação da integral
    """
    h = (b - a) / n
    soma = (f(a) + f(b)) / 2
    
    for i in range(1, n):
        x = a + i * h
        soma += f(x)
    
    return h * soma


def regra_trapezio_composta(f: Callable, a: float, b: float, n: int) -> Tuple[float, list]:
    """
    Regra do Trapézio Composta com diferentes números de subintervalos
    
    Args:
        f: Função a ser integrada
        a: Limite inferior
        b: Limite superior
        n: Número máximo de subintervalos
    
    Returns:
        Aproximação final e lista de aproximações intermediárias
    """
    aproximacoes = []
    for i in range(1, n+1):
        aprox = regra_trapezio(f, a, b, i)
        aproximacoes.append((i, aprox))
    
    return aproximacoes[-1][1], aproximacoes


def regra_simpson_1_3(f: Callable, a: float, b: float, n: int = 2) -> float:
    """
    Integração numérica usando a Regra de Simpson 1/3
    
    Args:
        f: Função a ser integrada
        a: Limite inferior
        b: Limite superior
        n: Número de subintervalos (deve ser par)
    
    Returns:
        Aproximação da integral
    """
    if n % 2 != 0:
        raise ValueError("n deve ser par para a Regra de Simpson 1/3")
    
    h = (b - a) / n
    soma = f(a) + f(b)
    
    # Soma dos termos ímpares (coeficiente 4)
    for i in range(1, n, 2):
        x = a + i * h
        soma += 4 * f(x)
    
    # Soma dos termos pares (coeficiente 2)
    for i in range(2, n, 2):
        x = a + i * h
        soma += 2 * f(x)
    
    return (h / 3) * soma


def regra_simpson_3_8(f: Callable, a: float, b: float, n: int = 3) -> float:
    """
    Integração numérica usando a Regra de Simpson 3/8
    
    Args:
        f: Função a ser integrada
        a: Limite inferior
        b: Limite superior
        n: Número de subintervalos (deve ser múltiplo de 3)
    
    Returns:
        Aproximação da integral
    """
    if n % 3 != 0:
        raise ValueError("n deve ser múltiplo de 3 para a Regra de Simpson 3/8")
    
    h = (b - a) / n
    soma = f(a) + f(b)
    
    for i in range(1, n):
        x = a + i * h
        if i % 3 == 0:
            soma += 2 * f(x)
        else:
            soma += 3 * f(x)
    
    return (3 * h / 8) * soma


def quadratura_gauss_2pontos(f: Callable, a: float, b: float) -> float:
    """
    Quadratura de Gauss com 2 pontos
    
    Args:
        f: Função a ser integrada
        a: Limite inferior
        b: Limite superior
    
    Returns:
        Aproximação da integral
    """
    # Pontos e pesos para 2 pontos
    pontos = [-1/np.sqrt(3), 1/np.sqrt(3)]
    pesos = [1.0, 1.0]
    
    # Transformação de [a,b] para [-1,1]
    def g(t):
        x = ((b - a) * t + (b + a)) / 2
        return f(x)
    
    integral = 0
    for i in range(2):
        integral += pesos[i] * g(pontos[i])
    
    return ((b - a) / 2) * integral


def quadratura_gauss_3pontos(f: Callable, a: float, b: float) -> float:
    """
    Quadratura de Gauss com 3 pontos
    
    Args:
        f: Função a ser integrada
        a: Limite inferior
        b: Limite superior
    
    Returns:
        Aproximação da integral
    """
    # Pontos e pesos para 3 pontos
    pontos = [-np.sqrt(3/5), 0, np.sqrt(3/5)]
    pesos = [5/9, 8/9, 5/9]
    
    # Transformação de [a,b] para [-1,1]
    def g(t):
        x = ((b - a) * t + (b + a)) / 2
        return f(x)
    
    integral = 0
    for i in range(3):
        integral += pesos[i] * g(pontos[i])
    
    return ((b - a) / 2) * integral


def quadratura_gauss_4pontos(f: Callable, a: float, b: float) -> float:
    """
    Quadratura de Gauss com 4 pontos
    
    Args:
        f: Função a ser integrada
        a: Limite inferior
        b: Limite superior
    
    Returns:
        Aproximação da integral
    """
    # Pontos e pesos para 4 pontos
    x1 = np.sqrt(3/7 - (2/7)*np.sqrt(6/5))
    x2 = np.sqrt(3/7 + (2/7)*np.sqrt(6/5))
    
    w1 = (18 + np.sqrt(30)) / 36
    w2 = (18 - np.sqrt(30)) / 36
    
    pontos = [-x2, -x1, x1, x2]
    pesos = [w2, w1, w1, w2]
    
    # Transformação de [a,b] para [-1,1]
    def g(t):
        x = ((b - a) * t + (b + a)) / 2
        return f(x)
    
    integral = 0
    for i in range(4):
        integral += pesos[i] * g(pontos[i])
    
    return ((b - a) / 2) * integral


def erro_integracao(aproximado: float, exato: float) -> Tuple[float, float]:
    """
    Calcula erro absoluto e relativo
    
    Args:
        aproximado: Valor aproximado da integral
        exato: Valor exato da integral
    
    Returns:
        Erro absoluto e erro relativo percentual
    """
    erro_abs = abs(exato - aproximado)
    erro_rel = (erro_abs / abs(exato)) * 100 if exato != 0 else float('inf')
    return erro_abs, erro_rel


def teste_integracao_numerica():
    """Testa os métodos de integração numérica"""
    print("=" * 60)
    print("TESTE DE INTEGRAÇÃO NUMÉRICA")
    print("=" * 60)
    
    # Exemplo 1: Integral simples
    print("\n" + "-" * 60)
    print("EXEMPLO 1: ∫₀² x² dx")
    print("-" * 60)
    
    f1 = lambda x: x**2
    a1, b1 = 0, 2
    integral_exata_1 = 8/3  # = 2.666...
    
    print(f"Integral exata: {integral_exata_1:.10f}")
    print(f"\n{'Método':<30} {'Aproximação':<15} {'Erro Abs':<12} {'Erro Rel %':<12}")
    print("-" * 60)
    
    # Trapézio
    aprox_trap = regra_trapezio(f1, a1, b1, n=10)
    erro_abs, erro_rel = erro_integracao(aprox_trap, integral_exata_1)
    print(f"{'Trapézio (n=10)':<30} {aprox_trap:<15.10f} {erro_abs:<12.2e} {erro_rel:<12.4f}")
    
    # Simpson 1/3
    aprox_simp13 = regra_simpson_1_3(f1, a1, b1, n=10)
    erro_abs, erro_rel = erro_integracao(aprox_simp13, integral_exata_1)
    print(f"{'Simpson 1/3 (n=10)':<30} {aprox_simp13:<15.10f} {erro_abs:<12.2e} {erro_rel:<12.4f}")
    
    # Simpson 3/8
    aprox_simp38 = regra_simpson_3_8(f1, a1, b1, n=9)
    erro_abs, erro_rel = erro_integracao(aprox_simp38, integral_exata_1)
    print(f"{'Simpson 3/8 (n=9)':<30} {aprox_simp38:<15.10f} {erro_abs:<12.2e} {erro_rel:<12.4f}")
    
    # Gauss
    aprox_gauss2 = quadratura_gauss_2pontos(f1, a1, b1)
    erro_abs, erro_rel = erro_integracao(aprox_gauss2, integral_exata_1)
    print(f"{'Gauss 2 pontos':<30} {aprox_gauss2:<15.10f} {erro_abs:<12.2e} {erro_rel:<12.4f}")
    
    aprox_gauss3 = quadratura_gauss_3pontos(f1, a1, b1)
    erro_abs, erro_rel = erro_integracao(aprox_gauss3, integral_exata_1)
    print(f"{'Gauss 3 pontos':<30} {aprox_gauss3:<15.10f} {erro_abs:<12.2e} {erro_rel:<12.4f}")
    
    # Exemplo 2: Função trigonométrica
    print("\n" + "-" * 60)
    print("EXEMPLO 2: ∫₀^π sin(x) dx")
    print("-" * 60)
    
    f2 = lambda x: np.sin(x)
    a2, b2 = 0, np.pi
    integral_exata_2 = 2.0
    
    print(f"Integral exata: {integral_exata_2:.10f}")
    print(f"\n{'Método':<30} {'Aproximação':<15} {'Erro Abs':<12} {'Erro Rel %':<12}")
    print("-" * 60)
    
    aprox_trap = regra_trapezio(f2, a2, b2, n=10)
    erro_abs, erro_rel = erro_integracao(aprox_trap, integral_exata_2)
    print(f"{'Trapézio (n=10)':<30} {aprox_trap:<15.10f} {erro_abs:<12.2e} {erro_rel:<12.4f}")
    
    aprox_simp13 = regra_simpson_1_3(f2, a2, b2, n=10)
    erro_abs, erro_rel = erro_integracao(aprox_simp13, integral_exata_2)
    print(f"{'Simpson 1/3 (n=10)':<30} {aprox_simp13:<15.10f} {erro_abs:<12.2e} {erro_rel:<12.4f}")
    
    aprox_simp38 = regra_simpson_3_8(f2, a2, b2, n=9)
    erro_abs, erro_rel = erro_integracao(aprox_simp38, integral_exata_2)
    print(f"{'Simpson 3/8 (n=9)':<30} {aprox_simp38:<15.10f} {erro_abs:<12.2e} {erro_rel:<12.4f}")
    
    aprox_gauss4 = quadratura_gauss_4pontos(f2, a2, b2)
    erro_abs, erro_rel = erro_integracao(aprox_gauss4, integral_exata_2)
    print(f"{'Gauss 4 pontos':<30} {aprox_gauss4:<15.10f} {erro_abs:<12.2e} {erro_rel:<12.4f}")
    
    # Exemplo 3: Função exponencial
    print("\n" + "-" * 60)
    print("EXEMPLO 3: ∫₀¹ e^x dx")
    print("-" * 60)
    
    f3 = lambda x: np.exp(x)
    a3, b3 = 0, 1
    integral_exata_3 = np.e - 1
    
    print(f"Integral exata: {integral_exata_3:.10f}")
    print(f"\n{'Método':<30} {'Aproximação':<15} {'Erro Abs':<12} {'Erro Rel %':<12}")
    print("-" * 60)
    
    # Teste com diferentes números de subintervalos
    for n in [2, 4, 8, 16]:
        aprox = regra_trapezio(f3, a3, b3, n=n)
        erro_abs, erro_rel = erro_integracao(aprox, integral_exata_3)
        print(f"{f'Trapézio (n={n})':<30} {aprox:<15.10f} {erro_abs:<12.2e} {erro_rel:<12.4f}")
    
    # Exemplo 4: Convergência da Regra do Trapézio
    print("\n" + "-" * 60)
    print("EXEMPLO 4: CONVERGÊNCIA - ∫₀¹ x³ dx")
    print("-" * 60)
    
    f4 = lambda x: x**3
    a4, b4 = 0, 1
    integral_exata_4 = 0.25
    
    print(f"Integral exata: {integral_exata_4}")
    print(f"\n{'n':<10} {'Trapézio':<15} {'Erro':<15}")
    print("-" * 60)
    
    for n in [2, 4, 8, 16, 32, 64, 128]:
        aprox = regra_trapezio(f4, a4, b4, n=n)
        erro_abs, _ = erro_integracao(aprox, integral_exata_4)
        print(f"{n:<10} {aprox:<15.10f} {erro_abs:<15.2e}")
    
    # Exemplo 5: Comparação de métodos
    print("\n" + "-" * 60)
    print("EXEMPLO 5: COMPARAÇÃO QUADRATURA DE GAUSS")
    print("-" * 60)
    print("Função: ∫₋₁¹ (1 + x + x² + x³ + x⁴ + x⁵) dx")
    
    f5 = lambda x: 1 + x + x**2 + x**3 + x**4 + x**5
    a5, b5 = -1, 1
    integral_exata_5 = 8/3  # Calculado analiticamente
    
    print(f"Integral exata: {integral_exata_5:.10f}")
    print(f"\n{'Método':<30} {'Aproximação':<15} {'Erro Abs':<12}")
    print("-" * 60)
    
    aprox_g2 = quadratura_gauss_2pontos(f5, a5, b5)
    erro_abs, _ = erro_integracao(aprox_g2, integral_exata_5)
    print(f"{'Gauss 2 pontos':<30} {aprox_g2:<15.10f} {erro_abs:<12.2e}")
    
    aprox_g3 = quadratura_gauss_3pontos(f5, a5, b5)
    erro_abs, _ = erro_integracao(aprox_g3, integral_exata_5)
    print(f"{'Gauss 3 pontos':<30} {aprox_g3:<15.10f} {erro_abs:<12.2e}")
    
    aprox_g4 = quadratura_gauss_4pontos(f5, a5, b5)
    erro_abs, _ = erro_integracao(aprox_g4, integral_exata_5)
    print(f"{'Gauss 4 pontos':<30} {aprox_g4:<15.10f} {erro_abs:<12.2e}")
    
    print("\n" + "-" * 60)
    print("OBSERVAÇÃO:")
    print("- Gauss com n pontos integra exatamente polinômios de grau ≤ 2n-1")
    print("- Gauss 3 pontos integra exatamente polinômios de grau ≤ 5")
    print("-" * 60)


if __name__ == "__main__":
    teste_integracao_numerica()
