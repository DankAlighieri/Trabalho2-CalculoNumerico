# GUIA DE INSTALAÇÃO E USO

## 📋 Requisitos do Sistema

- Python 3.7 ou superior
- pip (gerenciador de pacotes do Python)

## 🔧 Instalação

### Passo 1: Verificar instalação do Python

Abra o terminal (PowerShell no Windows) e execute:

```bash
python --version
```

Se o Python não estiver instalado, baixe em: https://www.python.org/downloads/

### Passo 2: Instalar dependências

No diretório do projeto, execute:

```bash
pip install -r requirements.txt
```

Ou instale manualmente:

```bash
pip install numpy matplotlib
```

## 🚀 Como Executar

### Opção 1: Interface Interativa (RECOMENDADO)

Execute o programa principal com menu interativo:

```bash
python main.py
```

O menu permite:
- Escolher categoria de métodos
- Executar métodos específicos
- Usar sistemas de exemplo
- Criar sistemas personalizados
- Ver demonstrações completas

### Opção 2: Executar Exemplos Prontos

Execute o arquivo de exemplos práticos:

```bash
python exemplos.py
```

Este arquivo mostra 10 exemplos práticos de aplicação dos métodos.

### Opção 3: Executar Módulos Individuais

Cada módulo pode ser executado separadamente para ver sua demonstração:

```bash
# Métodos Diretos
python metodos_diretos.py

# Métodos Iterativos
python metodos_iterativos.py

# Interpolação e Mínimos Quadrados
python interpolacao_minimos_quadrados.py

# Integração Numérica
python integracao_numerica.py
```

### Opção 4: Importar em Seu Código

Você pode importar os módulos em seus próprios scripts:

```python
import numpy as np
from metodos_diretos import eliminacao_gauss

# Seu código aqui
A = np.array([[4, -1], [-1, 4]], dtype=float)
b = np.array([3, 5], dtype=float)
x = eliminacao_gauss(A, b)
print(f"Solução: {x}")
```

## 📚 Estrutura do Projeto

```
projeto/
│
├── main.py                              # ⭐ Interface principal (EXECUTE ESTE)
├── exemplos.py                          # Exemplos práticos
├── metodos_diretos.py                   # Eliminação de Gauss, LU, Cholesky
├── metodos_iterativos.py                # Jacobi, Gauss-Seidel, SOR
├── interpolacao_minimos_quadrados.py    # Lagrange, Newton, Ajuste
├── integracao_numerica.py               # Trapézio, Simpson, Gauss
├── requirements.txt                     # Dependências
├── README.md                           # Documentação completa
└── GUIA_INSTALACAO.md                  # Este arquivo
```

## 🎯 Exemplos Rápidos

### Resolver Sistema Linear

```python
import numpy as np
from metodos_diretos import eliminacao_gauss

A = np.array([[10, -1, 2],
              [-1, 11, -1],
              [2, -1, 10]], dtype=float)
b = np.array([6, 25, -11], dtype=float)

solucao = eliminacao_gauss(A, b)
print(solucao)
```

### Interpolação

```python
import numpy as np
from interpolacao_minimos_quadrados import interpolacao_lagrange

x = np.array([0, 1, 2, 3])
y = np.array([1, 2, 5, 11])

P = interpolacao_lagrange(x, y)
print(f"P(1.5) = {P(1.5)}")
```

### Integração

```python
from integracao_numerica import regra_simpson_1_3

f = lambda x: x**2
resultado = regra_simpson_1_3(f, a=0, b=2, n=10)
print(f"Integral = {resultado}")
```

## ⚠️ Solução de Problemas

### Erro: "ModuleNotFoundError: No module named 'numpy'"

**Solução:** Instale as dependências:
```bash
pip install numpy matplotlib
```

### Erro: "pip: command not found"

**Solução:** Use:
```bash
python -m pip install numpy matplotlib
```

### Erro: Permissão negada no Windows

**Solução:** Execute o terminal como Administrador ou use:
```bash
pip install --user numpy matplotlib
```

### Código não limpa a tela

**Solução:** Isso é normal em alguns terminais. A funcionalidade não afeta os cálculos.

## 💻 Comandos Úteis

### Verificar versões instaladas
```bash
pip show numpy matplotlib
```

### Atualizar dependências
```bash
pip install --upgrade numpy matplotlib
```

### Executar teste rápido
```bash
python -c "import numpy; print('NumPy instalado:', numpy.__version__)"
```

## 📊 Menu Principal

Ao executar `python main.py`, você verá:

```
==================================================================
               CÁLCULO NUMÉRICO - APLICAÇÃO COMPLETA
==================================================================

1. SISTEMAS DE EQUAÇÕES LINEARES - MÉTODOS DIRETOS
2. SISTEMAS DE EQUAÇÕES LINEARES - MÉTODOS ITERATIVOS
3. INTERPOLAÇÃO POLINOMIAL E MÍNIMOS QUADRADOS
4. INTEGRAÇÃO NUMÉRICA
5. EXECUTAR TODOS OS TESTES
0. SAIR
```

### Navegação:
- Digite o número da opção desejada
- Pressione Enter
- Siga as instruções na tela
- Digite `0` para voltar ou sair

## 🎓 Recomendações de Estudo

1. **Primeiro:** Execute `python exemplos.py` para ver casos práticos
2. **Segundo:** Execute `python main.py` e explore o menu interativo
3. **Terceiro:** Execute cada módulo individual para ver detalhes
4. **Quarto:** Experimente com seus próprios dados

## 📖 Documentação Adicional

- Cada função possui docstrings explicativas
- Os módulos incluem exemplos de teste
- README.md contém documentação completa
- Código comentado para facilitar entendimento

## 🆘 Suporte

Se encontrar problemas:

1. Verifique se o Python 3.7+ está instalado
2. Confirme que numpy e matplotlib estão instalados
3. Execute os testes individuais para isolar o problema
4. Verifique a sintaxe se modificou o código

## ✅ Checklist de Instalação

- [ ] Python 3.7+ instalado
- [ ] pip funcionando
- [ ] numpy instalado (`pip install numpy`)
- [ ] matplotlib instalado (`pip install matplotlib`)
- [ ] Teste executado com sucesso (`python exemplos.py`)
- [ ] Menu principal funcionando (`python main.py`)

## 🎉 Pronto para Usar!

Se todos os passos acima funcionaram, você está pronto para usar a aplicação!

Execute:
```bash
python main.py
```

Divirta-se explorando os métodos de Cálculo Numérico! 🚀
