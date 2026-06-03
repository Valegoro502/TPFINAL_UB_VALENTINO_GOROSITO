from clinica import Paciente, Medico, Clinica


def test_camino_reservar_turno_exitoso():
    """Camino 1: paciente y médico existen -> turno creado"""
    c = Clinica()
    c.agregar_paciente(Paciente("12345678", "Juan"))
    c.agregar_medico(Medico("M001", "García", "Cardiología"))
    resultado = c.reservar_turno("12345678", "M001", "15/06/2026")
    assert resultado is True


def test_camino_paciente_no_encontrado():
    """Camino 2: paciente no existe -> retorna False en la primera validación"""
    c = Clinica()
    c.agregar_medico(Medico("M001", "García", "Cardiología"))
    resultado = c.reservar_turno("99999999", "M001", "15/06/2026")
    assert resultado is False


def test_camino_medico_no_encontrado():
    """Camino 3: paciente existe pero médico no -> retorna False en la segunda validación"""
    c = Clinica()
    c.agregar_paciente(Paciente("12345678", "Juan"))
    resultado = c.reservar_turno("12345678", "M999", "15/06/2026")
    assert resultado is False
