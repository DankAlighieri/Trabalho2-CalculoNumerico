"""
EXEMPLOS PRÁTICOS DE USO DOS MÓDULOS
Este arquivo demonstra como usar cada método implementado
"""

import numpy as np
import metodos_diretos as md
import metodos_iterativos as mi
import interpolacao_minimos_quadrados as imq
import integracao_numerica as intn

print("=" * 70)
print("EXEMPLOS PRÁTICOS - CÁLCULO NUMÉRICO")
print("=" * 70)

# =============================================================================
# EXEMPLO 1: SISTEMA LINEAR - MÉTODOS DIRETOS
# =============================================================================
print("\n" + "=" * 70)
print("EXEMPLO 1: RESOLVER SISTEMA LINEAR (MÉTODOS DIRETOS)")
print("=" * 70)

# Sistema: 3x + 2y - z = 1
#          2x - 2y + 4z = -2
#         -x + 0.5y - z = 0

A = np.array([[3, 2, -1],
              [2, -2, 4],
              [-1, 0.5, -1]], dtype=float)

b = np.array([1, -2, 0], dtype=float)

print("\nSistema:")
print("3x + 2y - z = 1")
print("2x - 2y + 4z = -2")
print("-x + 0.5y - z = 0")

# Usando Eliminação de Gauss
x_gauss = md.eliminacao_gauss(A.copy(), b.copy())
print(f"\nSolução (Gauss): x={x_gauss[0]:.4f}, y={x_gauss[1]:.4f}, z={x_gauss[2]:.4f}")

# Usando Decomposição LU
L, U = md.decomposicao_lu(A.copy())
x_lu = md.resolver_lu(L, U, b)
print(f"Solução (LU):    x={x_lu[0]:.4f}, y={x_lu[1]:.4f}, z={x_lu[2]:.4f}")

# Verificação
residuo = np.linalg.norm(np.dot(A, x_gauss) - b)
print(f"Resíduo: {residuo:.2e}")

# =============================================================================
# EXEMPLO 2: SISTEMA LINEAR - MÉTODOS ITERATIVOS
# =============================================================================
print("\n" + "=" * 70)
print("EXEMPLO 2: RESOLVER SISTEMA LINEAR (MÉTODOS ITERATIVOS)")
print("=" * 70)

# Sistema: 4x - y = 3
#         -x + 4y = 5

A_iter = np.array([[4, -1],
                   [-1, 4]], dtype=float)

b_iter = np.array([3, 5], dtype=float)

print("\nSistema:")
print("4x - y = 3")
print("-x + 4y = 5")

# Jacobi
x_jacobi, iter_j, _ = mi.metodo_jacobi(A_iter, b_iter, tol=1e-6)
print(f"\nJacobi:       x={x_jacobi[0]:.6f}, y={x_jacobi[1]:.6f} ({iter_j} iterações)")

# Gauss-Seidel
x_gs, iter_gs, _ = mi.metodo_gauss_seidel(A_iter, b_iter, tol=1e-6)
print(f"Gauss-Seidel: x={x_gs[0]:.6f}, y={x_gs[1]:.6f} ({iter_gs} iterações)")

# =============================================================================
# EXEMPLO 3: INTERPOLAÇÃO DE LAGRANGE
# =============================================================================
print("\n" + "=" * 70)
print("EXEMPLO 3: INTERPOLAÇÃO DE LAGRANGE")
print("=" * 70)

# Dados de temperatura ao longo do dia
horas = np.array([0, 6, 12, 18, 24])  # horas
temp = np.array([15, 14, 22, 19, 16])  # temperatura em °C

print("\nDados de temperatura:")
for i in range(len(horas)):
    print(f"  {horas[i]:2.0f}:00 - {temp[i]}°C")

P = imq.interpolacao_lagrange(horas, temp)

# Estimar temperatura às 9:00 e 15:00
print(f"\nTemperatura estimada:")
print(f"  09:00 - {P(9):.1f}°C")
print(f"  15:00 - {P(15):.1f}°C")

# =============================================================================
# EXEMPLO 4: AJUSTE POR MÍNIMOS QUADRADOS
# =============================================================================
print("\n" + "=" * 70)
print("EXEMPLO 4: AJUSTE LINEAR POR MÍNIMOS QUADRADOS")
print("=" * 70)

# Dados experimentais: relação entre tempo e distância
tempo = np.array([1, 2, 3, 4, 5, 6, 7, 8])  # segundos
distancia = np.array([2.9, 5.8, 9.1, 12.3, 15.0, 18.2, 21.1, 23.9])  # metros

print("\nDados experimentais (tempo vs distância):")
for i in range(len(tempo)):
    print(f"  t={tempo[i]}s → d={distancia[i]}m")

# Ajuste linear
a, b = imq.minimos_quadrados_linear(tempo, distancia)
print(f"\nReta ajustada: d(t) = {a:.2f}t + {b:.2f}")

# Qualidade do ajuste
y_ajustado = a * tempo + b
r2 = imq.coeficiente_determinacao(distancia, y_ajustado)
print(f"Coeficiente de determinação R² = {r2:.6f}")

# Previsão
t_novo = 10
d_previsto = a * t_novo + b
print(f"\nPrevisão: Para t={t_novo}s, d ≈ {d_previsto:.2f}m")

# =============================================================================
# EXEMPLO 5: INTERPOLAÇÃO DE NEWTON
# =============================================================================
print("\n" + "=" * 70)
print("EXEMPLO 5: INTERPOLAÇÃO DE NEWTON")
print("=" * 70)

# Pontos de uma função
x_pontos = np.array([1, 2, 3, 4])
y_pontos = np.array([1, 8, 27, 64])  # x³

print("\nPontos conhecidos:")
for i in range(len(x_pontos)):
    print(f"  ({x_pontos[i]}, {y_pontos[i]})")

P_newton, coef = imq.interpolacao_newton(x_pontos, y_pontos)

print(f"\nCoeficientes de Newton: {coef}")

# Avaliar em um ponto intermediário
x_test = 2.5
print(f"\nP({x_test}) = {P_newton(x_test):.2f}")
print(f"Valor real (2.5³) = {2.5**3:.2f}")

# =============================================================================
# EXEMPLO 6: INTEGRAÇÃO NUMÉRICA
# =============================================================================
print("\n" + "=" * 70)
print("EXEMPLO 6: INTEGRAÇÃO NUMÉRICA")
print("=" * 70)

# Calcular área sob a curva y = e^(-x²) de 0 a 1
# (Integral Gaussiana, não tem forma fechada simples)

def funcao(x):
    return np.exp(-x**2)

a_int, b_int = 0, 1

print(f"\nCalcular: ∫₀¹ e^(-x²) dx")

# Diferentes métodos
trap_10 = intn.regra_trapezio(funcao, a_int, b_int, n=10)
trap_100 = intn.regra_trapezio(funcao, a_int, b_int, n=100)
simp_10 = intn.regra_simpson_1_3(funcao, a_int, b_int, n=10)
gauss_3 = intn.quadratura_gauss_3pontos(funcao, a_int, b_int)

print(f"\nResultados:")
print(f"  Trapézio (n=10):   {trap_10:.8f}")
print(f"  Trapézio (n=100):  {trap_100:.8f}")
print(f"  Simpson 1/3 (n=10): {simp_10:.8f}")
print(f"  Gauss 3 pontos:     {gauss_3:.8f}")

# Valor de referência (calculado com alta precisão)
valor_ref = 0.74682413  # Aproximação conhecida
print(f"\n  Valor de referência: {valor_ref:.8f}")

# =============================================================================
# EXEMPLO 7: CÁLCULO DE ÁREA (APLICAÇÃO PRÁTICA)
# =============================================================================
print("\n" + "=" * 70)
print("EXEMPLO 7: CÁLCULO DE ÁREA - APLICAÇÃO PRÁTICA")
print("=" * 70)

# Calcular área sob a curva y = √(1-x²) de -1 a 1 (semicírculo)
# Deve dar π/2 ≈ 1.5708

def semicirculo(x):
    return np.sqrt(1 - x**2)

area_trap = intn.regra_trapezio(semicirculo, -1, 1, n=100)
area_simp = intn.regra_simpson_1_3(semicirculo, -1, 1, n=100)
area_gauss = intn.quadratura_gauss_4pontos(semicirculo, -1, 1)

area_exata = np.pi / 2

print(f"\nÁrea de semicírculo unitário (deve ser π/2):")
print(f"  Trapézio:       {area_trap:.8f} (erro: {abs(area_trap - area_exata):.2e})")
print(f"  Simpson 1/3:    {area_simp:.8f} (erro: {abs(area_simp - area_exata):.2e})")
print(f"  Gauss 4 pontos: {area_gauss:.8f} (erro: {abs(area_gauss - area_exata):.2e})")
print(f"  Valor exato:    {area_exata:.8f}")

# =============================================================================
# EXEMPLO 8: AJUSTE POLINOMIAL
# =============================================================================
print("\n" + "=" * 70)
print("EXEMPLO 8: AJUSTE POLINOMIAL DE GRAU 2")
print("=" * 70)

# Dados que seguem aproximadamente uma parábola
x_data = np.array([0, 1, 2, 3, 4, 5])
y_data = np.array([1.1, 2.9, 8.2, 16.8, 29.1, 45.3])

print("\nDados experimentais:")
for i in range(len(x_data)):
    print(f"  ({x_data[i]}, {y_data[i]})")

# Ajuste com polinômio de grau 2
coef_poly = imq.minimos_quadrados_polinomial(x_data, y_data, grau=2)

print(f"\nPolinômio ajustado: y = {coef_poly[2]:.2f}x² + {coef_poly[1]:.2f}x + {coef_poly[0]:.2f}")

# Qualidade do ajuste
y_ajust = imq.avaliar_polinomio(coef_poly, x_data)
r2_poly = imq.coeficiente_determinacao(y_data, y_ajust)
erro_poly = imq.calcular_erro_quadratico(y_data, y_ajust)

print(f"R² = {r2_poly:.6f}")
print(f"Erro quadrático médio = {erro_poly:.4f}")

# =============================================================================
# EXEMPLO 9: COMPARAÇÃO INTERPOLAÇÃO vs AJUSTE
# =============================================================================
print("\n" + "=" * 70)
print("EXEMPLO 9: INTERPOLAÇÃO vs AJUSTE (DADOS COM RUÍDO)")
print("=" * 70)

# Dados com ruído
x_ruido = np.array([0, 1, 2, 3, 4])
y_ruido = np.array([1.2, 2.8, 4.3, 5.9, 8.1])  # Aproximadamente linear com ruído

print("\nDados com ruído:")
for i in range(len(x_ruido)):
    print(f"  ({x_ruido[i]}, {y_ruido[i]})")

# Interpolação (passa por todos os pontos)
P_interp = imq.interpolacao_lagrange(x_ruido, y_ruido)

# Ajuste linear (minimiza erro global)
a_ajuste, b_ajuste = imq.minimos_quadrados_linear(x_ruido, y_ruido)

x_test_2 = 2.5
print(f"\nEm x = {x_test_2}:")
print(f"  Interpolação:  y = {P_interp(x_test_2):.2f}")
print(f"  Ajuste linear: y = {a_ajuste * x_test_2 + b_ajuste:.2f}")

print("\nObservação:")
print("  - Interpolação: passa por TODOS os pontos (incluindo o ruído)")
print("  - Ajuste: encontra tendência geral (suaviza o ruído)")

# =============================================================================
# EXEMPLO 10: CONVERGÊNCIA DE MÉTODO ITERATIVO
# =============================================================================
print("\n" + "=" * 70)
print("EXEMPLO 10: ANÁLISE DE CONVERGÊNCIA")
print("=" * 70)

A_conv = np.array([[5, 1],
                   [1, 5]], dtype=float)
b_conv = np.array([6, 6], dtype=float)

print("\nSistema:")
print("5x + y = 6")
print("x + 5y = 6")

# Teste com diferentes tolerâncias
tolerancias = [1e-3, 1e-6, 1e-9]

print(f"\n{'Tolerância':<15} {'Iterações (GS)':<20} {'Resíduo':<15}")
print("-" * 50)

for tol in tolerancias:
    x_conv, iter_conv, _ = mi.metodo_gauss_seidel(A_conv, b_conv, tol=tol)
    res_conv = mi.calcular_residuo(A_conv, x_conv, b_conv)
    print(f"{tol:<15.0e} {iter_conv:<20} {res_conv:<15.2e}")

print("\n" + "=" * 70)
print("FIM DOS EXEMPLOS")
print("=" * 70)
print("\nDica: Execute 'python main.py' para a interface interativa!")
