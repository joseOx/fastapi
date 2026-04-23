# FastAPI Task Manager

Una API RESTful para la gestión de tareas construida con [FastAPI](https://fastapi.tiangolo.com/).

## 🚀 Funcionalidades

- **Operaciones CRUD Completas**: Crear, leer, actualizar y eliminar tareas.
- **Base de Datos SQLite**: Integración con SQLAlchemy ORM para el almacenamiento persistente de datos.
- **Validación de Datos**: Uso de Pydantic (schemas) para garantizar la consistencia y correcta validación de los datos.
- **Estructura Modular**: Código organizado utilizando Routers (`app/routers/`) separando la lógica de base de datos (`crud.py`), los modelos (`models.py`) y los esquemas (`schemas.py`).
- **Pruebas (Testing)**: Configuración lista con `pytest` para realizar pruebas unitarias y de integración.
- **Documentación Interactiva Automática**: Swagger UI y ReDoc generados automáticamente por FastAPI.

## 🛠️ Tecnologías Utilizadas

- **Python 3**
- **FastAPI**
- **SQLAlchemy** (ORM)
- **SQLite** (Base de Datos)
- **Pydantic** (Validación de datos)
- **Uvicorn** (Servidor ASGI)
- **Pytest** (Testing)

## 📦 Estructura del Proyecto

```text
task-manager/
├── app/
│   ├── main.py          # Punto de entrada de la aplicación FastAPI
│   ├── database.py      # Configuración de la conexión a la base de datos
│   ├── models.py        # Modelos de base de datos (SQLAlchemy)
│   ├── schemas.py       # Modelos de validación (Pydantic)
│   ├── crud.py          # Lógica de operaciones CRUD
│   └── routers/         # Controladores y rutas de la API (ej. tasks.py)
├── tests/               # Carpeta para las pruebas con pytest
├── pytest.ini           # Configuración de pytest
├── sql_app.db           # Archivo de base de datos SQLite (generado automáticamente)
├── README.md            # Documentación del proyecto
└── requirements.txt     # Dependencias del proyecto
```

## ⚙️ Instalación y Ejecución

1. **Crear y activar un entorno virtual (recomendado):**
   ```bash
   python -m venv venv
   # En Windows:
   venv\Scripts\activate
   # En Linux/Mac:
   source venv/bin/activate
   ```

2. **Instalar las dependencias necesarias:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar el servidor de desarrollo:**
   ```bash
   uvicorn app.main:app --reload
   ```

4. **Acceder a la API y Documentación:**
   - URL Base: `http://127.0.0.1:8000/`
   - Documentación Interactiva (Swagger UI): `http://127.0.0.1:8000/docs`
   - Documentación Alternativa (ReDoc): `http://127.0.0.1:8000/redoc`
