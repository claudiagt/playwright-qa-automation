# Playwright QA Automation

Proyecto de automatización de pruebas desarrollado con Python, Playwright y Pytest.

## Tecnologías

- Python
- Playwright
- Pytest
- pytest-playwright
- pytest-base-url

## Estructura del proyecto

- `pages/`: Page Objects y lógica de interacción con las páginas.
- `tests/`: casos de prueba automatizados.
- `pytest.ini`: configuración de Pytest y URL base.
- `requirements.txt`: dependencias necesarias para ejecutar el proyecto.

## Instalación

Crear el entorno virtual:

```bash
python -m venv .venv

#Activarlo en Windows PowerShell:
.\.venv\Scripts\Activate.ps1

#Instalar dependencias:
pip install -r requirements.txt

#Instalar los navegadores de Playwright:
playwright install

#Ejecución
#Ejecutar todos los tests:
pytest

#Ejecutarlos visualizando el navegador:
pytest --headed