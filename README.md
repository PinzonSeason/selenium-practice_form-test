# Selenium Form Test – Registro Automatizado

## 📌 Descripción

Este proyecto automatiza el flujo de registro en un formulario web de práctica usando **Selenium**, **pytest** y el patrón **Page Object Model (POM)**. Simula un caso de registro exitoso, encapsula la lógica de interacción con el formulario y permite escalar fácilmente hacia pruebas negativas, validaciones visuales y reportes.

---

## ⚙️ Tecnologías utilizadas

- Python 3.14.3
- Selenium
- WebDriver Manager
- Pytest
- Faker (para generación de datos)

---

## 📁 Estructura del Proyecto

Organización modular basada en buenas prácticas de automatización con Selenium y Pytest:

| Carpeta / Archivo                 | Descripción breve                                       |
|-----------------------------------|---------------------------------------------------------|
| `tests/`                          | Contiene los casos de prueba automatizados              |
| └── `test_valid_registration.py`  | Test funcional para registro exitoso                    |
| `pages/`                          | Implementa el patrón Page Object Model                  |
| └── `registration_page.py`        | Métodos encapsulados para interactuar con el formulario |
| `utils/`                          | Funciones auxiliares y configuración del navegador      |
| └── `driver_setup.py`             | Inicializa el driver con WebDriver Manager              |
| `README.md`                       | Documentación principal del proyecto                    |
| `requirements.txt`                | Lista de dependencias esenciales                        |
| `requirements-dev.txt`            | Dependencias opcionales para desarrollo/debugging       |
| `venv/`                           | Entorno virtual local (excluido del repositorio)        |

---

## 🚀 Instalación y ejecución

### 1. Clonar el repositorio
```bash
git clone git@github.com:PinzonSeason/selenium-practice_form-test.git
cd selenium-practice_form-test
```

---

## Crear y activar entorno virtual
### En powerShell:
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```
### En CMD:
```bash
- venv\Scripts\activate.bat
```
---

## Instalar dependencias
```bash
pip install -r requirements.txt
```

---

## Ejecutar pruebas
```bash
pytest -v
```

