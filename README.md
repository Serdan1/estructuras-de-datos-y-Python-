# estructuras-de-datos-y-Python-

https://github.com/Serdan1/estructuras-de-datos-y-Python-.git


# Proyecto de Algoritmos y Estructuras de Datos

Este proyecto implementa tres juegos clásicos de algoritmos y estructuras de datos: **Torres de Hanói**, **Recorrido del Caballo** (Knight's Tour) y **N-Reinas**. Los juegos están desarrollados en Python y cumplen con los siguientes requisitos:
- Funcionan por terminal con un menú interactivo.
- Almacenan los movimientos/soluciones en una base de datos SQLite usando SQLAlchemy.
- Incluyen una interfaz gráfica opcional con Gradio para visualización.

## Ecuaciones Matemáticas

### 1. Torres de Hanói
El número de movimientos necesarios para resolver el problema con \( n \) discos es:
\[
2^n - 1
\]
Por ejemplo:
- Para \( n = 3 \), se necesitan \( 2^3 - 1 = 7 \) movimientos.
- Para \( n = 5 \), se necesitan \( 2^5 - 1 = 31 \) movimientos.

### 2. Recorrido del Caballo (Knight's Tour)
En un tablero 8x8 (64 casillas), el caballo debe visitar cada casilla exactamente una vez. El número de movimientos es:
\[
63
\]
Esto se debe a que, partiendo de una casilla inicial, se necesitan 63 saltos para visitar las 64 casillas.

### 3. N-Reinas
El número de soluciones únicas para el problema de las N-Reinas depende de \( N \). Algunas soluciones conocidas son:
- \( N = 1 \): 1 solución.
- \( N = 4 \): 2 soluciones (ej. [1, 3, 0, 2]).
- \( N = 8 \): 92 soluciones.
El programa encuentra al menos una solución para cada \( N \).

## Instrucciones de Uso
# Por terminal
1. Instar dependencias
pip install -r requirements.txt

2. Ejecutar el programa
python main.py

3. Sigue las instrucciones
Opción 1: Caballo (recomendado X=3, Y=3).
Opción 2: N-Reinas (recomendado N=4).
Opción 3: Torres de Hanói (recomendado N=3).

# Interfaz Gráfica 
1. Asegúrate de tener Gradio instalado (incluido en requirements.txt)
2. Ejecute la interfaz
python interface.py
3. Abrir el navegador
4. 4. Usa las pestañas para interacturar con cada juego
  
## Dependencias 
El proyecto requiere las siguientes bibliotecas:
sqlalchemy: Para la base de datos.
gradio: Para la interfaz gráfica.
Instaladas con:
pip install -r requirements.txt


## Diagrama de Flujo

El flujo del programa sigue este esquema:

```mermaid
flowchart TD
    A[Inicio] --> B[Menú Principal]
    B -->|Opción 1| C[Juego del Caballo]
    B -->|Opción 2| D[Juego de N-Reinas]
    B -->|Opción 3| E[Juego de Torres de Hanói]
    B -->|Opción 0| F[Salir]
    
    C --> G[Ingresar X, Y]
    G --> H[Resolver Recorrido]
    H --> I[Almacenar en DB]
    I --> J[Mostrar Resultado]
    J --> B
    
    D --> K[Ingresar N]
    K --> L[Resolver N-Reinas]
    L --> M[Almacenar en DB]
    M --> N[Mostrar Resultado]
    N --> B
    
    E --> O[Ingresar N Discos]
    O --> P[Resolver Hanói]
    P --> Q[Almacenar en DB]
    Q --> R[Mostrar Resultado]
    R --> B
    
    F --> S[Fin]
