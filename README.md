# estructuras-de-datos-y-Python-

https://github.com/Serdan1/estructuras-de-datos-y-Python-.git


# Proyecto de Algoritmos y Estructuras de Datos

Este proyecto implementa tres juegos clásicos de algoritmos y estructuras de datos: **Torres de Hanói**, **Recorrido del Caballo** (Knight's Tour) y **N-Reinas**. Los juegos están desarrollados en Python y cumplen con los siguientes requisitos:
- Funcionan por terminal con un menú interactivo.
- Almacenan los movimientos/soluciones en una base de datos SQLite usando SQLAlchemy.
- Incluyen una interfaz gráfica opcional con Gradio para visualización.
- Precalculan los movimientos/soluciones y los leen desde la base de datos, en lugar de calcularlos en cada ejecución.

## Ecuaciones Matemáticas

### 1. Torres de Hanói
El número de movimientos necesarios para resolver el problema con \( n \) discos es:
\[
2^n - 1
\]
Por ejemplo:
- Para \( n = 3 \), se necesitan \( 2^3 - 1 = 7 \) movimientos.
- Para \( n = 5 \), se necesitan \( 2^5 - 1 = 31 \) movimientos.
- Para \( n = 10 \), se necesitan \( 2^{10} - 1 = 1023 \) movimientos.
Los movimientos para \( n \) de 1 a 10 están precalculados y almacenados en la base de datos.

### 2. Recorrido del Caballo (Knight's Tour)
En un tablero 8x8 (64 casillas), el caballo debe visitar cada casilla exactamente una vez. El número de movimientos es:
\[
63
\]
Esto se debe a que, partiendo de una casilla inicial, se necesitan 63 saltos para visitar las 64 casillas. El programa precalcula recorridos solo para las posiciones (3,3) y (4,4).

### 3. N-Reinas
El número de soluciones únicas para el problema de las N-Reinas depende de \( N \). Algunas soluciones precalculadas son:
- \( N = 1 \): 1 solución.
- \( N = 4 \): 2 soluciones (ej. [1, 3, 0, 2]).
- \( N = 8 \): 92 soluciones.
Las soluciones para \( N \) de 1 a 8 están precalculadas y almacenadas en la base de datos.

## Algoritmos (Pseudocódigo)

### 1. Torres de Hanói
Los movimientos se precalculan usando un algoritmo recursivo y se almacenan en la base de datos.

**Pseudocódigo (Precomputo)**:
Procedimiento precompute_hanoi():
    Para n desde 1 hasta 10:
        Si movimientos para n ya están en la base de datos entonces:
            Continuar
        FinSi
        torres ← Inicializar con discos en A
        movimientos ← Lista vacía
        paso ← 1
        id_ejecucion ← Generar ID único
        resolver_hanoi(n, 'A', 'B', 'C', torres, movimientos, paso)
        Guardar movimientos en base de datos con id_ejecucion
FinProcedimiento
Procedimiento resolver_hanoi(n, origen, auxiliar, destino, torres, movimientos, paso):
    Si n = 1 entonces:
        Mover disco de origen a destino
        Registrar movimiento
        Incrementar paso
        Retornar
    FinSi

resolver_hanoi(n-1, origen, destino, auxiliar, torres, movimientos, paso)
Mover disco n de origen a destino
Registrar movimiento
Incrementar paso
resolver_hanoi(n-1, auxiliar, origen, destino, torres, movimientos, paso)

FinProcedimiento


**Pseudocódigo (Ejecución)**:

Procedimiento lanzar_hanoi(n):
    Si n no está entre 1 y 10 entonces:
        Mostrar mensaje de error
        Retornar
    FinSi

movimientos ← Leer movimientos de la base de datos para n
Si no hay movimientos entonces:
    Mostrar mensaje de error
    Retornar
FinSi

torres ← Inicializar con discos en A
Para cada movimiento en movimientos:
    Parsear movimiento (tamano, origen, destino)
    disco ← Buscar disco con tamano en torres[origen]
    torres[origen] ← Remover disco
    disco.posicion ← destino
    torres[destino] ← Añadir disco
FinPara

Mostrar movimientos y estado final de torres

FinProcedimiento


### 2. Recorrido del Caballo (Knight's Tour)
Los recorridos para las posiciones (3,3) y (4,4) se precalculan usando backtracking con la heurística de Warnsdorff.

**Pseudocódigo (Precomputo)**:
Función grado_salida(pos, visitado):
    Retornar número de movimientos válidos desde pos que no están en visitado
FinFunción
Procedimiento resolver_caballo(caballo, visitado, secuencia):
    Si longitud(secuencia) = 64 entonces:
        Retornar Verdadero
    FinSi

destinos ← posibles movimientos del caballo desde posición actual
Ordenar destinos por grado_salida (menor primero)

Para cada destino en destinos:
    Si destino no está en visitado entonces:
        Añadir destino a visitado
        Añadir destino a secuencia
        Mover caballo a destino
        Si resolver_caballo(caballo, visitado, secuencia) entonces:
            Retornar Verdadero
        FinSi
        Quitar destino de visitado
        Quitar destino de secuencia
        Retroceder posición del caballo
    FinSi
FinPara
Retornar Falso

FinProcedimiento

Procedimiento precompute_caballo():
    posiciones ← [(3,3), (4,4)]
    Para cada (x,y) en posiciones:
        Si recorrido para (x,y) ya está en la base de datos entonces:
            Continuar
        FinSi
        caballo ← Crear caballo en (x,y)
        visitado ← Conjunto con (x,y)
        secuencia ← Lista con (x,y)
        id_ejecucion ← Generar ID único
        Si resolver_caballo(caballo, visitado, secuencia) entonces:
            Guardar secuencia en base de datos con id_ejecucion
        FinSi
FinProcedimiento


**Pseudocódigo (Ejecución)**:

### 3. N-Reinas
Las soluciones para \( N \) de 1 a 8 se precalculan usando backtracking y se almacenan en la base de datos.

**Pseudocódigo (Precomputo)**:
Función es_seguro(tablero, fila, col, n):
    Para j desde 0 hasta col-1:
        Si tablero[j] = fila entonces:
            Retornar Falso
        FinSi
    FinPara

Para i, j desde (col-1, fila-1) hasta (0, 0):
    Si tablero[i] = j entonces:
        Retornar Falso
    FinSi
FinPara

Para i, j desde (col-1, fila+1) hasta (0, n-1):
    Si tablero[i] = j entonces:
        Retornar Falso
    FinSi
FinPara

Retornar Verdadero
FinFunción
Procedimiento resolver_reinas(tablero, col, n, soluciones):
    Si col ≥ n entonces:
        Añadir copia de tablero a soluciones
        Retornar
    FinSi

Para fila desde 0 hasta n-1:
    Si es_seguro(tablero, fila, col, n) entonces:
        tablero[col] ← fila
        resolver_reinas(tablero, col+1, n, soluciones)
        tablero[col] ← -1
    FinSi
FinPara
FinProcedimiento
Procedimiento precompute_reinas():
    Para n desde 1 hasta 8:
        Si soluciones para n ya están en la base de datos entonces:
            Continuar
        FinSi
        tablero ← Lista de tamaño n con -1
        soluciones ← Lista vacía
        resolver_reinas(tablero, 0, n, soluciones)
        id_ejecucion ← Generar ID único
        Para cada solucion en soluciones:
            Guardar solucion en base de datos con id_ejecucion
        FinPara
FinProcedimiento


**Pseudocódigo (Ejecución)**:
Procedimiento lanzar_reinas():
    n ← Ingresar N (1-8)
    Si n no está entre 1 y 8 entonces:
        Mostrar mensaje de error
        Retornar
    FinSi

soluciones ← Leer soluciones de la base de datos para n
Si no hay soluciones entonces:
    Mostrar mensaje de error
    Retornar
FinSi

solucion ← Tomar primera solución
Mostrar solución y tablero

FinProcedimiento


## Clases y Herencia

### Clases en `nodo/`
- **`nodo.py` (Clase `Nodo`, Abstracta)**:
  - Atributos: `posicion`.
  - Métodos abstractos: `mover(destino)`, `validar_movimiento(destino)`.
  - Descripción: Clase base para las piezas de los juegos.

- **`disco.py` (Clase `Disco`, Hereda de `Nodo`)**:
  - Atributos: `tamano`, `posicion`.
  - Métodos: `mover(destino, torres)`, `validar_movimiento(destino, torres)`.
  - Descripción: Representa un disco en las Torres de Hanói.

- **`caballo.py` (Clase `Caballo`, Hereda de `Nodo`)**:
  - Atributos: `posicion`.
  - Métodos: `mover(destino)`, `validar_movimiento(destino)`, `posibles_movimientos()`.
  - Descripción: Representa el caballo en el Knight's Tour.

- **`reina.py` (Clase `Reina`, Hereda de `Nodo`)**:
  - Atributos: `posicion`.
  - Métodos: `mover(destino)`, `validar_movimiento(destino)`.
  - Descripción: Representa una reina en N-Reinas.

### Clases en `db/`
- **`disco_movimiento.py` (Clase `DiscoMovimiento`, Hereda de `Base`)**:
  - Atributos: `id`, `id_ejecucion`, `n_discos`, `movimiento`, `paso`, `fecha`.
  - Descripción: Modelo para almacenar movimientos de Hanói.

- **`caballo_movimiento.py` (Clase `CaballoMovimiento`, Hereda de `Base`)**:
  - Atributos: `id`, `id_ejecucion`, `posicion_inicial`, `secuencia`, `pasos`, `fecha`.
  - Descripción: Modelo para almacenar recorridos del caballo.

- **`reina_movimiento.py` (Clase `ReinaMovimiento`, Hereda de `Base`)**:
  - Atributos: `id`, `id_ejecucion`, `n`, `solucion`, `fecha`.
  - Descripción: Modelo para almacenar soluciones de N-Reinas.

### Herencia
- **En `nodo/`**:
  - `Nodo` es la clase padre (abstracta).
  - `Disco`, `Caballo` y `Reina` heredan de `Nodo` y sobrescriben los métodos abstractos.
- **En `db/`**:
  - `Base` (de SQLAlchemy) es la clase padre.
  - `DiscoMovimiento`, `CaballoMovimiento` y `ReinaMovimiento` heredan de `Base`.

## Diagrama de Clases

El siguiente diagrama muestra las clases del proyecto y sus relaciones de herencia:

```mermaid
classDiagram
    class Nodo {
        +posicion
        +mover(destino)*()
        +validar_movimiento(destino)*()
    }
    class Disco {
        +tamano
        +posicion
        +mover(destino, torres)
        +validar_movimiento(destino, torres)
    }
    class Caballo {
        +posicion
        +mover(destino)
        +validar_movimiento(destino)
        +posibles_movimientos()
    }
    class Reina {
        +posicion
        +mover(destino)
        +validar_movimiento(destino)
    }
    class Base {
        <<SQLAlchemy Base>>
    }
    class DiscoMovimiento {
        +id
        +id_ejecucion
        +n_discos
        +movimiento
        +paso
        +fecha
    }
    class CaballoMovimiento {
        +id
        +id_ejecucion
        +posicion_inicial
        +secuencia
        +pasos
        +fecha
    }
    class ReinaMovimiento {
        +id
        +id_ejecucion
        +n
        +solucion
        +fecha
    }

    Nodo <|-- Disco
    Nodo <|-- Caballo
    Nodo <|-- Reina
    Base <|-- DiscoMovimiento
    Base <|-- CaballoMovimiento
    Base <|-- ReinaMovimiento
