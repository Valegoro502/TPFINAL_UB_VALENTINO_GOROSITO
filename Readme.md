**Sistema de Gestión de Turnos Médicos**

## Descripción General

El sistema permite administrar turnos médicos mediante consola. Está desarrollado utilizando Programación Orientada a Objetos en Python.

El software permite:

- Registrar pacientes.
- Registrar médicos.
- Reservar turnos.
- Cancelar turnos.
- Consultar turnos registrados.
- Consultar médicos disponibles.

El objetivo principal es automatizar la administración básica de turnos médicos.

## 1.1 Descriptivo del Software

### Objetivo del Software

Desarrollar un sistema orientado a objetos que permita gestionar turnos médicos de manera simple y eficiente.

El sistema busca:

- Organizar información de pacientes y médicos.
- Registrar turnos.
- Cancelar turnos.
- Facilitar consultas rápidas.

### Requerimientos Funcionales

**RF01 – Registrar paciente**
El sistema debe permitir registrar pacientes indicando DNI y Nombre.

**RF02 – Registrar médico**
El sistema debe permitir registrar médicos indicando Matrícula, Nombre y Especialidad.

**RF03 – Reservar turno**
El sistema debe permitir reservar un turno entre un paciente y un médico, validando su existencia.

**RF04 – Cancelar turno**
El sistema debe permitir cancelar un turno previamente registrado.

**RF05 – Mostrar médicos**
El sistema debe listar todos los médicos registrados.

**RF06 – Mostrar turnos**
El sistema debe mostrar todos los turnos registrados.

### Requerimientos No Funcionales

**RNF01 – Usabilidad**
El sistema debe poseer un menú simple y fácil de utilizar.

**RNF02 – Rendimiento**
Las operaciones deben ejecutarse en menos de 2 segundos.

**RNF03 – Mantenibilidad**
El código debe estar organizado en clases y métodos reutilizables.

**RNF04 – Compatibilidad**
El software debe ejecutarse en Python 3.10 o superior.
El software de pruebas debe ejecutarse con Python 3.10 o superior y con el paquete de pytest instalado.

## Estructura del Proyecto

```
tpfinal/
├── clinica.py                   # Módulo principal (clases Paciente, Medico, Turno, Clinica)
├── main.py                      # Interfaz de consola (menú interactivo)
├── test_PruebaComponentes.py    # Pruebas de componentes
├── test_IntegracionPrueba.py    # Pruebas de integración
├── test_CajaNegra.py            # Pruebas de caja negra
├── test_PruebaDeRendimiento.py  # Pruebas de rendimiento
├── test_PruebaInterfaz.py       # Pruebas de interfaz
├── test_PruebaCamino.py         # Pruebas de camino
├── test_E2E.py                  # Pruebas End-to-End
├── PlanDePruebas.md             # Plan de pruebas
├── DocumentacionEjecucion.md    # Documentación de ejecución
├── resultado_tests.log          # Log de ejecución de pruebas
├── ejecutar.sh / ejecutar.bat   # Scripts de ejecución
├── ejecutar_pruebas.sh / .bat   # Scripts de ejecución de pruebas
└── Readme.md                    # Este archivo
```

## Ejecución

```bash
# Windows
ejecutar.bat

# Linux/Mac
bash ejecutar.sh
```

## Ejecución de Pruebas

```bash
# Windows
ejecutar_pruebas.bat

# Linux/Mac
bash ejecutar_pruebas.sh
```

# Diagrama UML

![Diagrama UML y Diagrama de casos de uso](uml_clinica.png)
