# TRA-001 - Matriz de Trazabilidad de SoftEdu-MCS-Activity

## Información del elemento de configuración

- Código del CI: TRA-001
- Nombre: Matriz de Trazabilidad
- Proyecto: SoftEdu-MCS-Activity
- Versión: 1.1
- Estado: En modificacion por CR-001
- Fecha: 09/18/2026
- Responsable: Equipo SoftEdu-MCS-Activity
- Responsable del cambio: Revant11y

## Historial de versiones

| Versión | Fecha | Descripción del cambio | Responsable |
|---------|-------|------------------------|-------------|
| 1.0 | 09/09/2026 | Creación inicial de la matriz de trazabilidad | Equipo SoftEdu-MCS-Activity |
| 1.1 | 09/18/2026 | Actualización de la trazabilidad asociada a CR-001 - Agregar teléfono al estudiante | Revant11y |

## 1. Objetivo

Relacionar los requisitos definidos para SoftEdu-MCS-Activity con los elementos de diseño, código fuente y pruebas que los implementan o verifican.

La matriz permite identificar qué elementos de configuración deben revisarse cuando un requisito sea modificado.

## 2. Matriz de trazabilidad inicial

| Requisito | Descripción | Diseño relacionado | Código relacionado | Prueba relacionada | Estado |
|-----------|-------------|--------------------|--------------------|--------------------|--------|
| RF-01 | Registrar estudiante | DIS-001 v1.1 - Entidad Estudiante | SRC-001 v1.1 - Gestión de Estudiantes | TST-001 v1.1 / CP-01 | Completa |
| RF-02 | Consultar estudiante | DIS-001 v1.1 - Entidad Estudiante | SRC-001 v1.1 - Gestión de Estudiantes | TST-001 v1.1 / CP-02 | Completa |
| RF-03 | Registrar curso | DIS-001 v1.1 - Entidad Curso | Pendiente de implementación | TST-001 v1.1 / CP-03 | Parcial |
| RF-04 | Matricular estudiante | DIS-001 v1.1 - Entidad Matrícula | Pendiente de implementación | TST-001 v1.1 / CP-04 | Parcial |

## 3. Relación entre elementos de configuración afectados por CR-001

La solicitud de cambio CR-001 afecta la funcionalidad de registro de estudiantes y genera la siguiente cadena de trazabilidad:
CR-001- Agregar teléfono al estudiante
↓
REQ-001 v1.1 - RF-01 Registrar estudiante
↓
DIS-001 v1.1 - Entidad Estudiante
↓
SRC-001 v1.1 - Gestión de Estudiantes
↓
TST-001 v1.1 - CP-01 Registrar estudiante correctamente
↓
TRA-001 v1.1 - Actualización de la trazabilidad
↓
Pull Request pendiente


## 4. Trazabilidad por requisito


### RF-01 - Registrar estudiante

- Requisito: REQ-001 v1.1
- Cambio asociado: CR-001 - Agregar teléfono al estudiante
- Diseño asociado: DIS-001 v1.1 - Entidad Estudiante
- Código asociado: SRC-001 v1.1 - Gestión de Estudiantes
- Caso de prueba asociado: TST-001 v1.1 / CP-01
- Estado de trazabilidad: Completa

### RF-02 - Consultar estudiante

- Requisito: REQ-001 v1.1
- Diseño asociado: DIS-001 v1.1 - Entidad Estudiante
- Código asociado: SRC-001 v1.1 - Gestión de Estudiantes
- Caso de prueba asociado: TST-001 v1.1 / CP-02
- Estado de trazabilidad: Completa

### RF-03 - Registrar curso

- Caso de prueba asociado: TST-001 v1.1 / CP-02
- Requisito: REQ-001 v1.1
- Diseño asociado: DIS-001 v1.1 - Entidad Curso
- Código asociado: Pendiente
- Caso de prueba asociado: TST-001 v1.1 / CP-03
- Estado de trazabilidad: Parcial

### RF-04 - Matricular estudiante

- Requisito: REQ-001 v1.1
- Diseño asociado: DIS-001 v1.1 - Entidad Matrícula
- Código asociado: Pendiente
- Caso de prueba asociado: TST-001 v1.1 / CP-04
- Estado de trazabilidad: Parcial
- 
## 5. Trazabilidad de cambios

Toda solicitud de cambio aprobada para implementación debe permitir identificar los elementos afectados y seguir su evolución hasta la revisión e integración final.

Para CR-001, se registra la siguiente trazabilidad:

Solicitud de cambio CR-001 - Issue #1

↓

RF-01 de REQ-001 v1.1

↓

DIS-001 v1.1

↓

SRC-001 v1.1

↓

TST-001 v1.1 / CP-01

↓

TRA-001 v1.1

## 6. Registro de cambios trazables

| Solicitud de cambio | Requisito afectado | Diseño afectado | Código afectado | Prueba afectada | Commit / PR | Estado |
|--------------------|--------------------|-----------------|-----------------|-----------------|-------------|--------|
| Sin cambios aprobados en la versión 1.0 | - | - | - | - | - | Línea base inicial |
| CR-001 - Agregar teléfono al estudiante | REQ-001 v1.1 / RF-01 | DIS-001 v1.1 | SRC-001 v1.1 | TST-001 v1.1 / CP-01 | Commits Realizados /PR pendiente | Pendiente en implementacion  |

## 7. Observaciones

Este documento constituye el Elemento de Configuración TRA-001.

La versión 1.0 representa la trazabilidad correspondiente a la configuración inicial de SoftEdu-MCS-Activity establecida en BL-001.

La versión 1.1 registra el impacto y las relaciones generadas por la solicitud de cambio CR-001 - Agregar teléfono al estudiante.

CR-001 se encuentra aprobada para implementación, pero todavía está pendiente de revisión e integración en la rama
principal.

Toda modificación posterior deberá actualizar esta matriz y quedar relacionada con una solicitud de cambio aprobada.
