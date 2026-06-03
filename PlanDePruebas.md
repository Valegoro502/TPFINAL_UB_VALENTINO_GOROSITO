# Plan de Pruebas – Sistema de Gestión de Turnos Médicos

## 1. Objetivo

Verificar el correcto funcionamiento del software "Sistema de Gestión de Turnos Médicos" mediante un conjunto de pruebas que cubran distintos niveles y técnicas de testing.

## 2. Alcance

Se probará el módulo `clinica.py` (clases `Paciente`, `Medico`, `Turno` y `Clinica`) y la interfaz de consola (`main.py`).

## 3. Tipos de Pruebas a Realizar

### 3.1 Prueba de Componentes (`test_PruebaComponentes.py`)

**Objetivo:** Verificar que cada clase y método funcione correctamente de forma aislada.

| ID | Caso de prueba | Entrada | Resultado esperado |
|----|----------------|---------|-------------------|
| TC-01 | Crear un Paciente | dni="123", nombre="Juan" | Objeto Paciente con dni="123", nombre="Juan" |
| TC-02 | Crear un Médico | mat="M1", nombre="Ana", esp="Cardio" | Objeto Médico correcto |
| TC-03 | Agregar paciente a Clinica | agregar_paciente(Paciente) | Retorna True, paciente en lista |

### 3.2 Prueba de Integración (`test_IntegracionPrueba.py`)

**Objetivo:** Verificar la interacción entre componentes (Paciente + Médico + Clínica + Turno).

| ID | Caso de prueba | Flujo | Resultado esperado |
|----|----------------|-------|-------------------|
| TI-01 | Flujo completo | Agregar Paciente y Médico → Reservar Turno → Cancelar Turno | Estado de Clínica consistente (turnos creados y eliminados correctamente) |

### 3.3 Prueba de Caja Negra (`test_CajaNegra.py`)

**Objetivo:** Probar entradas y salidas sin conocer la implementación interna.

| ID | Caso de prueba | Entrada | Resultado esperado |
|----|----------------|---------|-------------------|
| TCN-01 | Registrar paciente válido | DNI y Nombre | True |
| TCN-02 | Registrar paciente duplicado | DNI existente | False |
| TCN-03 | Reservar turno válido | DNI y Matrícula existentes | True |
| TCN-04 | Reservar turno paciente inexistente | DNI no registrado | False |
| TCN-05 | Reservar turno médico inexistente | Matrícula no registrada | False |
| TCN-06 | Cancelar turno existente | DNI y Matrícula del turno | True |
| TCN-07 | Cancelar turno inexistente | DNI y Matrícula sin turno | False |

### 3.4 Prueba de Rendimiento (`test_PruebaDeRendimiento.py`)

**Objetivo:** Verificar que el sistema opere dentro de los límites de rendimiento aceptables.

| ID | Caso de prueba | Operación | Criterio |
|----|----------------|-----------|----------|
| TR-01 | Registrar 1000 pacientes | agregar_paciente() x1000 | < 1 segundo |

### 3.5 Prueba de Interfaz (`test_PruebaInterfaz.py`)

**Objetivo:** Verificar que la salida en consola sea correcta.

| ID | Caso de prueba | Acción | Resultado esperado en consola |
|----|----------------|--------|-------------------------------|
| TIF-01 | Mostrar médicos | mostrar_medicos() | Imprime datos del médico |
| TIF-02 | Mostrar sin turnos | mostrar_turnos() | Muestra "No hay turnos registrados" |

### 3.6 Prueba de Camino (`test_PruebaCamino.py`)

**Objetivo:** Cubrir los distintos caminos de ejecución del método `reservar_turno()`.

| ID | Caso de prueba | Camino | Resultado esperado |
|----|----------------|--------|-------------------|
| TPC-01 | Camino 1: Éxito | Paciente existe, Médico existe | Retorna True |
| TPC-02 | Camino 2: Falla 1 | Paciente no existe | Retorna False (sale temprano) |
| TPC-03 | Camino 3: Falla 2 | Paciente existe, Médico no existe | Retorna False (sale después) |

### 3.7 Prueba End-to-End (`test_E2E.py`)

**Objetivo:** Simular flujos completos de usuario a través de la interfaz de consola.

| ID | Caso de prueba | Flujo simulado | Resultado esperado |
|----|----------------|----------------|-------------------|
| TE-01 | Flujo completo | Registrar Paciente → Registrar Médico → Reservar Turno → Mostrar Turnos → Cancelar Turno → Salir | Mensajes de éxito en todas las operaciones |
| TE-02 | Manejo de errores | Reservar turno con datos falsos | Mensajes de error controlados ("No se encontró...") |

## 4. Herramientas

- **Framework de testing:** pytest 9.0.3
- **Lenguaje:** Python 3.13.2
- **Mocking:** unittest.mock (para E2E)
- **Captura de salida:** capsys (fixture de pytest)

## 5. Orden de Ejecución

1. Pruebas de Componentes
2. Pruebas de Integración
3. Pruebas de Caja Negra
4. Pruebas de Rendimiento
5. Pruebas de Interfaz
6. Pruebas de Camino
7. Pruebas End-to-End

## 6. Criterios de Éxito

- **100% de tests pasados** (0 fallos)
- **Rendimiento** < 1 segundo para 1000 registros
- **Cobertura** de requerimientos funcionales y caminos principales
