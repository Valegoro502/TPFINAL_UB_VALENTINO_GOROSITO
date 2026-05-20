import time

def test_rendimiento_agregar_muchas_tareas():
    g = GestorTareas()

    inicio = time.time()

    for i in range(1000):
        g.agregar_tarea(f"Tarea {i}")

    fin = time.time()

    assert (fin - inicio) < 1  # menos de 1 segundo
