#!/bin/bash
# Script para iniciar o servidor Flask com o ambiente virtual

cd "$(dirname "$0")"

echo "======================================"
echo "  Iniciando Servidor Flask"
echo "======================================"

# Ativar ambiente virtual
if [ ! -d ".venv" ]; then
    echo "⚠️  Ambiente virtual não encontrado. Criando..."
    python3 -m venv .venv
    source .venv/bin/activate
    echo "📦 Instalando dependências..."
    pip install flask flask-cors numpy matplotlib
else
    source .venv/bin/activate
fi

echo ""
echo "✓ Ambiente virtual ativado"
echo "✓ Iniciando servidor na porta 5000..."
echo ""

# Iniciar servidor
cd interface_web
python3 servidor_web.py
