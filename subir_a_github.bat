@echo off
echo ========================================
echo   SUBIR PROYECTO A GITHUB
echo ========================================
echo.

REM Solicitar URL del repositorio
set /p REPO_URL="Ingresa la URL de tu repositorio de GitHub: "

echo.
echo Conectando con GitHub...
git remote add origin %REPO_URL%

echo.
echo Renombrando rama a main...
git branch -M main

echo.
echo Subiendo archivos a GitHub...
git push -u origin main

echo.
echo ========================================
echo   COMPLETADO!
echo ========================================
echo.
echo Tu proyecto esta en GitHub!
echo.
echo PROXIMOS PASOS:
echo 1. Ve a tu repositorio en GitHub
echo 2. Haz clic en Settings - Pages
echo 3. Selecciona branch: main
echo 4. Guarda y espera 1-2 minutos
echo 5. Tu Gantt estara en:
echo    https://TUUSUARIO.github.io/NOMBRE-REPO/gantt_proyecto.html
echo.
pause
