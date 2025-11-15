# 🧮 Cálculo Numérico - Trabalho 2

Interface web moderna para resolução de problemas de Cálculo Numérico usando Python, HTML, CSS e JavaScript.

---

## 🚀 Início Rápido

### 1️⃣ Iniciar o Servidor

```powershell
.\iniciar_web.ps1
```

ou

```cmd
iniciar_web.bat
```

### 2️⃣ Abrir a Interface

Duplo clique em **`index.html`** ou abra no navegador de sua preferência.

**Pronto!** 🎉

---

## 📦 Estrutura do Projeto

```
📦 Trabalho2-CalculoNumerico/
│
├── 🐍 Módulos Python (Core)
│   ├── metodos_diretos.py                    # Gauss, LU
│   ├── metodos_iterativos.py                 # Gauss-Seidel, Jacobi
│   ├── interpolacao_minimos_quadrados.py     # Lagrange, MMQ
│   ├── integracao_numerica.py                # Trapézio, Simpson
│   └── resolucao_problemas_lista.py          # Exemplos
│
├── 🌐 Interface Web
│   ├── index.html                            # Estrutura
│   ├── styles.css                            # Design minimalista
│   ├── script.js                             # Lógica
│   └── servidor_web.py                       # Backend Flask/API
│
├── 🖥️ Interface Desktop (Alternativa)
│   └── interface_gui.py                      # Tkinter GUI
│
├── 🚀 Scripts de Inicialização
│   ├── iniciar_web.bat / .ps1                # Interface Web
│   └── rodar_interface.bat / .ps1            # Interface Tkinter
│
└── 📖 Documentação
    ├── README.md                             # Este arquivo
    ├── README_WEB.md                         # Doc detalhada da web
    ├── GUIA_RAPIDO.md                        # Guia rápido
    ├── COMPARATIVO_INTERFACES.md             # Tkinter vs Web
    ├── INDICE.md                             # Índice completo
    └── EXPLICACAO_FUNCIONAMENTO.txt          # Explicação dos algoritmos
```

---

## 🎯 Funcionalidades

### ⚡ Métodos Diretos
- Eliminação de Gauss
- Fatoração LU

### 🔄 Métodos Iterativos
- Gauss-Seidel
- Jacobi

### 📈 Interpolação
- Interpolação de Lagrange
- Mínimos Quadrados

### ∫ Integração Numérica
- Método do Trapézio
- Método de Simpson

---

## 🎨 Interfaces Disponíveis

### 🌐 Interface Web (Recomendada)
- ✨ Design moderno e minimalista
- 💫 Animações suaves
- 📱 Responsiva (mobile, tablet, desktop)
- 🎨 Paleta de cores elegante

**Iniciar:**
```bash
.\iniciar_web.ps1
```

### 🖥️ Interface Desktop (Tkinter)
- ⚡ Rápida e simples
- 🖱️ Aplicativo nativo
- 💻 Desktop tradicional

**Iniciar:**
```bash
.\rodar_interface.ps1
```

---

## 📋 Requisitos

```bash
pip install -r requirements.txt
```

**Dependências:**
- Python 3.x
- NumPy
- Flask
- Flask-CORS
- Matplotlib (opcional)

---

## 💡 Exemplos de Uso

### Via Interface Web
1. Abra a interface
2. Escolha a aba (Diretos, Iterativos, etc)
3. Preencha os campos
4. Clique no botão do método desejado
5. Veja o resultado

### Via Código Python
```python
import numpy as np
import metodos_diretos as md

# Sistema linear
A = np.array([[4, 3, 2], [1, 3, 1], [2, 1, 3]])
b = np.array([960, 510, 610])

# Resolver
x = md.eliminacao_gauss(A, b)
print(f"Solução: {x}")
```

---

## 📚 Documentação

- **[README_WEB.md](README_WEB.md)** - Documentação completa da interface web
- **[GUIA_RAPIDO.md](GUIA_RAPIDO.md)** - Guia rápido para iniciantes
- **[COMPARATIVO_INTERFACES.md](COMPARATIVO_INTERFACES.md)** - Comparação entre interfaces
- **[INDICE.md](INDICE.md)** - Índice completo do projeto
- **[EXPLICACAO_FUNCIONAMENTO.txt](EXPLICACAO_FUNCIONAMENTO.txt)** - Como os algoritmos funcionam

---

## 🎨 Paleta de Cores (Interface Web)

```css
Fundo:       #FAFAFA  (cinza muito claro)
Superfície:  #FFFFFF  (branco puro)
Primária:    #2E2E2E  (cinza escuro)
Secundária:  #666666  (cinza médio)
Borda:       #E0E0E0  (cinza claro)
Texto:       #1A1A1A  (quase preto)
```

---

## 🔧 Troubleshooting

### Servidor não inicia
```bash
# Ativar ambiente virtual
.venv\Scripts\activate

# Instalar dependências
pip install flask flask-cors numpy

# Iniciar manualmente
python servidor_web.py
```

### Interface não abre
- Verifique se o servidor está rodando (http://localhost:5000)
- Abra `index.html` diretamente no navegador
- Verifique o console do navegador (F12)

### Erros de cálculo
- Verifique o formato de entrada (vírgulas entre valores)
- Matriz A deve ser quadrada
- Vetor b deve ter mesmo tamanho que A

---

## 🚀 Comandos Úteis

```bash
# Instalar dependências
pip install -r requirements.txt

# Interface Web
.\iniciar_web.ps1

# Interface Tkinter
.\rodar_interface.ps1

# Executar exemplos
python resolucao_problemas_lista.py

# Servidor manual
python servidor_web.py
```

---

## 🎓 Créditos

**Projeto:** Trabalho 2 - Cálculo Numérico  
**Tecnologias:** Python, NumPy, Flask, HTML5, CSS3, JavaScript  
**Design:** Minimalista & Moderno  

---

## 📞 Suporte

Consulte a documentação completa:
- [README_WEB.md](README_WEB.md) - Detalhes da interface web
- [GUIA_RAPIDO.md](GUIA_RAPIDO.md) - Guia passo-a-passo
- [INDICE.md](INDICE.md) - Navegação completa

---

**✨ Desenvolvido com ❤️ para Cálculo Numérico**
