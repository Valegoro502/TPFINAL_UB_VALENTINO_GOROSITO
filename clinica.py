class Paciente:
        for turno in self.turnos:
            if (
                turno.paciente.dni == dni
                and turno.medico.matricula == matricula
            ):
                self.turnos.remove(turno)
                print("Turno cancelado correctamente")
                return

        print("No existe ese turno")

    def mostrar_medicos(self):
        for medico in self.medicos:
            print(medico)

    def mostrar_turnos(self):
        if len(self.turnos) == 0:
            print("No hay turnos registrados")
        else:
            for turno in self.turnos:
                print(turno)


clinica = Clinica()

while True:
    print("
=== SISTEMA DE TURNOS MÉDICOS ===")
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
        clinica.agregar_paciente(paciente)

        print("Paciente registrado correctamente")

    elif opcion == "2":
        matricula = input("Matrícula: ")
        nombre = input("Nombre: ")
        especialidad = input("Especialidad: ")

        medico = Medico(matricula, nombre, especialidad)
        clinica.agregar_medico(medico)

        print("Médico registrado correctamente")

    elif opcion == "3":
        dni = input("DNI del paciente: ")
        matricula = input("Matrícula del médico: ")
        fecha = input("Fecha del turno: ")

        clinica.reservar_turno(dni, matricula, fecha)

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
