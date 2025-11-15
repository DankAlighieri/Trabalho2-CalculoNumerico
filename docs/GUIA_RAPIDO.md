# 🚀 GUIA RÁPIDO - Interface Web

## ⚡ Iniciar em 3 Passos

### 1️⃣ Iniciar o Servidor Backend
```powershell
.\iniciar_web.ps1
```
ou
```cmd
iniciar_web.bat
```

### 2️⃣ Abrir a Interface
Duplo clique no arquivo **`index.html`**

Ou abra manualmente no navegador:
- Chrome
- Firefox
- Edge
- Safari

### 3️⃣ Usar a Interface
✅ O servidor Flask está rodando em `http://localhost:5000`  
✅ A interface web está aberta no navegador  
✅ Pronto para usar!

---

## 🎯 Diferenças entre as Interfaces

| Característica | Tkinter (GUI) | Web (HTML/CSS/JS) |
|----------------|---------------|-------------------|
| **Visual** | Simples | ⭐ Moderno e elegante |
| **Animações** | Não | ⭐ Sim (suaves) |
| **Design** | Básico | ⭐ Minimalista profissional |
| **Responsivo** | Não | ⭐ Sim (mobile-friendly) |
| **Customização** | Limitada | ⭐ Total (CSS) |
| **Deploy** | Desktop | ⭐ Pode ser online |
| **Velocidade** | Rápida | Rápida |

---

## 📦 Arquivos Criados

### Interface Tkinter (Original)
- `interface_gui.py` - Interface desktop
- `rodar_interface.bat` / `.ps1` - Scripts de inicialização

### Interface Web (Nova) ⭐
- `index.html` - Estrutura HTML5
- `styles.css` - Estilos modernos CSS3
- `script.js` - Lógica JavaScript
- `servidor_web.py` - Backend Flask/API REST
- `iniciar_web.bat` / `.ps1` - Scripts de inicialização

---

## 🎨 O que mudou?

### Visual
- ✨ Design minimalista moderno
- 🎨 Paleta de cores profissional
- 💫 Animações suaves (fade-in, slide-up)
- 🔲 Cards com sombras elegantes
- 📱 Totalmente responsivo

### UX/UI
- 🖱️ Hover effects nos botões
- ⌨️ Focus states nos inputs
- ⏳ Loading overlay durante processamento
- ✅ Feedback visual de sucesso/erro
- 📊 Área de resultados com scrolling

### Tecnologia
- 🌐 HTML5 + CSS3 + JavaScript ES6+
- 🐍 Backend Flask (Python)
- 🔌 API REST para comunicação
- 📡 CORS habilitado
- 🚀 Arquitetura cliente-servidor

---

## 💻 Como Usar Cada Funcionalidade

### Métodos Diretos
1. Digite a matriz A (uma linha por linha)
2. Digite o vetor b (separado por vírgulas)
3. Clique em "Eliminação de Gauss" ou "Fatoração LU"
4. Veja o resultado aparecer com animação

### Métodos Iterativos
1. Digite a matriz e vetor
2. Ajuste tolerância e máx. iterações
3. Escolha "Gauss-Seidel" ou "Jacobi"
4. Veja quantas iterações foram necessárias

### Interpolação
1. Digite pontos X e Y conhecidos
2. Digite o ponto para avaliar
3. Escolha Lagrange ou Mínimos Quadrados
4. Veja o valor interpolado/ajustado

### Integração
1. Digite limites a e b
2. Digite número de intervalos
3. Escolha Trapézio ou Simpson
4. Veja a integral aproximada

---

## ⚙️ Configurações

### Porta do Servidor
Editando `servidor_web.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5000)  # Mude 5000 para outra porta
```

### Temas/Cores
Editando `styles.css`:
```css
:root {
    --color-primary: #2E2E2E;  /* Mude para sua cor */
    --color-bg: #FAFAFA;
    /* ... outras cores ... */
}
```

---

## 🔥 Dicas Pro

1. **F12** - Abrir DevTools para debug
2. **Ctrl+Shift+R** - Recarregar sem cache
3. **Ctrl+F5** - Hard refresh
4. Servidor roda em **localhost:5000**
5. Use **Chrome DevTools** para testar responsive

---

## 🎁 Bônus

### Ambas as interfaces funcionam!

**Use Tkinter** se preferir:
- Interface desktop tradicional
- Sem necessidade de navegador
- Rápido para testes locais

**Use Web** se preferir:
- Visual moderno e elegante
- Experiência mais fluida
- Pode compartilhar online futuramente

---

## 📞 Comandos Úteis

```bash
# Iniciar servidor web
python servidor_web.py

# Iniciar interface Tkinter
python interface_gui.py

# Testar importações
python teste_imports.py

# Instalar dependências
pip install -r requirements.txt
```

---

**✨ Agora você tem DUAS interfaces para escolher!**

🖥️ **Tkinter** = Tradicional e funcional  
🌐 **Web** = Moderna e elegante
