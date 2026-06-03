from clinica import Paciente, Medico, Turno, Clinica


def test_paciente_creacion():
    p = Paciente("12345678", "Juan Pérez")
    assert p.dni == "12345678"
    assert p.nombre == "Juan Pérez"


def test_medico_creacion():
    m = Medico("M001", "García", "Cardiología")
    assert m.matricula == "M001"
    assert m.nombre == "García"
    assert m.especialidad == "Cardiología"


def test_clinica_agregar_paciente():
    c = Clinica()
    p = Paciente("12345678", "Juan Pérez")
    resultado = c.agregar_paciente(p)
    assert resultado is True
    assert len(c.pacientes) == 1
