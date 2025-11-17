"""
RESOLUÇÃO DOS PROBLEMAS DA LISTA DE EXERCÍCIOS
"""

import numpy as np
import sys
import os

# Adicionar pasta metodos ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'metodos'))

import metodos_diretos as md
import metodos_iterativos as mi
import interpolacao_minimos_quadrados as imq
import integracao_numerica as intn

print("=" * 80)
print("RESOLUÇÃO DA LISTA - CÁLCULO NUMÉRICO")
print("=" * 80)

# =============================================================================
# TÓPICO 01 - MÉTODOS DIRETOS
# =============================================================================
print("\n" + "=" * 80)
print("TÓPICO 01 - MÉTODOS DIRETOS")
print("=" * 80)

# PROBLEMA 1 - Produção de componentes eletrônicos
print("\nPROBLEMA 1: Produção de componentes eletrônicos")
print("-" * 80)
print("Sistema: 4T + 3R + 2C = 960 (cobre)")
print("         1T + 3R + 1C = 510 (zinco)")
print("         2T + 1R + 3C = 610 (vidro)")


A1 = np.array([[4, 3, 2],
               [1, 3, 1],
               [2, 1, 3]], dtype=float)
b1 = np.array([960, 510, 610], dtype=float)

x1 = md.eliminacao_gauss(A1.copy(), b1.copy())
print(f"Solução: {x1[0]:.0f} Transistores, {x1[1]:.0f} Resistores, {x1[2]:.0f} Chips")

# =============================================================================
# TÓPICO 02 - MÉTODOS ITERATIVOS
# =============================================================================
print("\n" + "=" * 80)
print("TÓPICO 02 - MÉTODOS ITERATIVOS (Gauss-Seidel)")
print("=" * 80)

# PROBLEMA 3 - Circuito elétrico
print("\nPROBLEMA 3: Circuito elétrico com resistores")
print("-" * 80)

A_circuito = np.array([[8.5, -2.5, 0, 0],
                       [-2.5, 10.3, -3, 0],
                       [0, -3, 12, -4],
                       [0, 0, -4, 11]], dtype=float)
b_circuito = np.array([16, 0, 0, 14], dtype=float)

x_circuito, iter_circ, _ = mi.metodo_gauss_seidel(A_circuito, b_circuito, tol=0.0001)
print(f"Solução (tensões): V1={x_circuito[0]:.4f}V, V2={x_circuito[1]:.4f}V, V3={x_circuito[2]:.4f}V, V4={x_circuito[3]:.4f}V")
print(f"Iterações: {iter_circ}")


# =============================================================================
# TÓPICO 03 - INTERPOLAÇÃO E MÍNIMOS QUADRADOS
# =============================================================================
print("\n" + "=" * 80)
print("TÓPICO 03 - INTERPOLAÇÃO E MÍNIMOS QUADRADOS")
print("=" * 80)

# PROBLEMA 2 - Queda de tensao em resistor
print("\nPROBLEMA 2: Queda de voltagem em resistor")
print("-" * 80)

correntes = np.array([0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 2.00])
voltagens = np.array([0.28, 0.67, 0.97, 1.42, 1.88, 6.0, 8.0])

# Interpolação de Lagrange
P_volt = imq.interpolacao_lagrange(correntes, voltagens)
print(f"Interpolação Lagrange - V(0.85A) = {P_volt(0.85):.2f}V")

# Ajuste polinomial grau 2
coef_2 = imq.minimos_quadrados_polinomial(correntes, voltagens, 2)
v_aj_2 = imq.avaliar_polinomio(coef_2, correntes)
r2_2 = imq.coeficiente_determinacao(voltagens, v_aj_2)
print(f"Ajuste grau 2: V = {coef_2[2]:.4f}I² + {coef_2[1]:.4f}I + {coef_2[0]:.4f}, R²={r2_2:.6f}")

# Ajuste polinomial grau 3
coef_3 = imq.minimos_quadrados_polinomial(correntes, voltagens, 3)
v_aj_3 = imq.avaliar_polinomio(coef_3, correntes)
r2_3 = imq.coeficiente_determinacao(voltagens, v_aj_3)
print(f"Ajuste grau 3: R²={r2_3:.6f}")

# =============================================================================
# TÓPICO 04 - INTEGRAÇÃO NUMÉRICA
# =============================================================================
print("\n" + "=" * 80)
print("TÓPICO 04 - INTEGRAÇÃO NUMÉRICA")
print("=" * 80)

# PROBLEMA 2 - Momento de um rio
print("\nPROBLEMA 2: Área de um rio entre margens")
print("-" * 80)

x_rio = np.array([0, 10, 20, 30, 40])
M1 = np.array([50.8, 86.2, 136, 72.8, 51])
M2 = np.array([113.6, 144.5, 185, 171.2, 95.3])
larguras = M2 - M1

P_largura = imq.interpolacao_lagrange(x_rio, larguras)

area_trap = intn.regra_trapezio(P_largura, 0, 40, n=4)
area_simp = intn.regra_simpson_1_3(P_largura, 0, 40, n=4)

print(f"Área (Trapézio): {area_trap:.2f} m²")
print(f"Área (Simpson 1/3): {area_simp:.2f} m²")

print("\n" + "=" * 80)
print("RESOLUÇÃO CONCLUÍDA")
print("=" * 80)
