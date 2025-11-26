# 📚 EXPLICAÇÃO DOS MÉTODOS NUMÉRICOS

## 📖 Índice
1. [Métodos Diretos](#métodos-diretos)
2. [Métodos Iterativos](#métodos-iterativos)
3. [Comparação e Quando Usar](#comparação)

---

## 🎯 MÉTODOS DIRETOS

Os **métodos diretos** resolvem sistemas lineares **Ax = b** através de um **número finito de operações**, chegando à solução exata (exceto por erros de arredondamento).

### 1️⃣ Eliminação de Gauss

**O que faz:**
- Transforma o sistema em um sistema triangular superior
- Resolve por substituição retroativa

**Como funciona:**
```
Sistema Original:        Após Eliminação:
2x + 3y = 8             2x + 3y = 8
4x + 7y = 18            →    y = 2
```

**Passos:**
1. **Triangularização**: Elimina elementos abaixo da diagonal principal
2. **Substituição Retroativa**: Resolve de baixo para cima

**Vantagens:**
✅ Simples de implementar
✅ Solução exata (sem iterações)
✅ Funciona para a maioria dos sistemas

**Desvantagens:**
❌ Pode ter problemas com pivôs pequenos
❌ Custo computacional: O(n³)
❌ Acumula erros de arredondamento

**Quando usar:**
- Sistemas pequenos a médios (até ~1000 equações)
- Quando precisa de solução exata
- Sistema bem-condicionado

---

### 2️⃣ Decomposição LU (Fatoração LU)

**O que faz:**
- Decompõe a matriz A em duas matrizes:
  - **L** (Lower): Triangular inferior
  - **U** (Upper): Triangular superior
- A = LU

**Como funciona:**
```
Ax = b  →  LUx = b

Passo 1: Ly = b  (resolve y)
Passo 2: Ux = y  (resolve x)
```

**Exemplo:**
```
A = [4  3]  =  [1   0] × [4  3]  = L × U
    [6  3]     [1.5 1]   [0 -1.5]
```

**Vantagens:**
✅ Eficiente para múltiplos vetores b
✅ Reutiliza L e U
✅ Base para outros métodos
✅ Detecta singularidade da matriz

**Desvantagens:**
❌ Mais complexo que Gauss
❌ Requer pivotamento para estabilidade
❌ Custo inicial: O(n³)

**Quando usar:**
- Resolver múltiplos sistemas com mesma matriz A
- Calcular determinante ou inversa
- Base para outros algoritmos

---

### 3️⃣ Gauss-Jordan

**O que faz:**
- Estende Gauss para transformar A em matriz identidade
- Pode calcular a matriz inversa

**Como funciona:**
```
[A | b]  →  [I | x]
```

**Diferença do Gauss:**
- Gauss: Triangular superior
- Gauss-Jordan: Matriz identidade (diagonal)

**Vantagens:**
✅ Calcula matriz inversa diretamente
✅ Não precisa de substituição retroativa
✅ Útil para análise teórica

**Desvantagens:**
❌ Mais operações que Gauss (~50% mais)
❌ Menos eficiente para apenas resolver sistema
❌ Custo: O(n³) com constante maior

**Quando usar:**
- Calcular matriz inversa
- Fins didáticos/teóricos
- Sistemas muito pequenos

---

## 🔄 MÉTODOS ITERATIVOS

Os **métodos iterativos** geram uma **sequência de aproximações** que convergem para a solução. Não garantem solução exata, mas aproximam-se dela.

### 1️⃣ Método de Jacobi

**O que faz:**
- Isola cada variável em sua equação
- Atualiza todas simultaneamente usando valores da iteração anterior

**Fórmula:**
```
x[k+1] = (b - (A - D)x[k]) / D

Onde D = diagonal de A
```

**Algoritmo:**
```python
Para cada iteração k:
    Para cada equação i:
        x_novo[i] = (b[i] - Σ(a[i,j] × x_velho[j])) / a[i,i]
                            j≠i
```

**Exemplo Visual:**
```
Iteração 0: x=0, y=0  (chute inicial)
Iteração 1: x=1.2, y=0.8
Iteração 2: x=1.05, y=0.95
Iteração 3: x=1.01, y=0.99
...
Convergiu: x≈1, y≈1
```

**Vantagens:**
✅ Simples de implementar
✅ Paralelizável (independente)
✅ Baixo uso de memória
✅ Bom para matrizes esparsas grandes

**Desvantagens:**
❌ Convergência mais lenta que Gauss-Seidel
❌ Pode não convergir
❌ Requer critério de parada

**Condição de Convergência:**
- Matriz **diagonalmente dominante**:
  |a[i,i]| > Σ|a[i,j]| para todo i
           j≠i

**Quando usar:**
- Sistemas grandes e esparsos
- Computação paralela
- Matriz diagonalmente dominante
- Memória limitada

---

### 2️⃣ Método de Gauss-Seidel

**O que faz:**
- Similar ao Jacobi, mas usa valores **já atualizados** na mesma iteração
- Converge mais rápido que Jacobi

**Diferença do Jacobi:**
```
Jacobi:       Usa todos os valores de x[k]
Gauss-Seidel: Usa x[k+1] já calculados + x[k] restantes
```

**Algoritmo:**
```python
Para cada iteração k:
    Para cada equação i (em ordem):
        x[i] = (b[i] - Σ(a[i,j] × x[j])) / a[i,i]
                      j≠i
        # Usa x atualizado imediatamente!
```

**Exemplo Comparativo:**
```
JACOBI (paralelo):
x_novo[1] = f(x_velho[1], x_velho[2], x_velho[3])
x_novo[2] = f(x_velho[1], x_velho[2], x_velho[3])
x_novo[3] = f(x_velho[1], x_velho[2], x_velho[3])

GAUSS-SEIDEL (sequencial):
x[1] = f(x_velho[1], x_velho[2], x_velho[3])
x[2] = f(x[1], x_velho[2], x_velho[3])        ← usa x[1] novo!
x[3] = f(x[1], x[2], x_velho[3])              ← usa x[1] e x[2] novos!
```

**Vantagens:**
✅ Converge ~2× mais rápido que Jacobi
✅ Usa menos memória (sobrescreve valores)
✅ Melhor para matrizes simétricas positivas definidas
✅ Não precisa armazenar x_velho

**Desvantagens:**
❌ Não paralelizável (sequencial)
❌ Ordem das equações afeta convergência
❌ Pode não convergir

**Condição de Convergência:**
- Matriz **diagonalmente dominante** (suficiente)
- Matriz **simétrica positiva definida** (suficiente)

**Quando usar:**
- Quando Jacobi for aplicável mas quiser mais velocidade
- Sistemas grandes e esparsos
- Matriz simétrica positiva definida
- Computação sequencial

---

## ⚖️ COMPARAÇÃO: DIRETOS vs ITERATIVOS

### 📊 Tabela Comparativa

| Critério | Métodos Diretos | Métodos Iterativos |
|----------|----------------|-------------------|
| **Número de operações** | Fixo (finito) | Variável (até convergir) |
| **Solução** | Exata* | Aproximada |
| **Complexidade** | O(n³) | O(n²) por iteração |
| **Memória** | O(n²) | O(n) |
| **Erros** | Arredondamento acumula | Controlável por tolerância |
| **Garantia** | Sempre funciona** | Pode não convergir |
| **Matrizes grandes** | Inviável (n > 10.000) | Viável |
| **Matrizes esparsas*** | Ineficiente | Muito eficiente |
| **Paralelização** | Difícil | Fácil (Jacobi) |

\* Exceto erros de arredondamento  
\*\* Exceto matrizes singulares  
\*\*\* Matriz esparsa: maioria dos elementos são zero

---

## 🎯 QUANDO USAR CADA MÉTODO?

### Use **MÉTODOS DIRETOS** quando:

✅ **Sistema pequeno a médio** (n < 1.000)
- Exemplo: 10 equações, 10 incógnitas

✅ **Precisa de solução exata**
- Exemplo: Cálculos financeiros precisos

✅ **Resolver uma única vez**
- Não vai mudar os coeficientes

✅ **Matriz densa** (muitos elementos não-zero)
- Exemplo: Sistema sem padrão especial

✅ **Não sabe se converge**
- Matriz não tem propriedades especiais

**Escolha entre Gauss, LU ou Gauss-Jordan:**
- **Gauss**: Resolver sistema uma vez (mais rápido)
- **LU**: Resolver múltiplas vezes com mesma matriz A
- **Gauss-Jordan**: Calcular inversa ou fins didáticos

---

### Use **MÉTODOS ITERATIVOS** quando:

✅ **Sistema muito grande** (n > 10.000)
- Exemplo: Simulação de física, elementos finitos

✅ **Matriz esparsa** (maioria zeros)
- Exemplo: Redes, grafos, equações diferenciais

✅ **Memória limitada**
- Não cabe matriz completa na RAM

✅ **Matriz diagonalmente dominante**
- Garante convergência

✅ **Solução aproximada é suficiente**
- Pode parar quando erro < tolerância

✅ **Tem bom chute inicial**
- Converge mais rápido

✅ **Computação paralela disponível**
- Use Jacobi para paralelizar

**Escolha entre Jacobi e Gauss-Seidel:**
- **Jacobi**: Tem computação paralela (GPU, cluster)
- **Gauss-Seidel**: Computação sequencial (mais rápido)

---

## 💡 EXEMPLOS PRÁTICOS

### Exemplo 1: Circuito Elétrico (pequeno)
```
3 equações, 3 incógnitas
→ Use Eliminação de Gauss (rápido e simples)
```

### Exemplo 2: Análise Estrutural (médio)
```
50 equações, mesma estrutura, múltiplos carregamentos
→ Use Decomposição LU (resolve múltiplas vezes)
```

### Exemplo 3: Simulação CFD (grande)
```
100.000 equações, 99% zeros, matriz esparsa
→ Use Gauss-Seidel (eficiente para esparsa)
```

### Exemplo 4: Machine Learning (enorme)
```
1.000.000 equações, cluster de computadores
→ Use Jacobi (paralelizável em GPU/cluster)
```

---

## 🔍 CRITÉRIOS DE CONVERGÊNCIA

### Para Métodos Iterativos:

**1. Erro Absoluto:**
```
|x[k+1] - x[k]| < ε
```
Para quando mudança é pequena

**2. Erro Relativo:**
```
|x[k+1] - x[k]| / |x[k+1]| < ε
```
Considera magnitude da solução

**3. Resíduo:**
```
|Ax[k] - b| < ε
```
Verifica quanto a solução satisfaz o sistema

**4. Número Máximo de Iterações:**
```
k < k_max
```
Evita loop infinito se não convergir

**Recomendação:**
Combine múltiplos critérios! Exemplo:
```python
while k < 100 and erro_relativo > 1e-6:
    # iterar
```

---

## 📈 COMPLEXIDADE COMPUTACIONAL

### Métodos Diretos:
```
Eliminação de Gauss:  O(n³/3)     ≈ 0.33n³ operações
Decomposição LU:      O(n³/3)     ≈ 0.33n³ operações
Gauss-Jordan:         O(n³/2)     ≈ 0.50n³ operações
```

### Métodos Iterativos (por iteração):
```
Jacobi:               O(n²)       ≈ n² operações
Gauss-Seidel:         O(n²)       ≈ n² operações
```

**Exemplo Numérico (n=1000):**
- Gauss: ~333 milhões de operações
- Jacobi: ~1 milhão por iteração
  - Se convergir em 50 iterações: 50 milhões (6× mais rápido!)

---

## 🎓 RESUMO EXECUTIVO

### Métodos Diretos:
> "Faça cálculos suficientes e chegará à resposta exata"

**Essência:** Transformação sistemática até solução
**Trade-off:** Precisão × Custo computacional para sistemas grandes

### Métodos Iterativos:
> "Melhore o chute até estar bom o suficiente"

**Essência:** Refinamento progressivo da aproximação
**Trade-off:** Velocidade/memória × Necessita convergência

---

## 📚 REFERÊNCIAS E LEITURA ADICIONAL

Para aprofundar seus conhecimentos:

1. **Burden & Faires** - "Numerical Analysis"
   - Capítulos 6 (Diretos) e 7 (Iterativos)

2. **Quarteroni et al.** - "Numerical Mathematics"
   - Análise de convergência detalhada

3. **Golub & Van Loan** - "Matrix Computations"
   - Aspectos computacionais avançados

4. **Online:**
   - Wikipedia: "Gaussian Elimination", "Iterative Methods"
   - NumPy/SciPy Documentation

---

**Criado para:** Trabalho de Cálculo Numérico  
**Data:** Novembro 2025  
**Versão:** 1.0
