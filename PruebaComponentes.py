from gestor import Tarea, GestorTareas

def test_tarea_creacion():
    t = Tarea("Estudiar")
    assert t.nombre == "Estudiar"
    assert t.completada is False

def test_tarea_completar():
    t = Tarea("Leer")
    t.completar()
    assert t.completada is True

def test_gestor_agregar():
    g = GestorTareas()
    resultado = g.agregar_tarea("Programar")
    assert resultado is True
    assert len(g.tareas) == 1
