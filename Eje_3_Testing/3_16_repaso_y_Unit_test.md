## Repaso

- **Python**: interpretado, tipado dinámico - tipado fuerte

* Python es un lenguaje interpretado, lo que significa que su código se ejecuta línea por línea mediante un intérprete (como CPython), sin necesidad de compilarlo previamente a código máquina. 

* Tipado dinámico
  
```python

x = 5       # x es int
x = "hola"  # ahora x es str
```

* Fortaleza del tipado
```python

x = "5"
y = 2
print(x + y)  # ❌ Error: no se puede sumar str + int

```

- **Tipos de errores**: sintaxis, runtime, lógicos.
```python

""" sintaxis: Ocurre cuando el código no respeta las reglas del lenguaje. 
Python no puede ni siquiera empezar a ejecutarlo.
 """
print("Hola mundo"  # Falta el paréntesis de cierre

""" ejecución: El código es sintácticamente correcto, pero falla al ejecutarse por alguna condición inesperada (división por cero, acceso a índice inexistente, etc.).
 """

x = [1, 2, 3]
print(x[5])  # Índice fuera de rango

#IndexError
""" Error Lógico
El código corre sin errores, pero no hace lo que debería. Es el más difícil de detectar porque no lanza excepciones
 """
def promedio(a, b):
    return a + b / 2  # ❌ Error lógico: falta paréntesis

print(promedio(4, 6))  # Esperado: 5, pero da 7
```

- **Depuración**: uso de `pdb`, breakpoints en VS Code.
- **Manejo de errores**: `try/except`, `finally`.
- **Verificación**: uso de `assert`.

---

## Tipos de pruebas (introducción sencilla)

| Tipo de prueba | ¿Qué verifica? | Ejemplo |
|----------------|----------------|---------|
| **Prueba manual** | Hecha por humanos | Probar botones, entradas, etc. |
| **Prueba unitaria** | Una función o bloque específico | ¿La función `suma(2, 3)` devuelve `5`? |
| **Prueba automatizada** | Hecha por código | Usar `assert` o librerías como `unittest` |
| **Prueba de integración** | Módulos que trabajan juntos | ¿La función `login()` usa correctamente `verificar_usuario()`? |
| **Prueba funcional** | Comportamiento completo | ¿El programa permite registrar usuarios correctamente? |

---

## ¿Qué es un test unitario?

> Un **test unitario** es una prueba que verifica que una función específica hace lo que debe hacer, usando entradas conocidas y comparando con salidas esperadas.

---

## Ejemplo simple: función `es_par`

```python
def es_par(n):
    return n % 2 == 0
```

### Test unitario básico con `assert`

```python
# Pruebas manuales
assert es_par(2) == True
assert es_par(3) == False
assert es_par(0) == True
```

---

## Práctica guiada

### Actividad: Crear y testear una función `mayor(a, b)` 


1. **Función a testear**: Debe comparar dos números y devolver el mayor

```python
def mayor(a, b):
    if a > b:
        return a
    else:
        return b
```

2. **Pruebas unitarias con `assert`**:

```python
# Casos normales
assert mayor(5, 3) == 5
assert mayor(2, 8) == 8

# Casos borde
assert mayor(0, 0) == 0
assert mayor(-1, -5) == -1
```

3. **Errores esperados** (opcional):

```python
# assert mayor("a", 5)  # Esto debería fallar
```



## Material complementario

1. [Python | repaso - Assert](https://www.youtube.com/watch?v=tmRmW31Y2Mw)  

2. [Unit Test](https://www.freerangetesters.com/view/courses/unit-testing-con-python/2109320-introduccion/6652068-unit-testing-y-su-importancia)
   

  
   
   
---
