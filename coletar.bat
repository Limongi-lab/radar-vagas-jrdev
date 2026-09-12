@echo off
chcp 65001 >nul
cd /d "%~dp0"
call venv\Scripts\activate.bat
echo ===== %date% %time% ===== >> coleta.log
python manage.py coletar_vagas >> coleta.log 2>&1
python manage.py coletar_vagas_adzuna >> coleta.log 2>&1
python manage.py gerar_snapshot >> coleta.log 2>&1