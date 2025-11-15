@echo off
REM Script para executar a interface gráfica Tkinter

echo.
echo ======================================================
echo    Cálculo Numérico - Interface Desktop
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

cd interface_desktop
python interface_gui.py

pause
