# 🌐 Interface Web Moderna - Cálculo Numérico

Interface web minimalista e elegante usando **HTML5**, **CSS3** e **JavaScript** puro, com backend em **Flask (Python)**.

---

## ✨ Características

### 🎨 Design Moderno
- **Paleta minimalista** em escala de cinza
- **Animações suaves** e transições fluidas
- **Responsivo** - funciona em desktop e mobile
- **UX intuitiva** com abas organizadas
- **Loading overlay** durante processamento

### ⚡ Tecnologias
- **Frontend:** HTML5, CSS3 (CSS Variables), JavaScript ES6+
- **Backend:** Flask (Python 3), REST API
- **Ciência:** NumPy para cálculos numéricos

---

## 🚀 Como Usar

### Opção 1: Script Automático (Recomendado)

**Windows PowerShell:**
```powershell
.\iniciar_web.ps1
```

**Windows CMD:**
```cmd
iniciar_web.bat
```

Isso irá:
1. ✅ Ativar o ambiente virtual
2. ✅ Instalar dependências automaticamente
3. ✅ Iniciar o servidor Flask na porta 5000

### Opção 2: Manual

**Passo 1:** Ativar ambiente virtual
```bash
.venv\Scripts\activate
```

**Passo 2:** Instalar dependências
```bash
pip install flask flask-cors numpy matplotlib
```

**Passo 3:** Iniciar servidor
```bash
python servidor_web.py
```

**Passo 4:** Abrir interface
- Abra o arquivo `index.html` no seu navegador
- Ou acesse: `file:///caminho/para/index.html`

---

## 📁 Arquivos da Interface Web

```
📦 Trabalho2-CalculoNumerico/
├── 🌐 index.html           # Estrutura HTML
├── 🎨 styles.css           # Estilos CSS modernos
├── ⚡ script.js            # Lógica JavaScript
├── 🐍 servidor_web.py     # Backend Flask/API
├── 🚀 iniciar_web.bat     # Script Windows CMD
└── 🚀 iniciar_web.ps1     # Script PowerShell
```

---

## 🎯 Funcionalidades

### 1️⃣ Métodos Diretos
- ⚡ **Eliminação de Gauss** - Resolve sistemas lineares
- 📐 **Fatoração LU** - Decomposição matricial

**Entrada:**
- Matriz A (n×n)
- Vetor b (n×1)

**Saída:**
- Vetor solução x
- Matrizes L e U (no caso de LU)

---

### 2️⃣ Métodos Iterativos
- 🔄 **Gauss-Seidel** - Convergência rápida
- 🔄 **Jacobi** - Paralelizável

**Parâmetros:**
- Tolerância (padrão: 0.0001)
- Máximo de iterações (padrão: 1000)

**Saída:**
- Vetor solução
- Número de iterações realizadas

---

### 3️⃣ Interpolação
- 📈 **Lagrange** - Polinômio exato
- 📉 **Mínimos Quadrados** - Regressão linear

**Entrada:**
- Pontos X e Y conhecidos
- Ponto para avaliar

**Saída:**
- Valor interpolado/ajustado
- Coeficientes da reta (mínimos quadrados)

---

### 4️⃣ Integração Numérica
- 📊 **Trapézio** - Aproximação linear
- 📊 **Simpson** - Aproximação quadrática

**Entrada:**
- Limites de integração [a, b]
- Número de intervalos (n)

**Saída:**
- Valor da integral aproximada

---

## 🎨 Paleta de Cores

```css
/* Cores Principais */
Fundo:       #FAFAFA  (cinza muito claro)
Superfície:  #FFFFFF  (branco)
Primária:    #2E2E2E  (cinza escuro)
Secundária:  #666666  (cinza médio)
Borda:       #E0E0E0  (cinza claro)
Texto:       #1A1A1A  (quase preto)
```

---

## 🔧 Estrutura da API REST

### Endpoints Disponíveis

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | `/gauss` | Eliminação de Gauss |
| POST | `/lu` | Fatoração LU |
| POST | `/gauss-seidel` | Método Gauss-Seidel |
| POST | `/jacobi` | Método Jacobi |
| POST | `/lagrange` | Interpolação Lagrange |
| POST | `/minimos-quadrados` | Mínimos Quadrados |
| POST | `/trapezio` | Integração Trapézio |
| POST | `/simpson` | Integração Simpson |
| GET | `/` | Info da API |

### Exemplo de Requisição

```javascript
// Chamar Eliminação de Gauss
fetch('http://localhost:5000/gauss', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
        A: [[4, 3, 2], [1, 3, 1], [2, 1, 3]],
        b: [960, 510, 610]
    })
})
.then(res => res.json())
.then(data => console.log(data.x));
```

---

## 💡 Vantagens da Interface Web

| Aspecto | Tkinter | Interface Web |
|---------|---------|---------------|
| **Visual** | Simples | Moderno, elegante |
| **Customização** | Limitada | Total (CSS) |
| **Animações** | Difícil | Fácil |
| **Responsivo** | Não | Sim |
| **Mobile** | Não | Sim |
| **Deploy** | Desktop only | Pode ser online |
| **Atualização** | Reinstalar | F5 no browser |

---

## 🐛 Troubleshooting

### ❌ Erro: "Fetch failed" ou "Network error"

**Solução:** Certifique-se de que o servidor Flask está rodando:
```bash
python servidor_web.py
```

### ❌ Erro: "No module named 'flask'"

**Solução:** Instale as dependências:
```bash
pip install flask flask-cors
```

### ❌ A página não carrega os estilos

**Solução:** Verifique se os arquivos estão na mesma pasta:
- `index.html`
- `styles.css`
- `script.js`

### ❌ CORS error

**Solução:** O Flask-CORS já está configurado. Se persistir, use um servidor local:
```bash
python -m http.server 8000
```
Depois acesse: `http://localhost:8000`

---

## 📸 Screenshots

### Interface Principal
- Header com título e descrição
- Abas elegantes com ícones
- Cards brancos com sombras suaves
- Campos de entrada com feedback visual
- Botões com hover effects

### Resultados
- Área de resultado com fonte monoespaçada
- Animações de fade-in
- Indicadores de sucesso/erro
- Loading overlay durante processamento

---

## 🔮 Próximas Melhorias

- [ ] Gráficos interativos com Chart.js
- [ ] Histórico de cálculos
- [ ] Export de resultados (PDF/CSV)
- [ ] Dark mode
- [ ] Salvar configurações no localStorage
- [ ] Exemplos pré-definidos
- [ ] Validação de entrada em tempo real

---

## 📚 Referências

- **Flask:** https://flask.palletsprojects.com/
- **CSS Grid/Flexbox:** https://css-tricks.com/
- **Fetch API:** https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API
- **NumPy:** https://numpy.org/doc/

---

## 🎓 Créditos

**Projeto:** Trabalho 2 - Cálculo Numérico  
**Interface:** HTML5 + CSS3 + JavaScript + Flask  
**Linguagem:** Python 3.14  
**Design:** Minimalista & Moderno

---

**🚀 Desenvolvido com ❤️ para Cálculo Numérico**
