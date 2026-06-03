@echo off
echo Ejecutando tests...
py -m pytest -v > resultado_tests.log
echo Tests finalizados. Log guardado en resultado_tests.log
type resultado_tests.log
pause
