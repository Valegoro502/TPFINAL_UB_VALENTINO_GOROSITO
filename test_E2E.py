from unittest.mock import patch
from main import menu


def test_e2e_flujo_completo(capsys):
    """
    Test E2E: Simula un usuario que realiza el flujo completo:
    1. Registra un paciente
    2. Registra un médico
    3. Reserva un turno
    4. Muestra los turnos
    5. Cancela el turno
    6. Sale del sistema
    """
    inputs = iter([
        "1", "12345678", "Juan Pérez",
        "2", "M001", "García", "Cardiología",
        "3", "12345678", "M001", "15/06/2026",
        "6",
        "4", "12345678", "M001",
        "7",
    ])

    with patch("builtins.input", lambda _: next(inputs)):
        menu()

    salida = capsys.readouterr().out

    assert "Paciente registrado correctamente" in salida
    assert "Médico registrado correctamente" in salida
    assert "Turno reservado correctamente" in salida
    assert "Turno cancelado correctamente" in salida
    assert "Saliendo del sistema" in salida


def test_e2e_manejo_errores(capsys):
    """
    Test E2E: Verifica que el sistema maneja correctamente
    entradas inválidas del usuario sin crashear.
    """
    inputs = iter([
        "9",
        "3", "99999999", "M999", "01/01/2026",
        "7",
    ])

    with patch("builtins.input", lambda _: next(inputs)):
        menu()

    salida = capsys.readouterr().out

    assert "Opción inválida" in salida
    assert "No se encontró el paciente" in salida
