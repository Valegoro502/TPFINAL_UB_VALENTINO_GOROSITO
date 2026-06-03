from clinica import Paciente, Medico, Clinica


def menu():
    clinica = Clinica()

    while True:
        print("\n=== SISTEMA DE TURNOS MÉDICOS ===")
        print("1. Registrar paciente")
        print("2. Registrar médico")
        print("3. Reservar turno")
        print("4. Cancelar turno")
        print("5. Mostrar médicos")
        print("6. Mostrar turnos")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            dni = input("DNI: ")
            nombre = input("Nombre: ")
            paciente = Paciente(dni, nombre)
            if clinica.agregar_paciente(paciente):
                print("Paciente registrado correctamente")

        elif opcion == "2":
            matricula = input("Matrícula: ")
            nombre = input("Nombre: ")
            especialidad = input("Especialidad: ")
            medico = Medico(matricula, nombre, especialidad)
            if clinica.agregar_medico(medico):
                print("Médico registrado correctamente")

        elif opcion == "3":
            dni = input("DNI del paciente: ")
            matricula = input("Matrícula del médico: ")
            fecha = input("Fecha del turno: ")
            if clinica.reservar_turno(dni, matricula, fecha):
                print("Turno reservado correctamente")

        elif opcion == "4":
            dni = input("DNI del paciente: ")
            matricula = input("Matrícula del médico: ")
            clinica.cancelar_turno(dni, matricula)

        elif opcion == "5":
            clinica.mostrar_medicos()

        elif opcion == "6":
            clinica.mostrar_turnos()

        elif opcion == "7":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    menu()
