def test_caja_negra_agregar_valido():
    g = GestorTareas()
    assert g.agregar_tarea("Leer") is True

def test_caja_negra_agregar_invalido():
    g = GestorTareas()
    assert g.agregar_tarea("") is False

def test_caja_negra_busqueda():
    g = GestorTareas()
    g.agregar_tarea("Estudiar")
    resultado = g.buscar_tarea("Estudiar")
    assert len(resultado) == 1
