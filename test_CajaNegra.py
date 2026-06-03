from clinica import Paciente, Medico, Clinica


def test_caja_negra_registrar_paciente_valido():
    """Entrada válida: paciente con DNI y nombre -> debe retornar True"""
    c = Clinica()
    assert c.agregar_paciente(Paciente("12345678", "Juan")) is True


def test_caja_negra_registrar_paciente_duplicado():
    """Entrada inválida: DNI duplicado -> debe retornar False"""
    c = Clinica()
    c.agregar_paciente(Paciente("12345678", "Juan"))
    assert c.agregar_paciente(Paciente("12345678", "Pedro")) is False


def test_caja_negra_reservar_turno_valido():
    """Entrada válida: paciente y médico registrados -> debe retornar True"""
    c = Clinica()
    c.agregar_paciente(Paciente("12345678", "Juan"))
    c.agregar_medico(Medico("M001", "García", "Cardiología"))
    assert c.reservar_turno("12345678", "M001", "15/06/2026") is True


def test_caja_negra_reservar_paciente_inexistente():
    """Entrada inválida: paciente no registrado -> debe retornar False"""
    c = Clinica()
    c.agregar_medico(Medico("M001", "García", "Cardiología"))
    assert c.reservar_turno("99999999", "M001", "15/06/2026") is False


def test_caja_negra_reservar_medico_inexistente():
    """Entrada inválida: médico no registrado -> debe retornar False"""
    c = Clinica()
    c.agregar_paciente(Paciente("12345678", "Juan"))
    assert c.reservar_turno("12345678", "M999", "15/06/2026") is False


def test_caja_negra_cancelar_turno_existente():
    """Cancelar turno existente -> debe retornar True"""
    c = Clinica()
    c.agregar_paciente(Paciente("12345678", "Juan"))
    c.agregar_medico(Medico("M001", "García", "Cardiología"))
    c.reservar_turno("12345678", "M001", "15/06/2026")
    assert c.cancelar_turno("12345678", "M001") is True


def test_caja_negra_cancelar_turno_inexistente():
    """Cancelar turno inexistente -> debe retornar False"""
    c = Clinica()
    assert c.cancelar_turno("12345678", "M001") is False
