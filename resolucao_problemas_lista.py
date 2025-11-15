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


# PROBLEMA 2 - Produção de componentes elétricos
print("\nPROBLEMA 2: Produção de componentes elétricos")
print("-" * 80)
print("Sistema: 15x + 17y + 19z = 3890 (metal)")
print("         0.30x + 0.40y + 0.55z = 95 (plástico)")
print("         1.0x + 1.2y + 1.5z = 282 (borracha)")

A2 = np.array([[15, 17, 19],
               [0.30, 0.40, 0.55],
               [1.0, 1.2, 1.5]], dtype=float)
b2 = np.array([3890, 95, 282], dtype=float)

x2 = md.eliminacao_gauss(A2.copy(), b2.copy())
print(f"Solução: {x2[0]:.0f} unid. Comp.1, {x2[1]:.0f} unid. Comp.2, {x2[2]:.0f} unid. Comp.3")


# PROBLEMA 3 - Construção de mineração
print("\nPROBLEMA 3: Construção de mineração")
print("-" * 80)
print("Sistema: 0.50m1 + 0.25m2 + 0.25m3 = 4800 (areia)")
print("         0.30m1 + 0.45m2 + 0.20m3 = 5800 (cascalho fino)")
print("         0.15m1 + 0.30m2 + 0.30m3 = 5700 (cascalho grosso)")

A3 = np.array([[0.50, 0.25, 0.25],
               [0.30, 0.45, 0.20],
               [0.15, 0.30, 0.30]], dtype=float)
b3 = np.array([4800, 5800, 5700], dtype=float)

x3 = md.eliminacao_gauss(A3.copy(), b3.copy())
print(f"Solução: Mina 1: {x3[0]:.0f} m³, Mina 2: {x3[1]:.0f} m³, Mina 3: {x3[2]:.0f} m³")


# =============================================================================
# TÓPICO 02 - MÉTODOS ITERATIVOS
# =============================================================================
print("\n" + "=" * 80)
print("TÓPICO 02 - MÉTODOS ITERATIVOS (Gauss-Seidel)")
print("=" * 80)

# PROBLEMA 1 - Ponte de Wheatstone
print("\nPROBLEMA 1: Circuito - Ponte de Wheatstone")
print("-" * 80)

A_ponte = np.array([[10, -1, -1, 0, 0],
                    [-1, 15, 0, -2, 0],
                    [-1, 0, 12, -1, 0],
                    [0, -2, -1, 20, -1],
                    [0, 0, 0, -1, 8]], dtype=float)
b_ponte = np.array([12, 25, 10, 30, 15], dtype=float)

x_ponte, iter_ponte, _ = mi.metodo_gauss_seidel(A_ponte, b_ponte, tol=0.0001)
print(f"Solução (correntes): I1={x_ponte[0]:.4f}A, I2={x_ponte[1]:.4f}A, I3={x_ponte[2]:.4f}A, I4={x_ponte[3]:.4f}A, I5={x_ponte[4]:.4f}A")
print(f"Iterações: {iter_ponte}")


# PROBLEMA 2 - Treliça estática
print("\nPROBLEMA 2: Treliça estática")
print("-" * 80)

A_trelica = np.array([[10, -2, 0, 0, 0],
                      [-2, 15, -3, 0, 0],
                      [0, -3, 18, -2, 0],
                      [0, 0, -2, 12, -1],
                      [0, 0, 0, -1, 8]], dtype=float)
b_trelica = np.array([20, 15, 10, 25, 18], dtype=float)

x_trelica, iter_trelica, _ = mi.metodo_gauss_seidel(A_trelica, b_trelica, tol=0.0001)
print(f"Solução (tensões): T1={x_trelica[0]:.4f}, T2={x_trelica[1]:.4f}, T3={x_trelica[2]:.4f}, T4={x_trelica[3]:.4f}, T5={x_trelica[4]:.4f}")
print(f"Iterações: {iter_trelica}")


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

# PROBLEMA 1 - Lei de Moore
print("\nPROBLEMA 1: Lei de Moore - Previsão de transistores")
print("-" * 80)

anos = np.array([1971, 1972, 1974, 1978, 1982, 1985, 1989, 1993, 1997, 1999, 2000])
transistores = np.array([2300, 3500, 6000, 29000, 134000, 275000, 
                        1200000, 3100000, 7500000, 9500000, 42000000])
log_transistores = np.log(transistores)

# Ajuste linear nos dados logarítmicos
a_moore, b_moore = imq.minimos_quadrados_linear(anos, log_transistores)
prev_2010 = np.exp(a_moore * 2010 + b_moore)
prev_2020 = np.exp(a_moore * 2020 + b_moore)

print(f"Modelo: log(N) = {a_moore:.4f} * ano + {b_moore:.2f}")
print(f"Previsão 2010: {prev_2010:,.0f} transistores")
print(f"Previsão 2020: {prev_2020:,.0f} transistores")
r2_moore = imq.coeficiente_determinacao(log_transistores, a_moore * anos + b_moore)
print(f"R² = {r2_moore:.6f}")


# PROBLEMA 2 - Queda de voltagem em resistor
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


# PROBLEMA 3 - Regressão por mínimos quadrados
print("\nPROBLEMA 3: Regressão por mínimos quadrados")
print("-" * 80)

x_reg = np.array([0, 1.5, 2.6, 4.2, 6, 8.2, 10, 11.4])
y_reg = np.array([18, 13, 11, 9, 6, 4, 2, 1])

# Ajuste linear
a_lin, b_lin = imq.minimos_quadrados_linear(x_reg, y_reg)
y_lin = a_lin * x_reg + b_lin
r2_lin = imq.coeficiente_determinacao(y_reg, y_lin)
soma_lin = np.sum((y_reg - y_lin)**2)

# Ajuste parabólico
coef_parab = imq.minimos_quadrados_polinomial(x_reg, y_reg, 2)
y_parab = imq.avaliar_polinomio(coef_parab, x_reg)
r2_parab = imq.coeficiente_determinacao(y_reg, y_parab)
soma_parab = np.sum((y_reg - y_parab)**2)

# Ajuste exponencial
log_y = np.log(y_reg)
b_exp, log_a = imq.minimos_quadrados_linear(x_reg, log_y)
a_exp = np.exp(log_a)
y_exp = a_exp * np.exp(b_exp * x_reg)
r2_exp = imq.coeficiente_determinacao(y_reg, y_exp)
soma_exp = np.sum((y_reg - y_exp)**2)

print(f"Linear:       y = {a_lin:.4f}x + {b_lin:.4f}, R2={r2_lin:.6f}, Soma_erros2={soma_lin:.2f}")
print(f"Parabolico:   y = {coef_parab[2]:.4f}x^2 + {coef_parab[1]:.4f}x + {coef_parab[0]:.4f}, R2={r2_parab:.6f}, Soma_erros2={soma_parab:.2f}")
print(f"Exponencial:  y = {a_exp:.4f}*e^({b_exp:.4f}x), R2={r2_exp:.6f}, Soma_erros2={soma_exp:.2f}")
print(f"Melhor ajuste: Parabólico (menor erro)")


# =============================================================================
# TÓPICO 04 - INTEGRAÇÃO NUMÉRICA
# =============================================================================
print("\n" + "=" * 80)
print("TÓPICO 04 - INTEGRAÇÃO NUMÉRICA")
print("=" * 80)

# PROBLEMA 1 - Área da seção reta de rio
print("\nPROBLEMA 1: Área da seção reta de rio")
print("-" * 80)

distancias = np.array([0, 2, 4, 6, 8, 10])
profundidades = np.array([4.4, 4.1, 4.0, 5.0, 5.8, 5.5])
P_rio = imq.interpolacao_lagrange(distancias, profundidades)

area_trap = intn.regra_trapezio(P_rio, 0, 10, n=5)
area_simp = intn.regra_simpson_1_3(P_rio, 0, 10, n=10)

print(f"Área (Trapézio): {area_trap:.2f} m²")
print(f"Área (Simpson 1/3): {area_simp:.2f} m²")


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


# PROBLEMA 3 - Seção de trecho de navio
print("\nPROBLEMA 3: Área da seção de um navio")
print("-" * 80)

distancias_navio = np.array([3.00, 2.92, 2.75, 2.52, 2.30, 1.84, 0.92, 0.00])
x_navio = np.arange(0, len(distancias_navio)) * 1.0  # M = 1m
P_navio = imq.interpolacao_lagrange(x_navio, distancias_navio)

area_meio_trap = intn.regra_trapezio(P_navio, x_navio[0], x_navio[-1], n=7)
area_total_trap = 2 * area_meio_trap

area_meio_simp = intn.regra_simpson_1_3(P_navio, x_navio[0], x_navio[-2], n=6)
area_total_simp = 2 * area_meio_simp

area_meio_simp38 = intn.regra_simpson_3_8(P_navio, x_navio[0], x_navio[6], n=6)
area_total_simp38 = 2 * area_meio_simp38

print(f"Área total (Trapézio): {area_total_trap:.3f} m²")
print(f"Área total (Simpson 1/3): {area_total_simp:.3f} m²")
print(f"Área total (Simpson 3/8): {area_total_simp38:.3f} m²")


print("\n" + "=" * 80)
print("RESOLUÇÃO CONCLUÍDA")
print("=" * 80)
