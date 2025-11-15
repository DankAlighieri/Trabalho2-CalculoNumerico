# Script PowerShell para executar a interface gráfica Tkinter

Write-Host ""
Write-Host "======================================================"
Write-Host "   Cálculo Numérico - Interface Desktop"
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

Set-Location interface_desktop
python interface_gui.py
