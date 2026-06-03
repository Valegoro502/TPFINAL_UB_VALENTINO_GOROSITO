from clinica import Paciente, Medico, Clinica


def test_interfaz_mostrar_medicos(capsys):
    c = Clinica()
    c.agregar_medico(Medico("M001", "García", "Cardiología"))

    c.mostrar_medicos()
    salida = capsys.readouterr().out

    assert "García" in salida


def test_interfaz_sin_turnos(capsys):
    c = Clinica()

    c.mostrar_turnos()
    salida = capsys.readouterr().out

    assert "No hay turnos registrados" in salida
