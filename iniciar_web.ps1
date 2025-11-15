# Script PowerShell para iniciar a interface web

Write-Host ""
Write-Host "========================================================"
Write-Host "   Cálculo Numérico - Interface Web Moderna"
Write-Host "========================================================"
Write-Host ""

# Ativar o ambiente virtual
Write-Host "Ativando ambiente virtual..."
& ".\.venv\Scripts\Activate.ps1"

# Instalar dependências
Write-Host "Verificando dependências..."
python -m pip install flask flask-cors numpy matplotlib -q

# Iniciar o servidor
Write-Host ""
Write-Host "========================================================"
Write-Host "   Servidor iniciando..."
Write-Host "========================================================"
Write-Host ""
Write-Host "   Acesse http://localhost:5000 no navegador"
Write-Host "   Pressione Ctrl+C para parar o servidor"
Write-Host ""
Write-Host "========================================================"
Write-Host ""

Set-Location interface_web
python servidor_web.py
