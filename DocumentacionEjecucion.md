# Documentación de Ejecución de Pruebas

## 1. Información General

| Campo | Valor |
|-------|-------|
| **Software probado** | Sistema de Gestión de Turnos Médicos |
| **Versión de Python** | 3.13.2 |
| **Framework de testing** | pytest 9.0.3 |
| **Sistema operativo** | Windows |
| **Fecha de ejecución** | Junio 2026 |

## 2. Comando de Ejecución

```bash
py -m pytest -v
```

## 3. Resultados de Ejecución

### Resumen

| Métrica | Valor |
|---------|-------|
| **Tests ejecutados** | 19 |
| **Tests aprobados** | 19 |
| **Tests fallidos** | 0 |
| **Tiempo total** | < 1 segundo |
| **Tasa de éxito** | 100% |

### Detalle por Tipo de Prueba

#### Pruebas de Componentes (3/3 PASSED)
Verifican la correcta creación de `Paciente`, `Medico` y el agregado de pacientes a la `Clinica`.

#### Prueba de Integración (1/1 PASSED)
Verifica el flujo integral combinando `Paciente`, `Medico`, `Clinica` y `Turno`.

#### Pruebas de Caja Negra (7/7 PASSED)
Valida los inputs de la clase `Clinica` probando datos válidos (creación de turnos y cancelación) y datos inválidos (DNI duplicado, paciente/médico inexistente).

#### Prueba de Rendimiento (1/1 PASSED)
Comprueba que registrar 1000 pacientes se realiza en menos de 1 segundo.

#### Pruebas de Interfaz (2/2 PASSED)
Verifica que la salida estándar (stdout) sea correcta al mostrar médicos y al intentar mostrar turnos cuando no hay ninguno.

#### Pruebas de Camino (3/3 PASSED)
Prueba los 3 caminos lógicos de la función `reservar_turno`: éxito total, salida por paciente no encontrado, y salida por médico no encontrado.

#### Pruebas End-to-End (2/2 PASSED)
Mockeando la función `input()`, recorre la aplicación de consola de principio a fin interactuando con todas sus funciones como lo haría un usuario real, validando tanto el "happy path" como el manejo de errores en inputs incorrectos.

## 4. Log Completo

El log completo de la ejecución se encuentra en el archivo `resultado_tests.log`.

## 5. Análisis de Resultados

### Cobertura de Pruebas

Se aplicaron **7 tipos de pruebas** distintas. Todos los requerimientos funcionales fueron validados a través de estas pruebas. La arquitectura de test cubre exitosamente las reglas de negocio descritas en la Especificación.

### Defectos Encontrados

No se detectaron defectos (0 fallos). El sistema se comporta de manera estable y respeta todas las validaciones definidas.

### Requerimientos No Funcionales

| RNF | Criterio | Resultado |
|-----|----------|-----------|
| RNF01 - Usabilidad | Menú simple | ✅ Cumple - Menú CLI con opciones claras |
| RNF02 - Rendimiento | < 2 segundos | ✅ Cumple - Test de rendimiento exitoso |
| RNF03 - Mantenibilidad | Código en clases | ✅ Cumple - Clases `Paciente`, `Medico`, `Turno`, `Clinica` |
| RNF04 - Compatibilidad | Python 3.10+ | ✅ Cumple - Probado en 3.13.2 |

## 6. Conclusión

El software "Sistema de Gestión de Turnos Médicos" pasó exitosamente todos los tests diseñados para cada categoría de prueba solicitada. Cumple con los RF y RNF.
