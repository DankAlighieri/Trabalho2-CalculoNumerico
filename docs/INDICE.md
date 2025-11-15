# 📚 Índice Completo do Projeto

## 🎯 Estrutura do Projeto

```
📦 Trabalho2-CalculoNumerico/
│
├── 🐍 MÓDULOS PYTHON (Core)
│   ├── metodos_diretos.py                    - Eliminação Gauss, Fatoração LU
│   ├── metodos_iterativos.py                 - Gauss-Seidel, Jacobi
│   ├── interpolacao_minimos_quadrados.py     - Lagrange, Mínimos Quadrados
│   ├── integracao_numerica.py                - Trapézio, Simpson
│   └── resolucao_problemas_lista.py          - Exemplos da lista de exercícios
│
├── 🖥️ INTERFACE TKINTER (Desktop)
│   ├── interface_gui.py                      - Interface gráfica Tkinter
│   ├── rodar_interface.bat                   - Script Windows CMD
│   └── rodar_interface.ps1                   - Script Windows PowerShell
│
├── 🌐 INTERFACE WEB (Moderna)
│   ├── index.html                            - Estrutura HTML5
│   ├── styles.css                            - Estilos CSS3 minimalistas
│   ├── script.js                             - Lógica JavaScript
│   ├── servidor_web.py                       - Backend Flask/API REST
│   ├── iniciar_web.bat                       - Script Windows CMD
│   └── iniciar_web.ps1                       - Script Windows PowerShell
│
├── 🧪 TESTES & UTILITÁRIOS
│   └── teste_imports.py                      - Verifica imports e dependências
│
├── 📖 DOCUMENTAÇÃO
│   ├── README_GUI.md                         - Doc interface Tkinter
│   ├── README_WEB.md                         - Doc interface Web (completa)
│   ├── GUIA_RAPIDO.md                        - Guia rápido de uso
│   ├── COMPARATIVO_INTERFACES.md             - Tkinter vs Web
│   ├── RESUMO_INTERFACE_WEB.txt              - Resumo visual ASCII
│   ├── COMO_EXECUTAR.md                      - Instruções de execução
│   ├── EXPLICACAO_FUNCIONAMENTO.txt          - Explicação dos algoritmos
│   └── INDICE.md                             - Este arquivo
│
├── ⚙️ CONFIGURAÇÃO
│   └── requirements.txt                      - Dependências Python
│
└── 📁 OUTROS
    └── __pycache__/                          - Cache Python (auto-gerado)
```

---

## 🗺️ Mapa de Navegação Rápida

### 💡 Quero usar a interface...

**Desktop (Tkinter):**
1. Leia: [`README_GUI.md`](README_GUI.md)
2. Execute: `rodar_interface.ps1` ou `rodar_interface.bat`

**Web (Moderna):**
1. Leia: [`README_WEB.md`](README_WEB.md)
2. Execute: `iniciar_web.ps1` ou `iniciar_web.bat`
3. Abra: `index.html` no navegador

**Comparar ambas:**
- Leia: [`COMPARATIVO_INTERFACES.md`](COMPARATIVO_INTERFACES.md)

---

### 🔧 Quero entender o código...

**Algoritmos Numéricos:**
- [`metodos_diretos.py`](metodos_diretos.py) - Gauss, LU
- [`metodos_iterativos.py`](metodos_iterativos.py) - Gauss-Seidel, Jacobi
- [`interpolacao_minimos_quadrados.py`](interpolacao_minimos_quadrados.py) - Lagrange, MMQ
- [`integracao_numerica.py`](integracao_numerica.py) - Trapézio, Simpson

**Explicação Detalhada:**
- [`EXPLICACAO_FUNCIONAMENTO.txt`](EXPLICACAO_FUNCIONAMENTO.txt)

**Exemplos de Uso:**
- [`resolucao_problemas_lista.py`](resolucao_problemas_lista.py)

---

### 🐛 Problemas?

**Não consigo rodar:**
- Leia: [`COMO_EXECUTAR.md`](COMO_EXECUTAR.md)

**Erros de import:**
- Execute: `python teste_imports.py`
- Instale: `pip install -r requirements.txt`

**Servidor não inicia:**
- Verifique: Python 3.x instalado
- Ative venv: `.venv\Scripts\activate`
- Instale Flask: `pip install flask flask-cors`

---

## 📊 Funcionalidades por Arquivo

### 🔢 Métodos Diretos (`metodos_diretos.py`)
- ✅ Eliminação de Gauss
- ✅ Fatoração LU
- ✅ Substituição regressiva/progressiva

### 🔄 Métodos Iterativos (`metodos_iterativos.py`)
- ✅ Gauss-Seidel
- ✅ Jacobi
- ✅ Histórico de convergência

### 📈 Interpolação (`interpolacao_minimos_quadrados.py`)
- ✅ Interpolação de Lagrange
- ✅ Mínimos Quadrados (regressão linear)

### ∫ Integração (`integracao_numerica.py`)
- ✅ Método do Trapézio
- ✅ Método de Simpson
- ✅ Função customizável

---

## 🎨 Interfaces Disponíveis

### 🖥️ Tkinter (Desktop)
| Arquivo | Descrição | Uso |
|---------|-----------|-----|
| `interface_gui.py` | GUI principal | `python interface_gui.py` |
| `rodar_interface.ps1` | Launcher PS | `.\rodar_interface.ps1` |
| `rodar_interface.bat` | Launcher CMD | `rodar_interface.bat` |

**Características:**
- ⚪ Visual simples
- ⚡ Rápido de iniciar
- 🖱️ Desktop nativo

---

### 🌐 Web (Moderna)
| Arquivo | Descrição | Tecnologia |
|---------|-----------|------------|
| `index.html` | Estrutura | HTML5 |
| `styles.css` | Visual | CSS3 + Variables |
| `script.js` | Lógica | JavaScript ES6+ |
| `servidor_web.py` | Backend | Flask + REST API |
| `iniciar_web.ps1` | Launcher PS | PowerShell |
| `iniciar_web.bat` | Launcher CMD | Batch |

**Características:**
- ⭐ Visual moderno minimalista
- 💫 Animações suaves
- 📱 Totalmente responsivo
- 🌐 Deploy-ready

**Como usar:**
1. `.\iniciar_web.ps1` (inicia servidor)
2. Abrir `index.html` (interface)

---

## 📖 Documentação por Nível

### 👶 Iniciante
1. [`GUIA_RAPIDO.md`](GUIA_RAPIDO.md) ⭐ **Comece aqui!**
2. [`COMO_EXECUTAR.md`](COMO_EXECUTAR.md)
3. [`README_GUI.md`](README_GUI.md)

### 🧑‍💻 Intermediário
1. [`README_WEB.md`](README_WEB.md)
2. [`COMPARATIVO_INTERFACES.md`](COMPARATIVO_INTERFACES.md)
3. Código fonte dos módulos Python

### 🔬 Avançado
1. [`EXPLICACAO_FUNCIONAMENTO.txt`](EXPLICACAO_FUNCIONAMENTO.txt)
2. Análise do código fonte
3. Modificação dos algoritmos

---

## 🚀 Fluxo de Trabalho Recomendado

### Primeira Vez:
```bash
1. pip install -r requirements.txt
2. python teste_imports.py
3. .\rodar_interface.ps1  # Testar Tkinter
4. .\iniciar_web.ps1      # Testar Web
```

### Uso Regular:

**Para cálculos rápidos:**
```bash
.\rodar_interface.ps1
```

**Para apresentações:**
```bash
.\iniciar_web.ps1
# Abrir index.html
```

**Para programação:**
```python
import metodos_diretos as md
import numpy as np

A = np.array([[4, 3], [1, 2]])
b = np.array([10, 5])
x = md.eliminacao_gauss(A, b)
```

---

## 📦 Dependências

### Essenciais (Core)
```
numpy>=1.21.0
```

### Visualização (Opcional)
```
matplotlib>=3.4.0
```

### Interface Web
```
flask>=2.0.0
flask-cors>=3.0.0
```

**Instalar tudo:**
```bash
pip install -r requirements.txt
```

---

## 🎯 Casos de Uso

### 📚 Estudante
- Use: `resolucao_problemas_lista.py` para exemplos
- Teste: Interface Tkinter para experimentação
- Apresente: Interface Web para impressionar

### 👨‍🏫 Professor
- Demonstre: Interface Web (visual moderno)
- Explique: Código fonte dos módulos
- Distribua: `requirements.txt` + código

### 🔬 Pesquisador
- Importe: Módulos Python direto
- Modifique: Algoritmos conforme necessário
- Integre: Com seu código existente

---

## 🎨 Customização

### Mudar Cores (Web)
Edite `styles.css`:
```css
:root {
    --color-primary: #2E2E2E;  /* Sua cor aqui */
    --color-bg: #FAFAFA;
    /* ... */
}
```

### Adicionar Função (Integração)
Edite `integracao_numerica.py`:
```python
def funcao(x):
    return x**2  # Sua função aqui
```

### Adicionar Método
1. Implemente no módulo Python
2. Adicione rota em `servidor_web.py`
3. Adicione botão em `index.html`
4. Adicione handler em `script.js`

---

## 📞 Comandos Úteis

```bash
# Verificar instalação
python teste_imports.py

# Interface Tkinter
python interface_gui.py

# Interface Web (servidor)
python servidor_web.py

# Executar exemplos
python resolucao_problemas_lista.py

# Instalar dependências
pip install -r requirements.txt

# Ambiente virtual
python -m venv venv
venv\Scripts\activate
```

---

## 🏆 Destaques do Projeto

### ✨ Código Limpo
- Documentação inline
- Funções bem nomeadas
- Estrutura modular

### 🎨 Duas Interfaces Completas
- Desktop tradicional (Tkinter)
- Web moderna (HTML/CSS/JS)

### 📚 Documentação Extensa
- 10+ arquivos de documentação
- Guias passo-a-passo
- Comparativos detalhados

### 🚀 Pronto para Uso
- Scripts de inicialização
- Exemplos incluídos
- Testes automatizados

---

## 🎓 Conclusão

Este projeto oferece:

✅ **Implementações corretas** de métodos numéricos  
✅ **Duas interfaces** modernas e funcionais  
✅ **Documentação completa** para todos os níveis  
✅ **Código limpo** e bem organizado  
✅ **Pronto para uso** imediato  

**Escolha sua interface favorita e comece a calcular! 🚀**

---

**📌 Lembre-se:**
- Tkinter = Simples e rápido
- Web = Moderno e elegante
- Ambas são igualmente funcionais!

---

*Última atualização: Novembro 2025*
