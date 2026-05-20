def test_camino_valido():
    g = GestorTareas()
    g.agregar_tarea("Estudiar")

    resultado = g.completar_tarea(0)
    assert resultado is True


def test_camino_indice_negativo():
    g = GestorTareas()
    g.agregar_tarea("Estudiar")

    resultado = g.completar_tarea(-1)
    assert resultado is False


def test_camino_fuera_rango():
    g = GestorTareas()
    g.agregar_tarea("Estudiar")

    resultado = g.completar_tarea(10)
    assert resultado is False
