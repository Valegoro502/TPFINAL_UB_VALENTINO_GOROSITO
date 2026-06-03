from clinica import Paciente, Medico, Clinica


def test_integracion_flujo_completo():
    c = Clinica()

    c.agregar_paciente(Paciente("12345678", "Juan Pérez"))
    c.agregar_medico(Medico("M001", "García", "Cardiología"))

    c.reservar_turno("12345678", "M001", "15/06/2026")
    assert len(c.turnos) == 1

    c.cancelar_turno("12345678", "M001")
    assert len(c.turnos) == 0
