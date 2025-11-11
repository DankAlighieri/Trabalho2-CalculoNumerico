"""
APLICAÇÃO PRINCIPAL - CÁLCULO NUMÉRICO
Menu interativo para execução de todos os métodos numéricos
"""

import numpy as np
from typing import Callable
import os

# Importa os módulos
import metodos_diretos as md
import metodos_iterativos as mi
import interpolacao_minimos_quadrados as imq
import integracao_numerica as intn


def limpar_tela():
    """Limpa a tela do terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')


def pausar():
    """Pausa e espera o usuário pressionar Enter"""
    input("\nPressione Enter para continuar...")


def exibir_menu_principal():
    """Exibe o menu principal"""
    print("\n" + "=" * 70)
    print(" " * 15 + "CÁLCULO NUMÉRICO - APLICAÇÃO COMPLETA")
    print("=" * 70)
    print("\n1. SISTEMAS DE EQUAÇÕES LINEARES - MÉTODOS DIRETOS")
    print("2. SISTEMAS DE EQUAÇÕES LINEARES - MÉTODOS ITERATIVOS")
    print("3. INTERPOLAÇÃO POLINOMIAL E MÍNIMOS QUADRADOS")
    print("4. INTEGRAÇÃO NUMÉRICA")
    print("5. EXECUTAR TODOS OS TESTES")
    print("0. SAIR")
    print("\n" + "-" * 70)


def menu_metodos_diretos():
    """Menu para métodos diretos"""
    while True:
        limpar_tela()
        print("\n" + "=" * 70)
        print("MÉTODOS DIRETOS PARA SISTEMAS LINEARES")
        print("=" * 70)
        print("\n1. Eliminação de Gauss")
        print("2. Gauss-Jordan")
        print("3. Decomposição LU")
        print("4. Decomposição de Cholesky")
        print("5. Executar exemplo completo")
        print("6. Sistema personalizado")
        print("0. Voltar")
        print("\n" + "-" * 70)
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "0":
            break
        elif opcao == "5":
            limpar_tela()
            md.teste_metodos_diretos()
            pausar()
        elif opcao == "6":
            sistema_personalizado_direto()
        elif opcao in ["1", "2", "3", "4"]:
            executar_metodo_direto_especifico(opcao)
        else:
            print("Opção inválida!")
            pausar()


def executar_metodo_direto_especifico(opcao: str):
    """Executa um método direto específico"""
    limpar_tela()
    
    # Sistema exemplo
    A = np.array([[4, -1, 0, 0],
                  [-1, 4, -1, 0],
                  [0, -1, 4, -1],
                  [0, 0, -1, 3]], dtype=float)
    b = np.array([15, 10, 10, 10], dtype=float)
    
    print("Sistema Linear de Exemplo:")
    print("A =")
    print(A)
    print(f"\nb = {b}\n")
    
    if opcao == "1":
        print("ELIMINAÇÃO DE GAUSS")
        print("-" * 70)
        x = md.eliminacao_gauss(A.copy(), b.copy())
        print(f"Solução: {x}")
        print(f"Verificação Ax = {np.dot(A, x)}")
        print(f"Resíduo: {np.linalg.norm(np.dot(A, x) - b):.2e}")
    
    elif opcao == "2":
        print("GAUSS-JORDAN")
        print("-" * 70)
        x = md.gauss_jordan(A.copy(), b.copy())
        print(f"Solução: {x}")
        print(f"Verificação Ax = {np.dot(A, x)}")
        print(f"Resíduo: {np.linalg.norm(np.dot(A, x) - b):.2e}")
    
    elif opcao == "3":
        print("DECOMPOSIÇÃO LU")
        print("-" * 70)
        L, U = md.decomposicao_lu(A.copy())
        print("Matriz L (triangular inferior):")
        print(L)
        print("\nMatriz U (triangular superior):")
        print(U)
        print(f"\nVerificação L*U = A, erro: {np.linalg.norm(np.dot(L, U) - A):.2e}")
        
        x = md.resolver_lu(L, U, b)
        print(f"\nSolução: {x}")
        print(f"Resíduo: {np.linalg.norm(np.dot(A, x) - b):.2e}")
    
    elif opcao == "4":
        print("DECOMPOSIÇÃO DE CHOLESKY")
        print("-" * 70)
        A_spd = np.array([[4, 2, 2],
                          [2, 5, 1],
                          [2, 1, 6]], dtype=float)
        b_spd = np.array([8, 8, 9], dtype=float)
        
        print("Matriz simétrica positiva definida:")
        print(A_spd)
        print(f"b = {b_spd}\n")
        
        L = md.decomposicao_cholesky(A_spd)
        print("Matriz L:")
        print(L)
        print(f"\nVerificação L*L^T = A, erro: {np.linalg.norm(np.dot(L, L.T) - A_spd):.2e}")
        
        x = md.resolver_cholesky(L, b_spd)
        print(f"\nSolução: {x}")
        print(f"Resíduo: {np.linalg.norm(np.dot(A_spd, x) - b_spd):.2e}")
    
    pausar()


def sistema_personalizado_direto():
    """Permite ao usuário inserir sistema próprio"""
    limpar_tela()
    print("SISTEMA PERSONALIZADO - MÉTODO DIRETO")
    print("-" * 70)
    
    try:
        n = int(input("Digite o tamanho do sistema (n x n): "))
        
        print(f"\nDigite os elementos da matriz A ({n}x{n}):")
        A = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                A[i, j] = float(input(f"A[{i}][{j}] = "))
        
        print(f"\nDigite os elementos do vetor b ({n}):")
        b = np.zeros(n)
        for i in range(n):
            b[i] = float(input(f"b[{i}] = "))
        
        print("\nSistema inserido:")
        print("A =")
        print(A)
        print(f"b = {b}\n")
        
        print("Escolha o método:")
        print("1. Eliminação de Gauss")
        print("2. Gauss-Jordan")
        print("3. Decomposição LU")
        metodo = input("Método: ").strip()
        
        if metodo == "1":
            x = md.eliminacao_gauss(A, b)
        elif metodo == "2":
            x = md.gauss_jordan(A, b)
        elif metodo == "3":
            L, U = md.decomposicao_lu(A)
            x = md.resolver_lu(L, U, b)
        else:
            print("Método inválido!")
            pausar()
            return
        
        print(f"\nSolução: {x}")
        print(f"Resíduo: {np.linalg.norm(np.dot(A, x) - b):.2e}")
        
    except Exception as e:
        print(f"\nErro: {e}")
    
    pausar()


def menu_metodos_iterativos():
    """Menu para métodos iterativos"""
    while True:
        limpar_tela()
        print("\n" + "=" * 70)
        print("MÉTODOS ITERATIVOS PARA SISTEMAS LINEARES")
        print("=" * 70)
        print("\n1. Método de Jacobi")
        print("2. Método de Gauss-Seidel")
        print("3. Método SOR")
        print("4. Comparação de métodos")
        print("5. Executar exemplo completo")
        print("0. Voltar")
        print("\n" + "-" * 70)
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "0":
            break
        elif opcao == "5":
            limpar_tela()
            mi.teste_metodos_iterativos()
            pausar()
        elif opcao in ["1", "2", "3", "4"]:
            executar_metodo_iterativo_especifico(opcao)
        else:
            print("Opção inválida!")
            pausar()


def executar_metodo_iterativo_especifico(opcao: str):
    """Executa um método iterativo específico"""
    limpar_tela()
    
    # Sistema exemplo
    A = np.array([[10, -1, 2, 0],
                  [-1, 11, -1, 3],
                  [2, -1, 10, -1],
                  [0, 3, -1, 8]], dtype=float)
    b = np.array([6, 25, -11, 15], dtype=float)
    
    print("Sistema Linear de Exemplo:")
    print("A =")
    print(A)
    print(f"\nb = {b}")
    
    if mi.verificar_convergencia_diagonal(A):
        print("✓ Matriz diagonalmente dominante\n")
    else:
        print("⚠ Matriz NÃO diagonalmente dominante\n")
    
    if opcao == "1":
        print("MÉTODO DE JACOBI")
        print("-" * 70)
        x, iter_count, erros = mi.metodo_jacobi(A, b, tol=1e-6)
        print(f"Solução: {x}")
        print(f"Iterações: {iter_count}")
        print(f"Resíduo: {mi.calcular_residuo(A, x, b):.2e}")
    
    elif opcao == "2":
        print("MÉTODO DE GAUSS-SEIDEL")
        print("-" * 70)
        x, iter_count, erros = mi.metodo_gauss_seidel(A, b, tol=1e-6)
        print(f"Solução: {x}")
        print(f"Iterações: {iter_count}")
        print(f"Resíduo: {mi.calcular_residuo(A, x, b):.2e}")
    
    elif opcao == "3":
        print("MÉTODO SOR")
        print("-" * 70)
        omega = float(input("Digite o fator de relaxação ω (sugestão: 1.1): ") or "1.1")
        x, iter_count, erros = mi.metodo_sor(A, b, omega=omega, tol=1e-6)
        print(f"Solução: {x}")
        print(f"Iterações: {iter_count}")
        print(f"Resíduo: {mi.calcular_residuo(A, x, b):.2e}")
    
    elif opcao == "4":
        print("COMPARAÇÃO DE MÉTODOS")
        print("-" * 70)
        
        x_j, it_j, _ = mi.metodo_jacobi(A, b, tol=1e-6)
        x_gs, it_gs, _ = mi.metodo_gauss_seidel(A, b, tol=1e-6)
        x_sor, it_sor, _ = mi.metodo_sor(A, b, omega=1.1, tol=1e-6)
        
        print(f"{'Método':<20} {'Iterações':<12} {'Resíduo':<15}")
        print("-" * 70)
        print(f"{'Jacobi':<20} {it_j:<12} {mi.calcular_residuo(A, x_j, b):<15.2e}")
        print(f"{'Gauss-Seidel':<20} {it_gs:<12} {mi.calcular_residuo(A, x_gs, b):<15.2e}")
        print(f"{'SOR (ω=1.1)':<20} {it_sor:<12} {mi.calcular_residuo(A, x_sor, b):<15.2e}")
    
    pausar()


def menu_interpolacao_minimos_quadrados():
    """Menu para interpolação e mínimos quadrados"""
    while True:
        limpar_tela()
        print("\n" + "=" * 70)
        print("INTERPOLAÇÃO POLINOMIAL E MÍNIMOS QUADRADOS")
        print("=" * 70)
        print("\n1. Interpolação de Lagrange")
        print("2. Interpolação de Newton")
        print("3. Ajuste Linear (Mínimos Quadrados)")
        print("4. Ajuste Polinomial (Mínimos Quadrados)")
        print("5. Executar exemplo completo")
        print("0. Voltar")
        print("\n" + "-" * 70)
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "0":
            break
        elif opcao == "5":
            limpar_tela()
            imq.teste_interpolacao_minimos_quadrados()
            pausar()
        elif opcao in ["1", "2", "3", "4"]:
            executar_interpolacao_especifica(opcao)
        else:
            print("Opção inválida!")
            pausar()


def executar_interpolacao_especifica(opcao: str):
    """Executa interpolação específica"""
    limpar_tela()
    
    if opcao in ["1", "2"]:
        # Dados de exemplo para interpolação
        x = np.array([0, 1, 2, 3, 4])
        y = np.array([1, 2.7, 5.8, 11, 18.2])
        
        print("Pontos conhecidos:")
        for i in range(len(x)):
            print(f"  ({x[i]}, {y[i]})")
        
        if opcao == "1":
            print("\nINTERPOLAÇÃO DE LAGRANGE")
            print("-" * 70)
            P = imq.interpolacao_lagrange(x, y)
        else:
            print("\nINTERPOLAÇÃO DE NEWTON")
            print("-" * 70)
            P, coef = imq.interpolacao_newton(x, y)
            print(f"Coeficientes: {coef}\n")
        
        # Interpola em pontos
        x_teste = np.linspace(0, 4, 20)
        print("\nAlguns valores interpolados:")
        for xt in [0.5, 1.5, 2.5, 3.5]:
            print(f"  P({xt}) = {P(xt):.4f}")
    
    elif opcao == "3":
        print("AJUSTE LINEAR - MÍNIMOS QUADRADOS")
        print("-" * 70)
        
        x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        y = np.array([2.1, 3.9, 6.2, 8.1, 9.8, 12.3, 14.1, 16.2, 17.9, 20.1])
        
        print("Dados:")
        for i in range(len(x)):
            print(f"  ({x[i]}, {y[i]})")
        
        a, b = imq.minimos_quadrados_linear(x, y)
        print(f"\nReta ajustada: y = {a:.4f}x + {b:.4f}")
        
        y_ajustado = a * x + b
        erro = imq.calcular_erro_quadratico(y, y_ajustado)
        r2 = imq.coeficiente_determinacao(y, y_ajustado)
        
        print(f"Erro quadrático médio: {erro:.4f}")
        print(f"R² = {r2:.6f}")
    
    elif opcao == "4":
        print("AJUSTE POLINOMIAL - MÍNIMOS QUADRADOS")
        print("-" * 70)
        
        x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        y = np.array([2.1, 3.9, 6.2, 8.1, 9.8, 12.3, 14.1, 16.2, 17.9, 20.1])
        
        print("Dados:")
        for i in range(len(x)):
            print(f"  ({x[i]}, {y[i]})")
        
        grau = int(input("\nGrau do polinômio: "))
        coef = imq.minimos_quadrados_polinomial(x, y, grau)
        
        print(f"\nCoeficientes: {coef}")
        
        y_ajustado = imq.avaliar_polinomio(coef, x)
        erro = imq.calcular_erro_quadratico(y, y_ajustado)
        r2 = imq.coeficiente_determinacao(y, y_ajustado)
        
        print(f"Erro quadrático médio: {erro:.4f}")
        print(f"R² = {r2:.6f}")
    
    pausar()


def menu_integracao_numerica():
    """Menu para integração numérica"""
    while True:
        limpar_tela()
        print("\n" + "=" * 70)
        print("INTEGRAÇÃO NUMÉRICA")
        print("=" * 70)
        print("\n1. Regra do Trapézio")
        print("2. Regra de Simpson 1/3")
        print("3. Regra de Simpson 3/8")
        print("4. Quadratura de Gauss")
        print("5. Comparação de métodos")
        print("6. Executar exemplo completo")
        print("0. Voltar")
        print("\n" + "-" * 70)
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "0":
            break
        elif opcao == "6":
            limpar_tela()
            intn.teste_integracao_numerica()
            pausar()
        elif opcao in ["1", "2", "3", "4", "5"]:
            executar_integracao_especifica(opcao)
        else:
            print("Opção inválida!")
            pausar()


def executar_integracao_especifica(opcao: str):
    """Executa método de integração específico"""
    limpar_tela()
    
    # Função exemplo: x^2
    f = lambda x: x**2
    a, b = 0, 2
    integral_exata = 8/3
    
    print("Exemplo: ∫₀² x² dx")
    print(f"Integral exata: {integral_exata:.10f}\n")
    
    if opcao == "1":
        print("REGRA DO TRAPÉZIO")
        print("-" * 70)
        n = int(input("Número de subintervalos: ") or "10")
        aprox = intn.regra_trapezio(f, a, b, n)
        erro_abs, erro_rel = intn.erro_integracao(aprox, integral_exata)
        print(f"\nAproximação: {aprox:.10f}")
        print(f"Erro absoluto: {erro_abs:.2e}")
        print(f"Erro relativo: {erro_rel:.4f}%")
    
    elif opcao == "2":
        print("REGRA DE SIMPSON 1/3")
        print("-" * 70)
        n = int(input("Número de subintervalos (deve ser par): ") or "10")
        if n % 2 != 0:
            print("Erro: n deve ser par!")
        else:
            aprox = intn.regra_simpson_1_3(f, a, b, n)
            erro_abs, erro_rel = intn.erro_integracao(aprox, integral_exata)
            print(f"\nAproximação: {aprox:.10f}")
            print(f"Erro absoluto: {erro_abs:.2e}")
            print(f"Erro relativo: {erro_rel:.4f}%")
    
    elif opcao == "3":
        print("REGRA DE SIMPSON 3/8")
        print("-" * 70)
        n = int(input("Número de subintervalos (múltiplo de 3): ") or "9")
        if n % 3 != 0:
            print("Erro: n deve ser múltiplo de 3!")
        else:
            aprox = intn.regra_simpson_3_8(f, a, b, n)
            erro_abs, erro_rel = intn.erro_integracao(aprox, integral_exata)
            print(f"\nAproximação: {aprox:.10f}")
            print(f"Erro absoluto: {erro_abs:.2e}")
            print(f"Erro relativo: {erro_rel:.4f}%")
    
    elif opcao == "4":
        print("QUADRATURA DE GAUSS")
        print("-" * 70)
        print("1. 2 pontos")
        print("2. 3 pontos")
        print("3. 4 pontos")
        sub_opcao = input("Escolha: ").strip()
        
        if sub_opcao == "1":
            aprox = intn.quadratura_gauss_2pontos(f, a, b)
        elif sub_opcao == "2":
            aprox = intn.quadratura_gauss_3pontos(f, a, b)
        elif sub_opcao == "3":
            aprox = intn.quadratura_gauss_4pontos(f, a, b)
        else:
            print("Opção inválida!")
            pausar()
            return
        
        erro_abs, erro_rel = intn.erro_integracao(aprox, integral_exata)
        print(f"\nAproximação: {aprox:.10f}")
        print(f"Erro absoluto: {erro_abs:.2e}")
        print(f"Erro relativo: {erro_rel:.4f}%")
    
    elif opcao == "5":
        print("COMPARAÇÃO DE MÉTODOS")
        print("-" * 70)
        
        print(f"\n{'Método':<30} {'Aproximação':<15} {'Erro Abs':<12}")
        print("-" * 70)
        
        aprox_trap = intn.regra_trapezio(f, a, b, 10)
        erro_abs, _ = intn.erro_integracao(aprox_trap, integral_exata)
        print(f"{'Trapézio (n=10)':<30} {aprox_trap:<15.10f} {erro_abs:<12.2e}")
        
        aprox_simp13 = intn.regra_simpson_1_3(f, a, b, 10)
        erro_abs, _ = intn.erro_integracao(aprox_simp13, integral_exata)
        print(f"{'Simpson 1/3 (n=10)':<30} {aprox_simp13:<15.10f} {erro_abs:<12.2e}")
        
        aprox_gauss3 = intn.quadratura_gauss_3pontos(f, a, b)
        erro_abs, _ = intn.erro_integracao(aprox_gauss3, integral_exata)
        print(f"{'Gauss 3 pontos':<30} {aprox_gauss3:<15.10f} {erro_abs:<12.2e}")
    
    pausar()


def executar_todos_testes():
    """Executa todos os testes de uma vez"""
    limpar_tela()
    print("=" * 70)
    print("EXECUTANDO TODOS OS TESTES")
    print("=" * 70)
    
    print("\n\n")
    md.teste_metodos_diretos()
    
    print("\n\n")
    mi.teste_metodos_iterativos()
    
    print("\n\n")
    imq.teste_interpolacao_minimos_quadrados()
    
    print("\n\n")
    intn.teste_integracao_numerica()
    
    pausar()


def main():
    """Função principal"""
    while True:
        limpar_tela()
        exibir_menu_principal()
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "0":
            print("\nEncerrando aplicação...")
            break
        elif opcao == "1":
            menu_metodos_diretos()
        elif opcao == "2":
            menu_metodos_iterativos()
        elif opcao == "3":
            menu_interpolacao_minimos_quadrados()
        elif opcao == "4":
            menu_integracao_numerica()
        elif opcao == "5":
            executar_todos_testes()
        else:
            print("Opção inválida!")
            pausar()


if __name__ == "__main__":
    main()
