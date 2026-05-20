class Tarea:
    def __init__(self, nombre):
        self.nombre = nombre
        self.completada = False

    def completar(self):
        self.completada = True

    def __str__(self):
        estado = "Completada" if self.completada else "Pendiente"
        return f"{self.nombre} - {estado}"



class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, nombre):
        if nombre.strip() == "":
            return False
        self.tareas.append(Tarea(nombre))
        return True

    def completar_tarea(self, index):
        if 0 <= index < len(self.tareas):
            self.tareas[index].completar()
            return True
        else:
            print("Índice inválido")
            return False

    def eliminar_tarea(self, index):
        if 0 <= index < len(self.tareas):
            self.tareas.pop(index)
            return True
        return False

    def buscar_tarea(self, nombre):
        return [t for t in self.tareas if nombre.lower() in t.nombre.lower()]

    def listar_tareas(self):
        if not self.tareas:
            print("No hay tareas")
        for i, tarea in enumerate(self.tareas):
         print(f"{i}: {tarea}")