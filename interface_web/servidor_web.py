"""
SERVIDOR BACKEND FLASK - Interface Web para Cálculo Numérico
API REST para comunicação entre frontend HTML/JS e módulos Python
"""

import sys
import os
# Adicionar pasta 'metodos' ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'metodos'))

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import numpy as np
import metodos_diretos as md
import metodos_iterativos as mi
import interpolacao_minimos_quadrados as imq
import integracao_numerica as intn

app = Flask(__name__)
CORS(app)  # Permitir requisições do frontend

# ===================================
# ROTA PARA SERVIR A INTERFACE
# ===================================

@app.route('/')
def index():
    """Serve a interface HTML"""
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    """Serve arquivos estáticos (CSS, JS)"""
    return send_from_directory('.', filename)

# ===================================
# ROTAS - MÉTODOS DIRETOS
# ===================================

@app.route('/gauss', methods=['POST'])
def gauss():
    """Eliminação de Gauss"""
    try:
        dados = request.json
        A = np.array(dados['A'], dtype=float)
        b = np.array(dados['b'], dtype=float)
        
        x = md.eliminacao_gauss(A.copy(), b.copy())
        
        return jsonify({
            'x': x.tolist(),
            'sucesso': True
        })
    except Exception as e:
        return jsonify({
            'erro': str(e),
            'sucesso': False
        })

@app.route('/lu', methods=['POST'])
def lu():
    """Fatoração LU"""
    try:
        dados = request.json
        A = np.array(dados['A'], dtype=float)
        b = np.array(dados['b'], dtype=float)
        
        # Decompor A em L e U
        L, U = md.decomposicao_lu(A.copy())
        # Resolver o sistema usando L e U
        x = md.resolver_lu(L, U, b)
        
        return jsonify({
            'L': L.tolist(),
            'U': U.tolist(),
            'x': x.tolist(),
            'sucesso': True
        })
    except Exception as e:
        return jsonify({
            'erro': str(e),
            'sucesso': False
        })

# ===================================
# ROTAS - MÉTODOS ITERATIVOS
# ===================================

@app.route('/gauss-seidel', methods=['POST'])
def gauss_seidel():
    """Método de Gauss-Seidel"""
    try:
        dados = request.json
        A = np.array(dados['A'], dtype=float)
        b = np.array(dados['b'], dtype=float)
        tol = dados.get('tol', 0.0001)
        max_iter = dados.get('maxIter', 1000)
        
        x, iteracoes, historico = mi.metodo_gauss_seidel(A, b, tol=tol, max_iter=max_iter)
        
        return jsonify({
            'x': x.tolist(),
            'iteracoes': iteracoes,
            'sucesso': True
        })
    except Exception as e:
        return jsonify({
            'erro': str(e),
            'sucesso': False
        })

@app.route('/jacobi', methods=['POST'])
def jacobi():
    """Método de Jacobi"""
    try:
        dados = request.json
        A = np.array(dados['A'], dtype=float)
        b = np.array(dados['b'], dtype=float)
        tol = dados.get('tol', 0.0001)
        max_iter = dados.get('maxIter', 1000)
        
        x, iteracoes, historico = mi.metodo_jacobi(A, b, tol=tol, max_iter=max_iter)
        
        return jsonify({
            'x': x.tolist(),
            'iteracoes': iteracoes,
            'sucesso': True
        })
    except Exception as e:
        return jsonify({
            'erro': str(e),
            'sucesso': False
        })

# ===================================
# ROTAS - INTERPOLAÇÃO
# ===================================

@app.route('/lagrange', methods=['POST'])
def lagrange():
    """Interpolação de Lagrange"""
    try:
        dados = request.json
        x = np.array(dados['x'], dtype=float)
        y = np.array(dados['y'], dtype=float)
        x_eval = float(dados['xEval'])
        
        # Criar função interpoladora e avaliar no ponto
        P = imq.interpolacao_lagrange(x, y)
        y_eval = P(x_eval)
        
        return jsonify({
            'yEval': float(y_eval),
            'sucesso': True
        })
    except Exception as e:
        return jsonify({
            'erro': str(e),
            'sucesso': False
        })

@app.route('/minimos-quadrados', methods=['POST'])
def minimos_quadrados():
    """Método dos Mínimos Quadrados"""
    try:
        dados = request.json
        x = np.array(dados['x'], dtype=float)
        y = np.array(dados['y'], dtype=float)
        x_eval = float(dados['xEval'])
        
        a, b_coef = imq.minimos_quadrados_linear(x, y)
        y_eval = a + b_coef * x_eval
        
        return jsonify({
            'a': float(a),
            'b': float(b_coef),
            'yEval': float(y_eval),
            'sucesso': True
        })
    except Exception as e:
        return jsonify({
            'erro': str(e),
            'sucesso': False
        })

# ===================================
# ROTAS - INTEGRAÇÃO NUMÉRICA
# ===================================

@app.route('/trapezio', methods=['POST'])
def trapezio():
    """Método do Trapézio"""
    try:
        dados = request.json
        a = float(dados['a'])
        b = float(dados['b'])
        n = int(dados['n'])
        
        # Função padrão para integrar (exemplo: x^2)
        def f(x):
            return x**2
        
        resultado = intn.regra_trapezio(f, a, b, n)
        
        return jsonify({
            'valor': float(resultado),
            'sucesso': True
        })
    except Exception as e:
        return jsonify({
            'erro': str(e),
            'sucesso': False
        })

@app.route('/simpson', methods=['POST'])
def simpson():
    """Método de Simpson"""
    try:
        dados = request.json
        a = float(dados['a'])
        b = float(dados['b'])
        n = int(dados['n'])
        
        # Função padrão para integrar (exemplo: x^2)
        def f(x):
            return x**2
        
        resultado = intn.regra_simpson_1_3(f, a, b, n)
        
        return jsonify({
            'valor': float(resultado),
            'sucesso': True
        })
    except Exception as e:
        return jsonify({
            'erro': str(e),
            'sucesso': False
        })

# ===================================
# INICIALIZAÇÃO
# ===================================

if __name__ == '__main__':
    print("=" * 60)
    print("🚀 SERVIDOR BACKEND - CÁLCULO NUMÉRICO")
    print("=" * 60)
    print("📡 Servidor rodando em: http://localhost:5000")
    print("🌐 Acesse http://localhost:5000 no navegador")
    print("=" * 60)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
