import gradio as gr
from juegos.hanoi import lanzar_hanoi
from juegos.caballo import lanzar_caballo
from juegos.reinas import lanzar_reinas
from db.modelos import Session, DiscoMovimiento, CaballoMovimiento, ReinaMovimiento

# Funciones para Gradio (adaptadas para devolver texto y visualización)
def hanoi_gradio(n_discos):
    n = int(n_discos)
    torres = {'A': [i for i in range(n, 0, -1)], 'B': [], 'C': []}
    movimientos = []
    paso = [1]
    lanzar_hanoi(n, 'A', 'B', 'C', torres, movimientos, paso)  # Llamada directa a la lógica
    
    # Generar texto y visualización
    resultado = f"Movimientos ({len(movimientos)} totales):\n"
    resultado += "\n".join(f"{m[1]}. {m[0]}" for m in movimientos)
    
    # Visualización simple del estado final
    visual = "Torres finales:\n"
    for torre, discos in torres.items():
        visual += f"{torre}: {discos}\n"
    return resultado, visual

def caballo_gradio(x, y):
    x, y = int(x), int(y)
    if not (0 <= x <= 7 and 0 <= y <= 7):
        return "Posición inválida.", ""
    
    caballo = Caballo((x, y))
    tablero_visitado = {(x, y)}
    secuencia = [(x, y)]
    exito = resolver_caballo(caballo, tablero_visitado, secuencia)
    
    if exito:
        resultado = f"Recorrido desde ({x},{y}):\n"
        resultado += " -> ".join(f"{pos[0]},{pos[1]}" for pos in secuencia)
        resultado += f"\nMovimientos: {len(secuencia) - 1}"
        
        # Visualización del tablero 8x8
        tablero = [["." for _ in range(8)] for _ in range(8)]
        for i, (px, py) in enumerate(secuencia):
            tablero[7-py][px] = str(i+1)  # 7-y para que (0,0) esté abajo-izquierda
        visual = "\n".join(" ".join(row) for row in tablero)
        return resultado, visual
    return "No se encontró recorrido.", ""

def reinas_gradio(n):
    n = int(n)
    if n < 1 or (n < 4 and n != 1):
        return "N inválido.", ""
    
    tablero = [-1] * n
    if resolver_reinas(tablero, 0, n):
        resultado = f"Solución para {n}-Reinas:\n"
        resultado += str(tablero)
        
        # Visualización del tablero NxN
        visual = ""
        for fila in range(n):
            linea = ["Q" if tablero[col] == fila else "." for col in range(n)]
            visual += " ".join(linea) + "\n"
        return resultado, visual
    return "No se encontró solución.", ""

# Interfaz de Gradio
with gr.Blocks(title="Juegos de Algoritmos") as demo:
    gr.Markdown("# Juegos de Algoritmos y Estructuras de Datos")
    
    with gr.Tab("Torres de Hanói"):
        n_discos = gr.Textbox(label="Número de discos", value="3")
        btn_hanoi = gr.Button("Resolver")
        output_hanoi = gr.Textbox(label="Movimientos")
        visual_hanoi = gr.Textbox(label="Estado Final")
        btn_hanoi.click(hanoi_gradio, inputs=n_discos, outputs=[output_hanoi, visual_hanoi])
    
    with gr.Tab("Caballo"):
        x = gr.Textbox(label="X (0-7)", value="3")
        y = gr.Textbox(label="Y (0-7)", value="3")
        btn_caballo = gr.Button("Resolver")
        output_caballo = gr.Textbox(label="Recorrido")
        visual_caballo = gr.Textbox(label="Tablero")
        btn_caballo.click(caballo_gradio, inputs=[x, y], outputs=[output_caballo, visual_caballo])
    
    with gr.Tab("N-Reinas"):
        n_reinas = gr.Textbox(label="Tamaño del tablero (N)", value="4")
        btn_reinas = gr.Button("Resolver")
        output_reinas = gr.Textbox(label="Solución")
        visual_reinas = gr.Textbox(label="Tablero")
        btn_reinas.click(reinas_gradio, inputs=n_reinas, outputs=[output_reinas, visual_reinas])

demo.launch()