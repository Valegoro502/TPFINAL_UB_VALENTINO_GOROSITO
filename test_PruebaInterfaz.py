from gestor import Tarea, GestorTareas
def test_interfaz_listado(capsys):
    g = GestorTareas()
    g.agregar_tarea("Estudiar")

    g.listar_tareas()
    salida = capsys.readouterr().out

    assert "Estudiar" in salida


def test_interfaz_error_indice(capsys):
    g = GestorTareas()

    g.completar_tarea(5)
    salida = capsys.readouterr().out

    assert "Índice inválido" in salida

