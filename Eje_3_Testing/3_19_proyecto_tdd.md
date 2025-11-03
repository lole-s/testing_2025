
# Proyecto TDD: Función `es_palindrome`

## 1 Requerimientos de la función

* La función debe aceptar **números o strings**.
* Devuelve `True` si el input es **palíndromo**.
* Para **strings**, ignora:

  * Espacios
  * Signos de puntuación
  * Mayúsculas/minúsculas
* Devuelve `False` si no es palíndromo.

### Ejemplos esperados (en español)

| Input                                   | Resultado |
| --------------------------------------- | --------- |
| `'oso'`                                 | True      |
| `'reconocer'`                           | True      |
| `'anita lava la tina'`                  | True      |
| `'hola'`                                | False     |
| `121`                                   | True      |
| `123`                                   | False     |
| `'no es palíndromo'`                    | False     |

---

## 2 Estructura de carpetas

```
mi_proyecto_tdd/
├─ src/                  
│   ├─ __init__.py       ← vacío, marca la carpeta como paquete
│   └─ palindrome.py     ← funciones a implementar
└─ tests/                
    └─ test_palindrome.py ← tests escritos primero (TDD)
```

---

## 3 Contenido de archivos

### `src/palindrome.py`

```python
def es_palindrome(valor):
    """
    Devuelve True si el número o string es palíndromo.
    Para strings ignora mayúsculas, espacios y signos de puntuación.
    """
    pass  # se implementa después de escribir los tests
```

### `tests/test_palindrome.py`

```python
import pytest
from src.palindrome import es_palindrome

def test_es_palindrome_palabras():
     assert es_palindrome('oso') is True
    
def test_es_palindrome_frases():
    
def test_es_palindrome_numeros():

def test_no_es_palindrome_palabras():
    
def test_no_es_palindrome_frases():
    
def test_no_es_palindrome_numeros():
        

```

---


___

Aquí tienes una **introducción amigable** para presentar a los alumnos por qué usar entornos virtuales (venvs), y además un video explicativo que puedes proyectar en clase.

---

## [ENTORNO VIRTUAL EN PYTHON](https://www.youtube.com/watch?v=TNtrAvNNxTY) 

> Cuando trabajamos en proyectos de programación, a menudo instalamos librerías externas (por ejemplo, con `pip`). Si dos proyectos usan versiones diferentes de la misma librería —o del mismo intérprete de Python— pueden ocurrir **conflictos**: uno puede fallar porque instaló una versión antigua, el otro porque instaló una nueva.
>
> Un **entorno virtual** (`venv`, virtual environment) es como tener un “mini‑Python” dentro de tu proyecto, con sus propias librerías y su propio espacio aislado. Esto nos da tres grandes ventajas:
>
> 1. **Independencia de versiones**: cada proyecto puede usar la versión de librería que quiere sin molestar a otro.
> 2. **Protección del sistema**: evitamos instalar librerías globalmente que podrían romper otros programas o el propio sistema.
> 3. **Facilidad de compartir y reproducir proyectos**: si otro programador clona tu proyecto, activando el mismo venv podrá usar exactamente las mismas dependencia, y todo funcionará igual.
>
> En resumen: *un venv te ayuda a mantener tu proyecto limpio, con control de dependencias, y sin sorpresas*.


---

## Comandos Windows paso a paso para crear un entorno virtual python

1. Abrir PowerShell y crear proyecto:

```powershell
cd C:\temp2025
mkdir mi_proyecto_tdd
cd mi_proyecto_tdd
```

2. Crear y activar entorno virtual:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

3. Instalar pytest y pytest-cov:

```powershell
pip install pytest pytest-cov
```

4. Ejecutar tests (TDD: primero rojo):

```powershell
pytest -q
```

5. Implementar la función en `src/palindrome.py`.

6. Ejecutar tests nuevamente (TDD: verde):

```powershell
pytest -q
```

7. Medir cobertura (opcional):

```powershell
pytest --cov=src --cov-report=term-missing -q
```

---

##  Flujo visual TDD

```
+--------------------+
| Escribir tests     |
| (rojo)             |
+--------------------+
          |
          v
+--------------------+
| Ejecutar tests     |
| Fallan → rojo      |
+--------------------+
          |
          v
+--------------------+
| Implementar función|
|                     |
+--------------------+
          |
          v
+--------------------+
| Ejecutar tests     |
| Todos pasan → verde|
+--------------------+
          |
          v
+--------------------+
| Refactorizar       |
| Opcional           |
+--------------------+
```

---
