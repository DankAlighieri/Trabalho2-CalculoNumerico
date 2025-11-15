# Script PowerShell para executar a interface gráfica

Write-Host ""
Write-Host "======================================================"
Write-Host "   Cálculo Numérico - Interface Gráfica"
Write-Host "======================================================"
Write-Host ""

# Ativar o ambiente virtual
Write-Host "Ativando ambiente virtual..."
& ".\.venv\Scripts\Activate.ps1"

# Instalar dependências
Write-Host "Instalando dependências..."
python -m pip install numpy matplotlib -q

# Executar a interface
Write-Host ""
Write-Host "Iniciando interface..."
Write-Host ""

python interface_gui.py
