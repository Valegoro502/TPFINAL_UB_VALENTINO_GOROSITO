from gestor import Tarea, GestorTareas

def test_integracion_flujo_completo():
    g = GestorTareas()
    
    g.agregar_tarea("Estudiar")
    g.agregar_tarea("Entrenar")

    g.completar_tarea(0)
    g.eliminar_tarea(1)

    assert len(g.tareas) == 1
    assert g.tareas[0].completada is True
