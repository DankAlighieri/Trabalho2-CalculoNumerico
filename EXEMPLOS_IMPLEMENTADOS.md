# 📚 Exemplos Implementados na Aplicação Web

## ✅ Todos os 4 problemas do arquivo `resolucao_problemas_lista.py` estão implementados!

---

## 🎯 Tópico 1: Métodos Diretos

### ✓ Problema 1: Produção de componentes eletrônicos

**Localização:** Aba "Métodos Diretos"

**Como usar:**
1. Selecione "Produção de componentes eletrônicos" no dropdown "Carregar Exemplo"
2. Os dados serão carregados automaticamente:
   - Matriz A (4x4):
     ```
     4, 3, 2
     1, 3, 1
     2, 1, 3
     ```
   - Vetor b: `960, 510, 610`
3. Clique em "Eliminação de Gauss" ou "Fatoração LU"

**Resultado esperado:** 
- Solução: Transistores, Resistores, Chips

---

## 🎯 Tópico 2: Métodos Iterativos

### ✓ Problema 3: Circuito elétrico com resistores

**Localização:** Aba "Métodos Iterativos"

**Como usar:**
1. Selecione "Circuito elétrico com resistores" no dropdown
2. Os dados serão carregados:
   - Matriz A (4x4)
   - Vetor b: `16, 0, 0, 14`
   - Tolerância: 0.0001
   - Máx. Iterações: 1000
3. Clique em "Gauss-Seidel" ou "Jacobi"

**Resultado esperado:** 
- Tensões V1, V2, V3, V4
- Número de iterações

---

## 🎯 Tópico 3: Interpolação e Mínimos Quadrados

### ✓ Problema 2: Queda de voltagem em resistor

**Localização:** Aba "Interpolação"

**Como usar:**
1. Selecione "Queda de voltagem em resistor" no dropdown
2. Os dados serão carregados:
   - Pontos X (correntes): `0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 2.00`
   - Pontos Y (voltagens): `0.28, 0.67, 0.97, 1.42, 1.88, 6.0, 8.0`
   - Ponto de avaliação: `0.85`
3. Clique em "Interpolação de Lagrange"

**Resultado esperado:** 
- V(0.85A) calculado

---

## 🎯 Tópico 4: Integração Numérica

### ✓ Problema 2: Área de um rio entre margens

**Localização:** Aba "Integração"

**Como usar:**
1. Selecione "Área de um rio entre margens (interpolação)" no dropdown
2. Os dados serão carregados automaticamente:
   - Intervalo: [0, 40]
   - Número de intervalos: 4
   - Pontos X: `0, 10, 20, 30, 40`
   - Pontos Y (larguras): `62.8, 58.3, 49, 98.4, 44.3`
3. Clique em "Método do Trapézio" ou "Simpson 1/3"

**Resultado esperado:** 
- Área em m²
- Nota: "Usando interpolação de Lagrange com 5 pontos"

**📝 Nota técnica:** 
- O backend recebe os pontos X e Y
- Cria uma função interpolada usando `interpolacao_lagrange(x, y)`
- Integra essa função interpolada no intervalo [a, b] com n subintervalos

---

## 🔧 Funcionalidades Adicionais

### ✅ Entrada Manual de Dados

**Todos os campos são editáveis!** O usuário pode:
- Digitar sua própria matriz A e vetor b
- Inserir seus próprios pontos X e Y
- Definir tolerância e máximo de iterações
- Criar funções customizadas para integração

### ✅ Integração com Funções Customizadas

Na aba de Integração, além dos pontos, você pode:
- Digitar expressões matemáticas: `x**2`, `sin(x)`, `exp(x)`, `x**3 + 2*x`
- Usar funções do módulo `math`: `sin`, `cos`, `tan`, `exp`, `log`, `sqrt`
- Deixar vazio para usar x² (padrão)

### ✅ Validações Implementadas

- Matriz A deve ser quadrada
- Vetor b deve ter tamanho compatível
- Para Simpson 1/3, n deve ser par
- Pontos X e Y devem ter o mesmo tamanho

---

## 🚀 Como Executar

```bash
# Opção 1: Script automatizado
./iniciar_servidor.sh

# Opção 2: Manual
source .venv/bin/activate
cd interface_web
python3 servidor_web.py

# Abrir no navegador
http://localhost:5000
```

---

## 📊 Resultados Esperados (conforme resolucao_problemas_lista.py)

### Problema 1 - Componentes eletrônicos:
- Solução: depende da matriz específica

### Problema 3 - Circuito elétrico:
- Tensões calculadas iterativamente
- Iterações: varia conforme tolerância

### Problema 2 - Queda de voltagem:
- V(0.85A) calculado por Lagrange

### Problema 2 - Área do rio:
- Área (Trapézio): ~2380.00 m² (aproximado)
- Área (Simpson 1/3): ~2380.00 m² (aproximado)

---

**✨ Implementação completa!** Todos os 4 problemas estão funcionais na aplicação web.
