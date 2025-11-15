"""
INTERFACE GRÁFICA MINIMALISTA - CÁLCULO NUMÉRICO
Paleta de cores minimalista: Branco, Cinza Claro, Cinza Escuro, Preto
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import numpy as np
import sys
import os

# Adicionar pasta metodos ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'metodos'))

import metodos_diretos as md
import metodos_iterativos as mi
import interpolacao_minimos_quadrados as imq
import integracao_numerica as intn


class CalculoNumericoGUI:
    """Interface gráfica para Cálculo Numérico"""
    
    # Paleta de cores minimalista
    CORES = {
        'bg_principal': '#FFFFFF',      # Branco
        'bg_secundario': '#F5F5F5',     # Cinza muito claro
        'bg_input': '#FAFAFA',          # Cinza claro
        'bg_ativo': '#E8E8E8',          # Cinza mais escuro
        'texto_principal': '#1A1A1A',   # Quase preto
        'texto_secundario': '#666666',  # Cinza escuro
        'borda': '#CCCCCC',             # Cinza claro
        'acento': '#2E2E2E',            # Cinza escuro (acento)
    }
    
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Cálculo Numérico - Interface Minimalista")
        self.janela.geometry("1200x700")
        self.janela.configure(bg=self.CORES['bg_principal'])
        
        # Estilo minimalista
        self._configurar_estilos()
        
        # Criar interface
        self._criar_interface()
        
    def _configurar_estilos(self):
        """Configura os estilos ttk com paleta minimalista"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configurar cores base
        style.configure('TFrame', background=self.CORES['bg_principal'])
        style.configure('TLabel', background=self.CORES['bg_principal'], 
                       foreground=self.CORES['texto_principal'])
        style.configure('Header.TLabel', font=('Segoe UI', 12, 'bold'),
                       background=self.CORES['bg_principal'],
                       foreground=self.CORES['acento'])
        style.configure('SubHeader.TLabel', font=('Segoe UI', 10, 'bold'),
                       background=self.CORES['bg_secundario'],
                       foreground=self.CORES['texto_principal'])
        
        # Botões minimalistas
        style.configure('TButton',
                       background=self.CORES['bg_secundario'],
                       foreground=self.CORES['texto_principal'],
                       borderwidth=1,
                       focuscolor='none',
                       padding=8)
        style.map('TButton',
                 background=[('active', self.CORES['bg_ativo'])],
                 foreground=[('active', self.CORES['acento'])])
        
        # Entrada de texto
        style.configure('TEntry',
                       fieldbackground=self.CORES['bg_input'],
                       foreground=self.CORES['texto_principal'],
                       borderwidth=1)
        
        # Notebook (abas)
        style.configure('TNotebook',
                       background=self.CORES['bg_principal'],
                       borderwidth=0)
        style.configure('TNotebook.Tab',
                       background=self.CORES['bg_secundario'],
                       foreground=self.CORES['texto_principal'],
                       padding=10)
        
    def _criar_interface(self):
        """Cria a interface principal"""
        # Frame principal com padding
        frame_principal = ttk.Frame(self.janela)
        frame_principal.pack(fill='both', expand=True, padx=15, pady=15)
        
        # Cabeçalho
        self._criar_cabecalho(frame_principal)
        
        # Notebook com abas
        notebook = ttk.Notebook(frame_principal)
        notebook.pack(fill='both', expand=True, pady=(15, 0))
        
        # Abas do programa
        self.aba_diretos = ttk.Frame(notebook)
        self.aba_iterativos = ttk.Frame(notebook)
        self.aba_interpolacao = ttk.Frame(notebook)
        self.aba_integracao = ttk.Frame(notebook)
        
        notebook.add(self.aba_diretos, text="Métodos Diretos")
        notebook.add(self.aba_iterativos, text="Métodos Iterativos")
        notebook.add(self.aba_interpolacao, text="Interpolação")
        notebook.add(self.aba_integracao, text="Integração Numérica")
        
        # Popular as abas
        self._popular_aba_diretos()
        self._popular_aba_iterativos()
        self._popular_aba_interpolacao()
        self._popular_aba_integracao()
        
        # Rodapé
        self._criar_rodape(frame_principal)
        
    def _criar_cabecalho(self, parent):
        """Cria o cabeçalho da interface"""
        frame_header = ttk.Frame(parent, relief='flat')
        frame_header.pack(fill='x', pady=(0, 15))
        
        label_titulo = ttk.Label(frame_header, text="Cálculo Numérico",
                                style='Header.TLabel')
        label_titulo.pack(anchor='w')
        
        label_descricao = ttk.Label(frame_header, 
                                   text="Resolva problemas usando métodos numéricos",
                                   style='SubHeader.TLabel')
        label_descricao.pack(anchor='w', padx=(0, 0))
        
    def _criar_rodape(self, parent):
        """Cria o rodapé com informações"""
        frame_rodape = ttk.Frame(parent)
        frame_rodape.pack(fill='x', pady=(15, 0), side='bottom')
        
        label_rodape = ttk.Label(frame_rodape, 
                                text="Trabalho 2 - Cálculo Numérico | Interface Minimalista",
                                foreground=self.CORES['texto_secundario'])
        label_rodape.pack()
        
    def _popular_aba_diretos(self):
        """Popula a aba de Métodos Diretos"""
        # Frame de entrada
        frame_entrada = ttk.LabelFrame(self.aba_diretos, text="Entrada de Dados",
                                       padding=10)
        frame_entrada.pack(fill='x', padx=10, pady=10)
        
        ttk.Label(frame_entrada, text="Matriz A (separada por vírgula em cada linha):").pack(anchor='w')
        self.text_matriz_a = scrolledtext.ScrolledText(frame_entrada, height=5, width=60,
                                                       bg=self.CORES['bg_input'],
                                                       fg=self.CORES['texto_principal'])
        self.text_matriz_a.pack(fill='x', pady=(5, 10))
        self.text_matriz_a.insert('1.0', "4, 3, 2\n1, 3, 1\n2, 1, 3")
        
        ttk.Label(frame_entrada, text="Vetor b (separado por vírgula):").pack(anchor='w')
        self.entry_vetor_b = ttk.Entry(frame_entrada, width=60)
        self.entry_vetor_b.pack(fill='x', pady=(5, 10))
        self.entry_vetor_b.insert(0, "960, 510, 610")
        
        # Frame de operações
        frame_operacoes = ttk.LabelFrame(self.aba_diretos, text="Operações", padding=10)
        frame_operacoes.pack(fill='x', padx=10, pady=10)
        
        ttk.Button(frame_operacoes, text="Eliminação de Gauss",
                  command=self._executar_gauss).pack(side='left', padx=5)
        ttk.Button(frame_operacoes, text="Fatoração LU",
                  command=self._executar_lu).pack(side='left', padx=5)
        ttk.Button(frame_operacoes, text="Limpar",
                  command=self._limpar_diretos).pack(side='left', padx=5)
        
        # Frame de saída
        frame_saida = ttk.LabelFrame(self.aba_diretos, text="Resultado", padding=10)
        frame_saida.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.text_saida_diretos = scrolledtext.ScrolledText(frame_saida, height=12,
                                                           bg=self.CORES['bg_secundario'],
                                                           fg=self.CORES['texto_principal'],
                                                           state='disabled')
        self.text_saida_diretos.pack(fill='both', expand=True)
        
    def _popular_aba_iterativos(self):
        """Popula a aba de Métodos Iterativos"""
        # Frame de entrada
        frame_entrada = ttk.LabelFrame(self.aba_iterativos, text="Entrada de Dados", padding=10)
        frame_entrada.pack(fill='x', padx=10, pady=10)
        
        ttk.Label(frame_entrada, text="Matriz A:").pack(anchor='w')
        self.text_matriz_iter = scrolledtext.ScrolledText(frame_entrada, height=4, width=60,
                                                         bg=self.CORES['bg_input'],
                                                         fg=self.CORES['texto_principal'])
        self.text_matriz_iter.pack(fill='x', pady=(5, 10))
        self.text_matriz_iter.insert('1.0', "10, -1, -1, 0, 0\n-1, 15, 0, -2, 0\n-1, 0, 12, -1, 0\n0, -2, -1, 20, -1\n0, 0, 0, -1, 8")
        
        ttk.Label(frame_entrada, text="Vetor b:").pack(anchor='w')
        self.entry_vetor_iter = ttk.Entry(frame_entrada, width=60)
        self.entry_vetor_iter.pack(fill='x', pady=(5, 10))
        self.entry_vetor_iter.insert(0, "12, 25, 10, 30, 15")
        
        # Parâmetros
        frame_params = ttk.Frame(frame_entrada)
        frame_params.pack(fill='x', pady=10)
        
        ttk.Label(frame_params, text="Tolerância:").pack(side='left', padx=5)
        self.entry_tol = ttk.Entry(frame_params, width=10)
        self.entry_tol.pack(side='left', padx=5)
        self.entry_tol.insert(0, "0.0001")
        
        ttk.Label(frame_params, text="Máx. Iterações:").pack(side='left', padx=5)
        self.entry_max_iter = ttk.Entry(frame_params, width=10)
        self.entry_max_iter.pack(side='left', padx=5)
        self.entry_max_iter.insert(0, "1000")
        
        # Frame de operações
        frame_operacoes = ttk.LabelFrame(self.aba_iterativos, text="Operações", padding=10)
        frame_operacoes.pack(fill='x', padx=10, pady=10)
        
        ttk.Button(frame_operacoes, text="Gauss-Seidel",
                  command=self._executar_gauss_seidel).pack(side='left', padx=5)
        ttk.Button(frame_operacoes, text="Jacobi",
                  command=self._executar_jacobi).pack(side='left', padx=5)
        ttk.Button(frame_operacoes, text="Limpar",
                  command=self._limpar_iterativos).pack(side='left', padx=5)
        
        # Frame de saída
        frame_saida = ttk.LabelFrame(self.aba_iterativos, text="Resultado", padding=10)
        frame_saida.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.text_saida_iterativos = scrolledtext.ScrolledText(frame_saida, height=12,
                                                              bg=self.CORES['bg_secundario'],
                                                              fg=self.CORES['texto_principal'],
                                                              state='disabled')
        self.text_saida_iterativos.pack(fill='both', expand=True)
        
    def _popular_aba_interpolacao(self):
        """Popula a aba de Interpolação e Mínimos Quadrados"""
        # Frame de entrada
        frame_entrada = ttk.LabelFrame(self.aba_interpolacao, text="Entrada de Dados", padding=10)
        frame_entrada.pack(fill='x', padx=10, pady=10)
        
        ttk.Label(frame_entrada, text="Pontos X (separados por vírgula):").pack(anchor='w')
        self.entry_x_interp = ttk.Entry(frame_entrada, width=60)
        self.entry_x_interp.pack(fill='x', pady=(5, 10))
        self.entry_x_interp.insert(0, "1, 2, 3, 4, 5")
        
        ttk.Label(frame_entrada, text="Pontos Y (separados por vírgula):").pack(anchor='w')
        self.entry_y_interp = ttk.Entry(frame_entrada, width=60)
        self.entry_y_interp.pack(fill='x', pady=(5, 10))
        self.entry_y_interp.insert(0, "2.0, 2.3, 2.8, 3.1, 3.5")
        
        ttk.Label(frame_entrada, text="Ponto para avaliar:").pack(anchor='w')
        self.entry_x_eval = ttk.Entry(frame_entrada, width=20)
        self.entry_x_eval.pack(fill='x', pady=(5, 10))
        self.entry_x_eval.insert(0, "2.5")
        
        # Frame de operações
        frame_operacoes = ttk.LabelFrame(self.aba_interpolacao, text="Operações", padding=10)
        frame_operacoes.pack(fill='x', padx=10, pady=10)
        
        ttk.Button(frame_operacoes, text="Interpolação Lagrange",
                  command=self._executar_lagrange).pack(side='left', padx=5)
        ttk.Button(frame_operacoes, text="Mínimos Quadrados",
                  command=self._executar_minimos_quadrados).pack(side='left', padx=5)
        ttk.Button(frame_operacoes, text="Limpar",
                  command=self._limpar_interpolacao).pack(side='left', padx=5)
        
        # Frame de saída
        frame_saida = ttk.LabelFrame(self.aba_interpolacao, text="Resultado", padding=10)
        frame_saida.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.text_saida_interpolacao = scrolledtext.ScrolledText(frame_saida, height=12,
                                                                bg=self.CORES['bg_secundario'],
                                                                fg=self.CORES['texto_principal'],
                                                                state='disabled')
        self.text_saida_interpolacao.pack(fill='both', expand=True)
        
    def _popular_aba_integracao(self):
        """Popula a aba de Integração Numérica"""
        # Frame de entrada
        frame_entrada = ttk.LabelFrame(self.aba_integracao, text="Entrada de Dados", padding=10)
        frame_entrada.pack(fill='x', padx=10, pady=10)
        
        ttk.Label(frame_entrada, text="Limite inferior (a):").pack(anchor='w')
        self.entry_a = ttk.Entry(frame_entrada, width=20)
        self.entry_a.pack(fill='x', pady=(5, 10))
        self.entry_a.insert(0, "0")
        
        ttk.Label(frame_entrada, text="Limite superior (b):").pack(anchor='w')
        self.entry_b = ttk.Entry(frame_entrada, width=20)
        self.entry_b.pack(fill='x', pady=(5, 10))
        self.entry_b.insert(0, "1")
        
        ttk.Label(frame_entrada, text="Número de intervalos (n):").pack(anchor='w')
        self.entry_n_int = ttk.Entry(frame_entrada, width=20)
        self.entry_n_int.pack(fill='x', pady=(5, 10))
        self.entry_n_int.insert(0, "100")
        
        # Frame de operações
        frame_operacoes = ttk.LabelFrame(self.aba_integracao, text="Operações", padding=10)
        frame_operacoes.pack(fill='x', padx=10, pady=10)
        
        ttk.Button(frame_operacoes, text="Trapézio",
                  command=self._executar_trapezio).pack(side='left', padx=5)
        ttk.Button(frame_operacoes, text="Simpson",
                  command=self._executar_simpson).pack(side='left', padx=5)
        ttk.Button(frame_operacoes, text="Limpar",
                  command=self._limpar_integracao).pack(side='left', padx=5)
        
        # Frame de saída
        frame_saida = ttk.LabelFrame(self.aba_integracao, text="Resultado", padding=10)
        frame_saida.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.text_saida_integracao = scrolledtext.ScrolledText(frame_saida, height=12,
                                                              bg=self.CORES['bg_secundario'],
                                                              fg=self.CORES['texto_principal'],
                                                              state='disabled')
        self.text_saida_integracao.pack(fill='both', expand=True)
    
    # =====================================================================
    # MÉTODOS DIRETOS
    # =====================================================================
    
    def _executar_gauss(self):
        """Executa eliminação de Gauss"""
        try:
            A = self._parsear_matriz(self.text_matriz_a.get('1.0', 'end'))
            b = self._parsear_vetor(self.entry_vetor_b.get())
            
            x = md.eliminacao_gauss(A.copy(), b.copy())
            
            self._exibir_resultado_diretos(f"✓ ELIMINAÇÃO DE GAUSS\n\n"
                                          f"Solução:\n{self._formatar_solucao(x)}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro na execução: {str(e)}")
    
    def _executar_lu(self):
        """Executa fatoração LU"""
        try:
            A = self._parsear_matriz(self.text_matriz_a.get('1.0', 'end'))
            b = self._parsear_vetor(self.entry_vetor_b.get())
            
            L, U, x = md.fatoracao_lu(A.copy(), b.copy())
            
            resultado = f"✓ FATORAÇÃO LU\n\n"
            resultado += f"Matriz L:\n{self._formatar_matriz(L)}\n"
            resultado += f"Matriz U:\n{self._formatar_matriz(U)}\n"
            resultado += f"Solução:\n{self._formatar_solucao(x)}"
            
            self._exibir_resultado_diretos(resultado)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro na execução: {str(e)}")
    
    def _limpar_diretos(self):
        """Limpa a saída de métodos diretos"""
        self.text_saida_diretos.config(state='normal')
        self.text_saida_diretos.delete('1.0', 'end')
        self.text_saida_diretos.config(state='disabled')
    
    # =====================================================================
    # MÉTODOS ITERATIVOS
    # =====================================================================
    
    def _executar_gauss_seidel(self):
        """Executa Gauss-Seidel"""
        try:
            A = self._parsear_matriz(self.text_matriz_iter.get('1.0', 'end'))
            b = self._parsear_vetor(self.entry_vetor_iter.get())
            tol = float(self.entry_tol.get())
            max_iter = int(self.entry_max_iter.get())
            
            x, iter_count, historico = mi.metodo_gauss_seidel(A, b, tol=tol, max_iter=max_iter)
            
            resultado = f"✓ GAUSS-SEIDEL\n\n"
            resultado += f"Iterações: {iter_count}\n"
            resultado += f"Tolerância: {tol}\n\n"
            resultado += f"Solução:\n{self._formatar_solucao(x)}"
            
            self._exibir_resultado_iterativos(resultado)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro na execução: {str(e)}")
    
    def _executar_jacobi(self):
        """Executa método de Jacobi"""
        try:
            A = self._parsear_matriz(self.text_matriz_iter.get('1.0', 'end'))
            b = self._parsear_vetor(self.entry_vetor_iter.get())
            tol = float(self.entry_tol.get())
            max_iter = int(self.entry_max_iter.get())
            
            x, iter_count, historico = mi.metodo_jacobi(A, b, tol=tol, max_iter=max_iter)
            
            resultado = f"✓ JACOBI\n\n"
            resultado += f"Iterações: {iter_count}\n"
            resultado += f"Tolerância: {tol}\n\n"
            resultado += f"Solução:\n{self._formatar_solucao(x)}"
            
            self._exibir_resultado_iterativos(resultado)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro na execução: {str(e)}")
    
    def _limpar_iterativos(self):
        """Limpa a saída de métodos iterativos"""
        self.text_saida_iterativos.config(state='normal')
        self.text_saida_iterativos.delete('1.0', 'end')
        self.text_saida_iterativos.config(state='disabled')
    
    # =====================================================================
    # INTERPOLAÇÃO
    # =====================================================================
    
    def _executar_lagrange(self):
        """Executa interpolação de Lagrange"""
        try:
            x_dados = self._parsear_vetor(self.entry_x_interp.get())
            y_dados = self._parsear_vetor(self.entry_y_interp.get())
            x_eval = float(self.entry_x_eval.get())
            
            y_eval = imq.interpolacao_lagrange(x_dados, y_dados, x_eval)
            
            resultado = f"✓ INTERPOLAÇÃO DE LAGRANGE\n\n"
            resultado += f"Ponto avaliado: x = {x_eval}\n"
            resultado += f"Valor interpolado: y = {y_eval:.6f}"
            
            self._exibir_resultado_interpolacao(resultado)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro na execução: {str(e)}")
    
    def _executar_minimos_quadrados(self):
        """Executa regressão por mínimos quadrados"""
        try:
            x_dados = self._parsear_vetor(self.entry_x_interp.get())
            y_dados = self._parsear_vetor(self.entry_y_interp.get())
            x_eval = float(self.entry_x_eval.get())
            
            a, b_coef = imq.minimos_quadrados(x_dados, y_dados)
            y_eval = a + b_coef * x_eval
            
            resultado = f"✓ MÍNIMOS QUADRADOS\n\n"
            resultado += f"Reta ajustada: y = {a:.6f} + {b_coef:.6f}x\n\n"
            resultado += f"Ponto avaliado: x = {x_eval}\n"
            resultado += f"Valor: y = {y_eval:.6f}"
            
            self._exibir_resultado_interpolacao(resultado)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro na execução: {str(e)}")
    
    def _limpar_interpolacao(self):
        """Limpa a saída de interpolação"""
        self.text_saida_interpolacao.config(state='normal')
        self.text_saida_interpolacao.delete('1.0', 'end')
        self.text_saida_interpolacao.config(state='disabled')
    
    # =====================================================================
    # INTEGRAÇÃO NUMÉRICA
    # =====================================================================
    
    def _executar_trapezio(self):
        """Executa integração por trapézio"""
        try:
            a = float(self.entry_a.get())
            b = float(self.entry_b.get())
            n = int(self.entry_n_int.get())
            
            resultado_int = intn.metodo_trapezio(a, b, n)
            
            resultado = f"✓ MÉTODO DO TRAPÉZIO\n\n"
            resultado += f"Intervalo: [{a}, {b}]\n"
            resultado += f"Número de intervalos: {n}\n"
            resultado += f"Resultado: {resultado_int:.8f}"
            
            self._exibir_resultado_integracao(resultado)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro na execução: {str(e)}")
    
    def _executar_simpson(self):
        """Executa integração por Simpson"""
        try:
            a = float(self.entry_a.get())
            b = float(self.entry_b.get())
            n = int(self.entry_n_int.get())
            
            resultado_int = intn.metodo_simpson(a, b, n)
            
            resultado = f"✓ MÉTODO DE SIMPSON\n\n"
            resultado += f"Intervalo: [{a}, {b}]\n"
            resultado += f"Número de intervalos: {n}\n"
            resultado += f"Resultado: {resultado_int:.8f}"
            
            self._exibir_resultado_integracao(resultado)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro na execução: {str(e)}")
    
    def _limpar_integracao(self):
        """Limpa a saída de integração"""
        self.text_saida_integracao.config(state='normal')
        self.text_saida_integracao.delete('1.0', 'end')
        self.text_saida_integracao.config(state='disabled')
    
    # =====================================================================
    # UTILITÁRIOS
    # =====================================================================
    
    def _parsear_matriz(self, texto):
        """Converte texto em matriz numpy"""
        linhas = [linha.strip() for linha in texto.strip().split('\n') if linha.strip()]
        matriz = []
        for linha in linhas:
            elementos = [float(x.strip()) for x in linha.split(',')]
            matriz.append(elementos)
        return np.array(matriz, dtype=float)
    
    def _parsear_vetor(self, texto):
        """Converte texto em vetor numpy"""
        elementos = [float(x.strip()) for x in texto.split(',')]
        return np.array(elementos, dtype=float)
    
    def _formatar_solucao(self, x):
        """Formata um vetor solução para exibição"""
        resultado = ""
        for i, valor in enumerate(x):
            resultado += f"  x[{i}] = {valor:12.8f}\n"
        return resultado
    
    def _formatar_matriz(self, M):
        """Formata uma matriz para exibição"""
        resultado = ""
        for linha in M:
            resultado += "  " + "  ".join(f"{x:10.6f}" for x in linha) + "\n"
        return resultado
    
    def _exibir_resultado_diretos(self, texto):
        """Exibe resultado em métodos diretos"""
        self.text_saida_diretos.config(state='normal')
        self.text_saida_diretos.delete('1.0', 'end')
        self.text_saida_diretos.insert('1.0', texto)
        self.text_saida_diretos.config(state='disabled')
    
    def _exibir_resultado_iterativos(self, texto):
        """Exibe resultado em métodos iterativos"""
        self.text_saida_iterativos.config(state='normal')
        self.text_saida_iterativos.delete('1.0', 'end')
        self.text_saida_iterativos.insert('1.0', texto)
        self.text_saida_iterativos.config(state='disabled')
    
    def _exibir_resultado_interpolacao(self, texto):
        """Exibe resultado em interpolação"""
        self.text_saida_interpolacao.config(state='normal')
        self.text_saida_interpolacao.delete('1.0', 'end')
        self.text_saida_interpolacao.insert('1.0', texto)
        self.text_saida_interpolacao.config(state='disabled')
    
    def _exibir_resultado_integracao(self, texto):
        """Exibe resultado em integração"""
        self.text_saida_integracao.config(state='normal')
        self.text_saida_integracao.delete('1.0', 'end')
        self.text_saida_integracao.insert('1.0', texto)
        self.text_saida_integracao.config(state='disabled')


def main():
    """Função principal"""
    janela = tk.Tk()
    app = CalculoNumericoGUI(janela)
    janela.mainloop()


if __name__ == "__main__":
    main()
