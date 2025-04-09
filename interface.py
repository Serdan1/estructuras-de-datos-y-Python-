import gradio as gr
from juegos.hanoi import lanzar_hanoi
from juegos.caballo import lanzar_caballo, resolver_caballo
from juegos.reinas import lanzar_reinas, resolver_reinas
from nodo.caballo import Caballo
from db.setup import setup_database
from db.precompute import precompute_all
from db import Session, CaballoMovimiento, ReinaMovimiento

# Configurar la base de datos y precomputar datos
setup_database()
precompute_all()

def hanoi_gradio(n_discos):
    try:
        n = int(n_discos)
        if n < 1 or n > 10:
            return "Por favor, ingrese un número de discos entre 1 y 10.", ""
        resultado, visual = lanzar_hanoi(n, print_output=False)
        return resultado, visual
    except ValueError:
        return "Por favor, ingrese un número válido.", ""
    except Exception as e:
        return f"Error al resolver las Torres de Hanói: {str(e)}", ""

def caballo_gradio(x, y):
    try:
        x, y = int(x), int(y)
        if not (0 <= x <= 7 and 0 <= y <= 7):
            return "Posición inválida.", ""
        
        posicion_inicial = f"{x},{y}"
        session = Session()
        recorrido = session.query(CaballoMovimiento).filter_by(posicion_inicial=posicion_inicial).first()
        session.close()
        
        if not recorrido:
            return f"No hay recorrido precalculado para la posición ({x},{y}).", ""
        
        secuencia = [tuple(map(int, pos.split(','))) for pos in recorrido.secuencia.split('-')]
        
        resultado = f"Recorrido desde ({x},{y}):\n"
        resultado += " -> ".join(f"{pos[0]},{pos[1]}" for pos in secuencia)
        resultado += f"\nMovimientos: {recorrido.pasos}"
        
        tablero = [["." for _ in range(8)] for _ in range(8)]
        for i, (px, py) in enumerate(secuencia):
            tablero[7-py][px] = str(i+1)
        visual = "\n".join(" ".join(row) for row in tablero)
        return resultado, visual
    except ValueError:
        return "Por favor, ingrese números válidos.", ""
    except Exception as e:
        return f"Error al resolver el Juego del Caballo: {str(e)}", ""

def reinas_gradio(n):
    try:
        n = int(n)
        if n < 1 or n > 15:
            return "Por favor, ingrese un valor de N entre 1 y 15.", ""
        
        session = Session()
        soluciones = session.query(ReinaMovimiento).filter_by(n=n).all()
        session.close()
        
        if not soluciones:
            return f"No hay soluciones precalculadas para N={n}.", ""
        
        solucion = soluciones[0]
        tablero = list(map(int, solucion.solucion.split('-')))
        
        resultado = f"Solución para {n}-Reinas:\n"
        resultado += str(tablero)
        
        visual = ""
        for fila in range(n):
            linea = ["Q" if tablero[col] == fila else "." for col in range(n)]
            visual += " ".join(linea) + "\n"
        return resultado, visual
    except ValueError:
        return "Por favor, ingrese un número válido.", ""
    except Exception as e:
        return f"Error al resolver N-Reinas: {str(e)}", ""

with gr.Blocks(title="Juegos de Algoritmos") as demo:
    gr.Markdown("# Juegos de Algoritmos y Estructuras de Datos")
    
    with gr.Tab("Torres de Hanói"):
        n_discos = gr.Textbox(label="Número de discos (1-10)", value="3")
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
        n_reinas = gr.Textbox(label="Tamaño del tablero (N, 1-15)", value="4")
        btn_reinas = gr.Button("Resolver")
        output_reinas = gr.Textbox(label="Solución")
        visual_reinas = gr.Textbox(label="Tablero")
        btn_reinas.click(reinas_gradio, inputs=n_reinas, outputs=[output_reinas, visual_reinas])

demo.launch()