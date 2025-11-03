
# Proyecto TDD 

# Ejercicio:  Crea la función `es_palindrome` 

**Problema: Detectar palíndromos**

Un **palíndromo** es una palabra, número o frase que se lee igual de izquierda a derecha que de derecha a izquierda, ignorando espacios, signos de puntuación y mayúsculas.

**TAREA:** implementar (mediante la técnica de TDD) una función llamada `es_palindrome` que reciba un **número o string** y devuelva:

* `True` si el valor ingresado es un palíndromo.
* `False` si no lo es.

### Requerimientos

1. La función debe aceptar tanto **números** como **strings**.
2. Para strings, **ignorar**:

   * Espacios
   * Mayúsculas/minúsculas
   * Signos de puntuación (coma, punto, acentos, etc.)
3. Para números, evaluar su representación como string.
4. La función debe ser probada con **tests escritos antes de la implementación** (TDD).

### Ejemplos de uso

| Input                                   | Resultado esperado |
| --------------------------------------- | ------------------ |
| `'oso'`                                 | True               |
| `'reconocer'`                           | True               |
| `'hola'`                                | False              |
| `'anita lava la tina'`                  | True               |
| `121`                                   | True               |
| `123`                                   | False              |
| `12321`                                 | True               |

**Tip:** Podés usar métodos de Python como `str()`, `lower()`, y manipular cadenas para eliminar espacios o caracteres especiales antes de comprobar si es palíndromo

recordar que en Python, las cadenas (strings) y listas se pueden “rebanar” usando slicing:

`s[inicio:fin:paso]`

- inicio → posición inicial (por defecto 0)
- fin → posición final (por defecto hasta el final)
- paso → cada cuántos elementos avanzar; si es negativo, se recorre al revés

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

'''Completar con los tests pertinentes de acuerdo a los nombres de las funcinones
'''
def test_es_palindrome_palabras():
     assert es_palindrome('oso') is True
    
def test_es_palindrome_frases():
    
def test_es_palindrome_numeros():

def test_no_es_palindrome_palabras():
    
def test_no_es_palindrome_frases():
    
def test_no_es_palindrome_numeros():
        

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


___

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
