from clinica import Paciente, Medico, Clinica
import time


def test_rendimiento_registrar_muchos_pacientes():
    c = Clinica()

    inicio = time.time()

    for i in range(1000):
        c.agregar_paciente(Paciente(str(i), f"Paciente {i}"))

    fin = time.time()

    assert (fin - inicio) < 1  # menos de 1 segundo
