@echo off
REM Script para iniciar a interface web

echo.
echo ========================================================
echo    Calculo Numerico - Interface Web Moderna
echo ========================================================
echo.

REM Ativar o ambiente virtual
call .venv\Scripts\activate.bat

REM Instalar dependencias (se necessario)
echo Verificando dependencias...
pip install flask flask-cors numpy matplotlib -q

REM Iniciar o servidor
echo.
echo ========================================================
echo    Servidor iniciando...
echo ========================================================
echo.
echo    1. O servidor Flask iniciara em http://localhost:5000
echo    2. Abra index.html no navegador
echo    3. Pressione Ctrl+C para parar o servidor
echo.
echo ========================================================
echo.

python servidor_web.py

pause
