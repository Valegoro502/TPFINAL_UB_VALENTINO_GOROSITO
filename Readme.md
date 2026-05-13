1. Presentación del Software
Nombre del Software

Sistema de Gestión de Turnos Médicos

Descripción General

El sistema permite administrar turnos médicos mediante consola. Está desarrollado utilizando Programación Orientada a Objetos en Python.

El software permite:

Registrar pacientes.
Registrar médicos.
Reservar turnos.
Cancelar turnos.
Consultar turnos registrados.
Consultar médicos disponibles.

El objetivo principal es automatizar la administración básica de turnos médicos.

1.1 Descriptivo del Software
Objetivo del Software

Desarrollar un sistema orientado a objetos que permita gestionar turnos médicos de manera simple y eficiente.

El sistema busca:

Organizar información de pacientes y médicos.
Registrar turnos.
Cancelar turnos.
Facilitar consultas rápidas.
Requerimientos Funcionales
RF01 – Registrar paciente

El sistema debe permitir registrar pacientes indicando:

DNI
Nombre
RF02 – Registrar médico

El sistema debe permitir registrar médicos indicando:

Matrícula
Nombre
Especialidad
RF03 – Reservar turno

El sistema debe permitir reservar un turno entre un paciente y un médico.

RF04 – Cancelar turno

El sistema debe permitir cancelar un turno previamente registrado.

RF05 – Mostrar médicos

El sistema debe listar todos los médicos registrados.

RF06 – Mostrar turnos

El sistema debe mostrar todos los turnos registrados.

Requerimientos No Funcionales
RNF01 – Usabilidad

El sistema debe poseer un menú simple y fácil de utilizar.

RNF02 – Rendimiento

Las operaciones deben ejecutarse en menos de 2 segundos.

RNF03 – Mantenibilidad

El código debe estar organizado en clases y métodos reutilizables.

RNF04 – Compatibilidad

El software debe ejecutarse en Python 3.10 o superior.

# Diagrama UML

![Diagrama UML y Diagrama de casos de uso](uml.png)
