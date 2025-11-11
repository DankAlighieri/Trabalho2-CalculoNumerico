# Projeto de Cálculo Numérico

Aplicação completa em Python implementando diversos algoritmos de Cálculo Numérico.

## 📚 Conteúdo

Este projeto implementa os seguintes métodos:

### 1. Sistemas de Equações Lineares - Métodos Diretos
- **Eliminação de Gauss** (com pivoteamento parcial)
- **Gauss-Jordan**
- **Decomposição LU**
- **Decomposição de Cholesky** (para matrizes simétricas positivas definidas)

### 2. Sistemas de Equações Lineares - Métodos Iterativos
- **Método de Jacobi**
- **Método de Gauss-Seidel**
- **Método SOR** (Successive Over-Relaxation)
- Verificação de convergência (dominância diagonal)

### 3. Interpolação Polinomial e Mínimos Quadrados
- **Interpolação de Lagrange**
- **Interpolação de Newton** (diferenças divididas)
- **Ajuste Linear por Mínimos Quadrados**
- **Ajuste Polinomial por Mínimos Quadrados**
- Cálculo de erro quadrático médio e R²

### 4. Integração Numérica
- **Regra do Trapézio** (simples e composta)
- **Regra de Simpson 1/3**
- **Regra de Simpson 3/8**
- **Quadratura de Gauss** (2, 3 e 4 pontos)
- Cálculo de erro absoluto e relativo

## 🚀 Como Executar

### Pré-requisitos
```bash
pip install numpy matplotlib
```

### Executar a aplicação principal
```bash
python main.py
```

### Executar módulos individuais
Cada módulo pode ser executado independentemente para ver exemplos:

```bash
python metodos_diretos.py
python metodos_iterativos.py
python interpolacao_minimos_quadrados.py
python integracao_numerica.py
```

## 📁 Estrutura do Projeto

```
projeto/
│
├── main.py                              # Interface principal interativa
├── metodos_diretos.py                   # Métodos diretos para sistemas lineares
├── metodos_iterativos.py                # Métodos iterativos para sistemas lineares
├── interpolacao_minimos_quadrados.py    # Interpolação e ajuste
├── integracao_numerica.py               # Métodos de integração numérica
├── requirements.txt                     # Dependências do projeto
└── README.md                           # Este arquivo
```

## 💡 Exemplos de Uso

### Exemplo 1: Resolver Sistema Linear (Método Direto)
```python
import numpy as np
from metodos_diretos import eliminacao_gauss

A = np.array([[4, -1, 0],
              [-1, 4, -1],
              [0, -1, 3]], dtype=float)
b = np.array([15, 10, 10], dtype=float)

x = eliminacao_gauss(A, b)
print(f"Solução: {x}")
```

### Exemplo 2: Resolver Sistema Linear (Método Iterativo)
```python
import numpy as np
from metodos_iterativos import metodo_gauss_seidel

A = np.array([[10, -1, 2],
              [-1, 11, -1],
              [2, -1, 10]], dtype=float)
b = np.array([6, 25, -11], dtype=float)

x, iteracoes, erros = metodo_gauss_seidel(A, b, tol=1e-6)
print(f"Solução: {x}")
print(f"Iterações: {iteracoes}")
```

### Exemplo 3: Interpolação de Lagrange
```python
import numpy as np
from interpolacao_minimos_quadrados import interpolacao_lagrange

x_pontos = np.array([0, 1, 2, 3])
y_pontos = np.array([1, 2, 5, 11])

P = interpolacao_lagrange(x_pontos, y_pontos)
print(f"P(1.5) = {P(1.5)}")
```

### Exemplo 4: Integração Numérica
```python
import numpy as np
from integracao_numerica import regra_simpson_1_3

f = lambda x: x**2
resultado = regra_simpson_1_3(f, a=0, b=2, n=10)
print(f"Integral aproximada: {resultado}")
```

## 🔍 Características

- **Código documentado**: Todas as funções possuem docstrings explicativas
- **Tratamento de erros**: Verificação de pivôs zeros, convergência, etc.
- **Exemplos incluídos**: Cada módulo possui função de teste com exemplos práticos
- **Interface interativa**: Menu principal para fácil navegação entre métodos
- **Comparações**: Testes comparativos entre diferentes métodos

## 📊 Validação

Todos os métodos foram validados com:
- Exemplos cujas soluções exatas são conhecidas
- Cálculo de resíduos e erros
- Comparação com implementações de referência

## 👨‍💻 Autoria

Projeto desenvolvido para a disciplina de Cálculo Numérico.

## 📄 Licença

Este projeto é de código aberto e está disponível para fins educacionais.

## 🤝 Contribuições

Sugestões e melhorias são bem-vindas!

## 📝 Notas

- Todos os métodos implementados seguem algoritmos clássicos de Cálculo Numérico
- A precisão pode ser ajustada através dos parâmetros de tolerância
- Para sistemas mal-condicionados, considere usar métodos mais robustos
- A convergência de métodos iterativos depende das propriedades da matriz
