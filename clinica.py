class Paciente:
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre

    def __str__(self):
        return f"Paciente: {self.nombre} (DNI: {self.dni})"


class Medico:
    def __init__(self, matricula, nombre, especialidad):
        self.matricula = matricula
        self.nombre = nombre
        self.especialidad = especialidad

    def __str__(self):
        return f"Dr. {self.nombre} - {self.especialidad} (Mat: {self.matricula})"


class Turno:
    def __init__(self, paciente, medico, fecha):
        self.paciente = paciente
        self.medico = medico
        self.fecha = fecha

    def __str__(self):
        return f"Turno: {self.paciente.nombre} con Dr. {self.medico.nombre} - Fecha: {self.fecha}"


class Clinica:
    def __init__(self):
        self.pacientes = []
        self.medicos = []
        self.turnos = []

    def agregar_paciente(self, paciente):
        for p in self.pacientes:
            if p.dni == paciente.dni:
                print("Ya existe un paciente con ese DNI")
                return False
        self.pacientes.append(paciente)
        return True

    def agregar_medico(self, medico):
        for m in self.medicos:
            if m.matricula == medico.matricula:
                print("Ya existe un médico con esa matrícula")
                return False
        self.medicos.append(medico)
        return True

    def buscar_paciente(self, dni):
        for p in self.pacientes:
            if p.dni == dni:
                return p
        return None

    def buscar_medico(self, matricula):
        for m in self.medicos:
            if m.matricula == matricula:
                return m
        return None

    def reservar_turno(self, dni, matricula, fecha):
        paciente = self.buscar_paciente(dni)
        if paciente is None:
            print("No se encontró el paciente")
            return False
        medico = self.buscar_medico(matricula)
        if medico is None:
            print("No se encontró el médico")
            return False
        turno = Turno(paciente, medico, fecha)
        self.turnos.append(turno)
        return True

    def cancelar_turno(self, dni, matricula):
        for turno in self.turnos:
            if turno.paciente.dni == dni and turno.medico.matricula == matricula:
                self.turnos.remove(turno)
                print("Turno cancelado correctamente")
                return True
        print("No existe ese turno")
        return False

    def mostrar_medicos(self):
        if not self.medicos:
            print("No hay médicos registrados")
        else:
            for medico in self.medicos:
                print(medico)

    def mostrar_turnos(self):
        if not self.turnos:
            print("No hay turnos registrados")
        else:
            for turno in self.turnos:
                print(turno)
