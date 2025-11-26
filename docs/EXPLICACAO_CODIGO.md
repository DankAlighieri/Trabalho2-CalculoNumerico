# 💻 EXPLICAÇÃO DO CÓDIGO - Métodos Numéricos

## 📋 Índice
1. [Visão Geral](#visão-geral)
2. [Métodos Diretos - Código Detalhado](#métodos-diretos)
3. [Métodos Iterativos - Código Detalhado](#métodos-iterativos)
4. [Estruturas de Dados](#estruturas-de-dados)
5. [Fluxo de Execução](#fluxo-de-execução)

---

## 🎯 VISÃO GERAL

### Organização dos Arquivos
```
metodos/
├── metodos_diretos.py          # Gauss, LU, Gauss-Jordan
├── metodos_iterativos.py       # Jacobi, Gauss-Seidel
├── interpolacao_minimos_quadrados.py
└── integracao_numerica.py
```

### Bibliotecas Utilizadas
```python
import numpy as np              # Operações matriciais eficientes
from typing import Tuple, Optional  # Type hints para clareza
```

---

# 🔧 MÉTODOS DIRETOS

## 1️⃣ ELIMINAÇÃO DE GAUSS

### 📖 Teoria
Transforma o sistema **Ax = b** em um sistema triangular superior através de eliminação, depois resolve por substituição retroativa.

### 💻 Implementação

```python
def eliminacao_gauss(A: np.ndarray, b: np.ndarray, pivoteamento: bool = True) -> np.ndarray:
```

#### **Passo 1: Criar Matriz Aumentada [A|b]**
```python
n = len(b)
Ab = np.column_stack([A.astype(float), b.astype(float)])
```

**O que faz:**
- `np.column_stack`: Junta A e b em uma única matriz
- `astype(float)`: Garante precisão de ponto flutuante
- Resultado: Matriz n×(n+1) onde última coluna é b

**Exemplo Visual:**
```
A = [4  3]    b = [24]    →    Ab = [4  3 | 24]
    [3  4]        [27]              [3  4 | 27]
```

---

#### **Passo 2: Fase de Eliminação (Triangularização)**
```python
for k in range(n-1):  # Para cada coluna (exceto última)
```

##### **2a. Pivoteamento Parcial (Opcional mas Recomendado)**
```python
if pivoteamento:
    max_idx = np.argmax(np.abs(Ab[k:n, k])) + k
    if max_idx != k:
        Ab[[k, max_idx]] = Ab[[max_idx, k]]
```

**O que faz:**
- `np.argmax(np.abs(Ab[k:n, k]))`: Encontra linha com maior valor (em módulo) na coluna k
- `Ab[[k, max_idx]] = Ab[[max_idx, k]]`: Troca linhas
- **Por quê?** Evita divisão por números muito pequenos (melhora estabilidade numérica)

**Exemplo:**
```
Antes:          Após Pivoteamento:
[1   2 | 5]     [3   4 | 9]    ← Linha com maior pivô
[3   4 | 9]     [1   2 | 5]
```

##### **2b. Verificação de Pivô Zero**
```python
if abs(Ab[k, k]) < 1e-10:
    raise ValueError(f"Pivô zero encontrado na linha {k}")
```

**O que faz:**
- Verifica se pivô é praticamente zero (< 10⁻¹⁰)
- Se for, matriz é singular → sistema não tem solução única

##### **2c. Eliminação (Coração do Método)**
```python
for i in range(k+1, n):  # Para cada linha abaixo do pivô
    fator = Ab[i, k] / Ab[k, k]  # Calcula multiplicador
    Ab[i, k:] -= fator * Ab[k, k:]  # Elimina elemento
```

**O que faz:**
1. **Calcula fator**: Quantas vezes a linha k cabe na linha i
2. **Elimina**: Subtrai múltiplo da linha k da linha i
3. `Ab[i, k:]`: Atualiza apenas elementos da coluna k em diante (otimização)

**Exemplo Detalhado:**
```
Iteração k=0:
[4   3  | 24]    Linha 0 (pivô)
[3   4  | 27]    Linha 1

Passo 1: fator = 3/4 = 0.75
Passo 2: Linha1 = Linha1 - 0.75 × Linha0
         [3, 4, 27] - 0.75 × [4, 3, 24]
         = [3, 4, 27] - [3, 2.25, 18]
         = [0, 1.75, 9]

Resultado:
[4   3   | 24]
[0   1.75| 9]   ← Triangular!
```

---

#### **Passo 3: Substituição Retroativa (Resolver Sistema Triangular)**
```python
x = np.zeros(n)
for i in range(n-1, -1, -1):  # De baixo para cima
    x[i] = (Ab[i, -1] - np.dot(Ab[i, i+1:n], x[i+1:n])) / Ab[i, i]
```

**O que faz:**
1. Começa da última equação (já resolvida)
2. Substitui valores conhecidos nas equações acima
3. `np.dot(Ab[i, i+1:n], x[i+1:n])`: Produto escalar dos coeficientes com soluções já calculadas

**Exemplo Detalhado:**
```
Sistema Triangular:
[4   3   | 24]    →  4x + 3y = 24
[0   1.75| 9]     →  1.75y = 9

Passo 1 (i=1): y = 9 / 1.75 = 5.14
Passo 2 (i=0): x = (24 - 3×5.14) / 4 = 2.14
```

**Código Equivalente Expandido:**
```python
# Última linha: já está resolvida
x[n-1] = Ab[n-1, -1] / Ab[n-1, n-1]

# Penúltima linha
x[n-2] = (Ab[n-2, -1] - Ab[n-2, n-1] * x[n-1]) / Ab[n-2, n-2]

# E assim por diante...
```

---

## 2️⃣ GAUSS-JORDAN

### 📖 Teoria
Estende Gauss para transformar A em matriz identidade I, eliminando tanto acima quanto abaixo da diagonal.

### 💻 Implementação

```python
def gauss_jordan(A: np.ndarray, b: np.ndarray) -> np.ndarray:
```

#### **Diferença Principal do Gauss:**

**Gauss:** Apenas abaixo do pivô
```python
for i in range(k+1, n):  # Apenas linhas abaixo
```

**Gauss-Jordan:** Acima E abaixo do pivô
```python
for i in range(n):  # TODAS as linhas
    if i != k:      # Exceto a própria linha do pivô
```

#### **Normalização da Linha do Pivô**
```python
Ab[k] = Ab[k] / Ab[k, k]
```

**O que faz:**
- Divide linha inteira pelo elemento diagonal
- Resultado: Elemento diagonal vira 1

**Exemplo:**
```
Antes:  [4   3  | 24]
Depois: [1  0.75|  6]  ← Dividido por 4
```

#### **Eliminação Completa**
```python
for i in range(n):
    if i != k:
        fator = Ab[i, k]
        Ab[i] -= fator * Ab[k]
```

**O que faz:**
- Elimina elemento na coluna k de TODAS as outras linhas
- Diferente do Gauss que só elimina abaixo

**Resultado Final:**
```
[1  0 | x₁]    → x₁ já está na última coluna!
[0  1 | x₂]    → x₂ já está na última coluna!
```

**Por isso não precisa de substituição retroativa!**

---

## 3️⃣ DECOMPOSIÇÃO LU

### 📖 Teoria
Decompõe A em duas matrizes:
- **L** (Lower): Triangular inferior com 1's na diagonal
- **U** (Upper): Triangular superior

**A = LU**

### 💻 Implementação

```python
def decomposicao_lu(A: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
```

#### **Passo 1: Inicialização**
```python
n = A.shape[0]
L = np.eye(n)      # Matriz identidade (L começa com 1's na diagonal)
U = A.copy()        # U começa como cópia de A
```

**Estado Inicial:**
```
L = [1  0  0]      U = [4  3  2]
    [0  1  0]          [3  4  1]
    [0  0  1]          [2  1  5]
```

#### **Passo 2: Algoritmo de Fatoração**
```python
for k in range(n-1):  # Para cada coluna
    for i in range(k+1, n):  # Para cada linha abaixo
        fator = U[i, k] / U[k, k]  # Calcula multiplicador
        L[i, k] = fator             # Guarda em L
        U[i, k:] -= fator * U[k, k:]  # Elimina de U
```

**O que faz:**
1. **Calcula fator**: Mesmo que Gauss
2. **Armazena em L**: Guarda os multiplicadores (diferença chave!)
3. **Atualiza U**: Faz eliminação normalmente

**Exemplo Detalhado (k=0, i=1):**
```
Iteração 1:
U = [4  3  2]     L = [1  0  0]
    [3  4  1]         [0  1  0]
    [2  1  5]         [0  0  1]

Passo 1: fator = 3/4 = 0.75
Passo 2: L[1,0] = 0.75  ← Guarda multiplicador
Passo 3: U[1,:] -= 0.75 × U[0,:]

Resultado:
U = [4    3    2  ]    L = [1    0  0]
    [0  1.75 -0.5 ]        [0.75 1  0]  ← Fator guardado
    [2    1    5  ]        [0    0  1]
```

**Após todas iterações:**
```
L = [1    0    0]    U = [4   3     2  ]
    [0.75 1    0]        [0  1.75 -0.5 ]
    [0.5  0.29 1]        [0   0    4.14]
```

**Verificação:** `L @ U = A` ✓

---

#### **Função Auxiliar: Resolver com LU**

```python
def resolver_lu(L: np.ndarray, U: np.ndarray, b: np.ndarray) -> np.ndarray:
```

**Estratégia:** Resolver em duas etapas:
1. **Ly = b** (substituição progressiva)
2. **Ux = y** (substituição retroativa)

##### **Etapa 1: Substituição Progressiva (Resolver Ly = b)**
```python
y = np.zeros(n)
for i in range(n):  # De CIMA para BAIXO
    y[i] = (b[i] - np.dot(L[i, :i], y[:i])) / L[i, i]
```

**O que faz:**
- Similar à retroativa, mas de cima para baixo
- Resolve sistema triangular inferior

**Exemplo:**
```
L = [1   0]    b = [24]
    [0.75 1]       [27]

i=0: y[0] = 24 / 1 = 24
i=1: y[1] = (27 - 0.75×24) / 1 = 9
```

##### **Etapa 2: Substituição Retroativa (Resolver Ux = y)**
```python
x = np.zeros(n)
for i in range(n-1, -1, -1):  # De BAIXO para CIMA
    x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]
```

**Igual ao Gauss!**

---

# 🔄 MÉTODOS ITERATIVOS

## 1️⃣ MÉTODO DE JACOBI

### 📖 Teoria
Isola cada variável e atualiza todas simultaneamente usando valores da iteração anterior.

**Fórmula:**
```
x[i]^(k+1) = (b[i] - Σ(A[i,j] × x[j]^(k))) / A[i,i]
                    j≠i
```

### 💻 Implementação

```python
def metodo_jacobi(A, b, x0=None, tol=1e-6, max_iter=1000):
```

#### **Passo 1: Inicialização**
```python
n = len(b)
x = np.zeros(n) if x0 is None else x0.copy()
x_new = np.zeros(n)  # Array separado para novos valores
erros = []
```

**Por que dois arrays?**
- `x`: Valores da iteração anterior (k)
- `x_new`: Valores da iteração atual (k+1)
- **Jacobi usa SEMPRE valores de x[k]** para calcular x[k+1]

---

#### **Passo 2: Loop de Iterações**
```python
for k in range(max_iter):
    for i in range(n):  # Para cada equação
```

#### **Passo 3: Calcular Nova Aproximação**
```python
soma = sum(A[i, j] * x[j] for j in range(n) if j != i)
x_new[i] = (b[i] - soma) / A[i, i]
```

**O que faz:**
1. **soma**: Calcula Σ(A[i,j] × x[j]) para j ≠ i
2. **x_new[i]**: Isola x[i] na equação i

**Exemplo Detalhado:**
```
Sistema:
10x - y + 2z = 6    → x = (6 + y - 2z) / 10
-x + 11y - z + 3w = 25  → y = (25 + x + z - 3w) / 11

Iteração k=0: x=[0, 0, 0, 0]
  i=0: soma = -1×0 + 2×0 = 0
       x_new[0] = (6 - 0) / 10 = 0.6
  
  i=1: soma = -1×0 + (-1)×0 + 3×0 = 0
       x_new[1] = (25 - 0) / 11 = 2.27
  ...

Iteração k=1: x=[0.6, 2.27, -1.1, 1.87]
  i=0: soma = -1×2.27 + 2×(-1.1) = -4.47
       x_new[0] = (6 - (-4.47)) / 10 = 1.047
  ...
```

**Nota:** Todos os x_new são calculados usando o MESMO x (da iteração anterior)!

---

#### **Passo 4: Verificar Convergência**
```python
erro = np.linalg.norm(x_new - x) / np.linalg.norm(x_new)
erros.append(erro)

if erro < tol:
    return x_new, k + 1, erros

x = x_new.copy()  # Prepara para próxima iteração
```

**O que faz:**
- **Erro Relativo**: ||x[k+1] - x[k]|| / ||x[k+1]||
- `np.linalg.norm`: Calcula norma euclidiana (distância)
- Se erro < tolerância → **CONVERGIU!**
- Senão, copia x_new para x e continua

**Interpretação:**
```
Erro = 0.1  → Mudou 10% entre iterações (longe da solução)
Erro = 1e-6 → Mudou 0.0001% (praticamente parado = convergiu)
```

---

## 2️⃣ MÉTODO DE GAUSS-SEIDEL

### 📖 Teoria
Similar ao Jacobi, mas usa valores **já atualizados** na mesma iteração.

### 💻 Implementação

```python
def metodo_gauss_seidel(A, b, x0=None, tol=1e-6, max_iter=1000):
```

#### **Diferença Chave do Jacobi:**

**Jacobi:**
```python
x_new = np.zeros(n)  # Array separado
# ...
soma = sum(A[i, j] * x[j] for ...)  # Sempre usa x (antigo)
x_new[i] = ...
```

**Gauss-Seidel:**
```python
x = np.zeros(n)  # UM único array
x_old = x.copy()  # Cópia apenas para calcular erro
# ...
soma = sum(A[i, j] * x[j] for ...)  # Usa x (pode ter novos valores!)
x[i] = ...  # Atualiza x IMEDIATAMENTE
```

#### **Coração do Método**
```python
for k in range(max_iter):
    for i in range(n):
        soma = sum(A[i, j] * x[j] for j in range(n) if j != i)
        x[i] = (b[i] - soma) / A[i, i]  # Sobrescreve x[i]!
```

**O que faz:**
- Atualiza `x[i]` **imediatamente**
- Próximas equações já usam o novo valor!

**Exemplo Comparativo:**
```
Sistema: 10x - y = 6
         -x + 10y = 25

JACOBI (iteração k):
  x_new = (6 + y_old) / 10
  y_new = (25 + x_old) / 10  ← Usa x_old
  
GAUSS-SEIDEL (iteração k):
  x = (6 + y_old) / 10
  y = (25 + x) / 10          ← Usa x NOVO!
```

**Por isso Gauss-Seidel converge ~2× mais rápido!**

---

## 🔍 VERIFICAÇÃO DE CONVERGÊNCIA

### Dominância Diagonal

```python
def verificar_convergencia_diagonal(A: np.ndarray) -> bool:
    n = A.shape[0]
    for i in range(n):
        diagonal = abs(A[i, i])
        soma_linha = sum(abs(A[i, j]) for j in range(n) if j != i)
        if diagonal <= soma_linha:
            return False
    return True
```

**O que verifica:**
Para cada linha i:
```
|A[i,i]| > Σ|A[i,j]|  (j ≠ i)
```

**Exemplo:**
```
Linha 0: |10| > |-1| + |2| + |0| → 10 > 3 ✓
Linha 1: |11| > |-1| + |-1| + |3| → 11 > 5 ✓
→ Diagonalmente dominante → CONVERGE!
```

---

## 📊 ESTRUTURAS DE DADOS

### NumPy Arrays

```python
# Criação
A = np.array([[1, 2], [3, 4]], dtype=float)

# Slicing
Ab[i, k:]     # Linha i da coluna k em diante
Ab[k:n, k]    # Coluna k da linha k em diante
Ab[:, -1]     # Última coluna inteira

# Operações vetorizadas
Ab[i] -= fator * Ab[k]  # Subtrai linha inteira (RÁPIDO!)

# Normas
np.linalg.norm(v)  # Norma euclidiana: √(Σv[i]²)

# Produto escalar
np.dot(a, b)  # Σ(a[i] × b[i])
```

---

## 🎯 FLUXO DE EXECUÇÃO COMPLETO

### Exemplo: Eliminação de Gauss

```
INPUT: A = [[4,3], [3,4]], b = [24, 27]

1. Criar Matriz Aumentada:
   Ab = [[4, 3, 24],
         [3, 4, 27]]

2. Pivoteamento:
   max(|4|, |3|) = 4 → Não troca linhas

3. Eliminação (k=0):
   fator = 3/4 = 0.75
   Ab[1] -= 0.75 × Ab[0]
   Ab = [[4, 3, 24],
         [0, 1.75, 9]]

4. Substituição Retroativa:
   i=1: x[1] = 9/1.75 = 5.14
   i=0: x[0] = (24 - 3×5.14)/4 = 2.14

OUTPUT: x = [2.14, 5.14]

VERIFICAÇÃO: A @ x = [24, 27] ✓
```

---

### Exemplo: Método de Jacobi

```
INPUT: A = [[10,-1], [-1,10]], b = [6,25], tol=1e-2

Iteração 0: x = [0, 0]
  x_new[0] = (6 - (-1)×0) / 10 = 0.6
  x_new[1] = (25 - (-1)×0) / 10 = 2.5
  erro = ||(0.6, 2.5) - (0, 0)|| / ||(0.6, 2.5)|| = 1.0

Iteração 1: x = [0.6, 2.5]
  x_new[0] = (6 - (-1)×2.5) / 10 = 0.85
  x_new[1] = (25 - (-1)×0.6) / 10 = 2.56
  erro = 0.098

Iteração 2: x = [0.85, 2.56]
  x_new[0] = 0.856
  x_new[1] = 2.585
  erro = 0.0097 < 0.01 → CONVERGIU!

OUTPUT: x = [0.856, 2.585], iterações = 2
```

---

## 💡 OTIMIZAÇÕES E BOAS PRÁTICAS

### 1. Operações Vetorizadas
```python
# LENTO (loop Python)
for j in range(n):
    soma += A[i, j] * x[j]

# RÁPIDO (NumPy)
soma = np.dot(A[i, :], x)
```

### 2. Slicing Eficiente
```python
# Atualiza apenas elementos necessários
Ab[i, k:] -= fator * Ab[k, k:]  # Não toca colunas 0 até k-1
```

### 3. Copy vs View
```python
U = A.copy()     # Cópia real (não afeta A)
U = A            # Referência (modificar U modifica A!)
```

### 4. Type Hints
```python
def funcao(A: np.ndarray, tol: float = 1e-6) -> Tuple[np.ndarray, int]:
    # Clareza sobre tipos esperados e retornados
```

---

## 🐛 TRATAMENTO DE ERROS

### Pivô Zero
```python
if abs(Ab[k, k]) < 1e-10:
    raise ValueError("Pivô zero encontrado")
```
**Causa:** Matriz singular ou mal-condicionada

### Não Convergência
```python
if k >= max_iter:
    print("Aviso: Número máximo de iterações atingido")
    return x, max_iter, erros
```
**Causa:** Matriz não satisfaz critério de convergência

---

## 📈 ANÁLISE DE COMPLEXIDADE

### Operações Dominantes

**Eliminação de Gauss:**
```python
for k in range(n):        # n iterações
    for i in range(n):    # n iterações
        for j in range(n):  # n operações (implícito no slicing)
            # Ab[i, k:] -= ...
```
**Total:** n³/3 operações → **O(n³)**

**Método de Jacobi (por iteração):**
```python
for i in range(n):      # n iterações
    for j in range(n):  # n operações
        soma += A[i,j] * x[j]
```
**Total:** n² operações por iteração → **O(n²k)** onde k = número de iterações

---

## 🎓 RESUMO

### Métodos Diretos
- **Transformam** o sistema até a solução
- **Número fixo** de operações
- **Código:** Loops aninhados com slicing eficiente
- **Chave:** Matriz aumentada + eliminação + substituição

### Métodos Iterativos
- **Refinam** aproximação gradualmente
- **Número variável** de iterações
- **Código:** Loop de iteração + critério de parada
- **Chave:** Atualização sequencial/paralela + tolerância

---

**Documento criado para:** Entendimento profundo da implementação  
**Nível:** Intermediário/Avançado  
**Data:** Novembro 2025
