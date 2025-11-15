@echo off
REM Script para executar a interface gráfica com o Python correto

echo.
echo ======================================================
echo    Cálculo Numérico - Interface Gráfica
echo ======================================================
echo.

REM Ativar o ambiente virtual
call .venv\Scripts\activate.bat

REM Instalar dependências (se necessário)
echo Instalando dependências...
pip install numpy matplotlib -q

REM Executar a interface
echo.
echo Iniciando interface...
echo.

python interface_gui.py

pause
