# 📁 ESTRUTURA DE PASTAS

## 📂 Organização do Projeto

```
Trabalho2-CalculoNumerico/
│
├── 📁 metodos/                          # Módulos de cálculo numérico
│   ├── metodos_diretos.py              # Gauss, LU, Gauss-Jordan
│   ├── metodos_iterativos.py           # Gauss-Seidel, Jacobi
│   ├── interpolacao_minimos_quadrados.py  # Lagrange, Mínimos Quadrados
│   └── integracao_numerica.py          # Trapézio, Simpson
│
├── 📁 interface_web/                    # Interface Web Moderna
│   ├── servidor_web.py                 # Backend Flask (API REST)
│   ├── index.html                      # Interface HTML5
│   ├── styles.css                      # Estilos CSS3 minimalistas
│   └── script.js                       # Lógica JavaScript
│
├── 📁 interface_desktop/                # Interface Desktop
│   └── interface_gui.py                # Interface Tkinter
│
├── 📁 scripts/                          # Scripts auxiliares (vazio por enquanto)
│
├── 📁 docs/                             # Documentação
│   ├── README.md                       # Documentação principal
│   ├── GUIA_RAPIDO.md                  # Guia rápido de uso
│   ├── COMPARATIVO_INTERFACES.md       # Comparação de interfaces
│   ├── INDICE.md                       # Índice da documentação
│   ├── README_WEB.md                   # Documentação da interface web
│   ├── EXPLICACAO_FUNCIONAMENTO.txt    # Como funciona
│   └── ESTRUTURA_PASTAS.md            # Este arquivo
│
├── 🐍 resolucao_problemas_lista.py     # Script de resolução de exercícios
├── 📋 requirements.txt                  # Dependências Python
│
└── 🚀 Scripts de Inicialização (Raiz do Projeto)
    ├── iniciar_web.bat                 # Inicia interface web (Windows)
    ├── iniciar_web.ps1                 # Inicia interface web (PowerShell)
    ├── rodar_interface.bat             # Inicia interface desktop (Windows)
    └── rodar_interface.ps1             # Inicia interface desktop (PowerShell)
```

## 🚀 Como Usar

### Interface Web (Recomendada)
1. Execute na raiz do projeto:
   ```
   iniciar_web.bat
   ```
   ou
   ```
   .\iniciar_web.ps1
   ```

2. Abra no navegador: `interface_web\index.html`

### Interface Desktop (Alternativa)
1. Execute na raiz do projeto:
   ```
   rodar_interface.bat
   ```
   ou
   ```
   .\rodar_interface.ps1
   ```

### Script de Exercícios
Na raiz do projeto:
```powershell
.\.venv\Scripts\activate
python resolucao_problemas_lista.py
```

## 📦 Dependências

Instaladas automaticamente pelos scripts:
- Flask
- Flask-CORS
- NumPy
- Matplotlib

## 🎨 Características

### Interface Web
✅ Design minimalista e moderno  
✅ 4 abas organizadas por tópico  
✅ API REST com Flask  
✅ Responsiva e animada  

### Interface Desktop
✅ Design minimalista grayscale  
✅ 4 abas em Tkinter  
✅ Execução local  

## 📖 Documentação Completa

Veja `docs\README.md` para documentação completa dos métodos, exemplos de uso e detalhes técnicos.

## 🔧 Estrutura Técnica

- **Módulos de cálculo**: Independentes, podem ser importados separadamente
- **Interfaces**: Utilizam os módulos via importação ou API REST
- **Scripts**: Facilitam inicialização sem precisar navegar entre pastas
- **Documentação**: Centralizada na pasta `docs/`

---

**Nota**: Os erros de lint sobre imports não resolvidos são esperados - o Python resolve esses imports em tempo de execução através do `sys.path`.
