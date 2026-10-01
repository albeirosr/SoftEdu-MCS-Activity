# BL-002 - Segunda Línea Base de SoftEdu-MCS-Activity

## Información de la línea base

- Código: BL-002
- Proyecto: SoftEdu-MCS-Activity
- Nombre: Segunda Línea Base
- Versión del producto: 1.1
- Fecha de establecimiento: 30/09/2026
- Estado: Aprobada
- Responsable: Equipo SoftEdu-MCS-Activity
- Cambio incorporado: CR-001 - Agregar teléfono al estudiante

## 1. Objetivo

Establecer el conjunto de elementos de configuración aprobados que conforman la versión 1.1 de SoftEdu-MCS-Activity, después de la implementación, revisión, corrección y cierre de la solicitud de cambio CR-001.

Esta línea base representa el estado estable y aprobado del proyecto una vez incorporado el número de teléfono como dato del estudiante y actualizados los elementos de configuración relacionados.

## 2. Elementos incluidos en la línea base

| Código CI | Elemento de configuración | Versión | Estado |
|-----------|---------------------------|---------|--------|
| REQ-001 | Especificación de Requisitos | 1.1 | Aprobado |
| DIS-001 | Diseño del Sistema | 1.1 | Aprobado |
| SRC-001 | Gestión de Estudiantes | 1.1 | Aprobado |
| TST-001 | Plan y Casos de Prueba | 1.1 | Aprobado |
| TRA-001 | Matriz de Trazabilidad | 1.1 | Aprobado |

## 3. Relaciones de trazabilidad

La configuración aprobada mantiene la siguiente relación:

CR-001 - Agregar teléfono al estudiante
↓
REQ-001 v1.1
↓
DIS-001 v1.1
↓
SRC-001 v1.1
↓
TST-001 v1.1

TRA-001 v1.1 documenta las relaciones existentes entre la solicitud de cambio, los elementos de configuración, los commits realizados y los Pull Requests asociados.

## 4. Criterio de establecimiento

La línea base BL-002 se establece debido a que:

- La solicitud de cambio CR-001 fue implementada y cerrada.
- Los requisitos afectados fueron actualizados y aprobados en su versión 1.1.
- El diseño fue actualizado para incorporar el atributo teléfono.
- El código fuente fue modificado para almacenar y consultar el número de teléfono del estudiante.
- Los casos de prueba relacionados fueron actualizados y ejecutados.
- La matriz de trazabilidad fue actualizada para reflejar los cambios realizados.
- Los cambios fueron desarrollados mediante ramas de trabajo controladas.
- Las correcciones identificadas durante la práctica fueron realizadas mediante ramas adicionales y Pull Requests.
- Los cambios fueron revisados, aprobados y fusionados a la rama principal.
- Los elementos de configuración afectados se encuentran en un estado estable y aprobado.

## 5. Cambios incorporados desde BL-001

La línea base BL-002 incorpora la solicitud de cambio:

CR-001 - Agregar teléfono al estudiante.

Como consecuencia de esta solicitud se realizaron las siguientes modificaciones:

- REQ-001 fue actualizado para incluir el número de teléfono como dato del estudiante.
- DIS-001 fue actualizado para incorporar el atributo teléfono en la entidad Estudiante.
- SRC-001 fue actualizado para recibir, almacenar y mostrar el número de teléfono.
- TST-001 fue actualizado para validar el nuevo atributo mediante el caso de prueba correspondiente.
- TRA-001 fue actualizado para mantener la trazabilidad entre la solicitud de cambio, requisitos, diseño, código, pruebas, commits y Pull Requests.

Durante el proceso también se realizaron correcciones adicionales de documentación y trazabilidad mediante ramas y Pull Requests independientes, manteniendo el proceso controlado de gestión de cambios.

## 6. Evidencia de aprobación

La configuración correspondiente a BL-002 fue revisada y aprobada mediante Pull Request antes de su integración a la rama principal.

El cierre de CR-001 y las correcciones posteriores fueron integrados a `main` mediante el proceso colaborativo definido para el proyecto.

BL-002 representa por lo tanto el estado aprobado del repositorio posterior al cierre de CR-001.

## 7. Control posterior de cambios

Una vez establecida BL-002, los elementos incluidos no deberán modificarse directamente sin identificar y documentar una nueva solicitud de cambio.

Todo cambio posterior deberá:

1. Originarse en una nueva solicitud de cambio.
2. Identificar los CI afectados.
3. Analizar su impacto.
4. Realizarse en una rama de trabajo.
5. Quedar registrado mediante commits.
6. Ser revisado mediante Pull Request.
7. Ser aprobado antes de integrarse a la rama principal.
8. Actualizar la trazabilidad correspondiente.
9. Generar, cuando corresponda, una nueva versión y una nueva línea base.

## 8. Identificación técnica

La línea base BL-002 será identificada en el repositorio Git mediante la etiqueta:

`v1.1`

Esta etiqueta permitirá recuperar posteriormente el estado exacto del repositorio correspondiente a la segunda línea base aprobada.

La etiqueta `v1.0` continuará identificando la línea base BL-001 y no será modificada.

## 9. Observaciones

BL-002 representa la configuración aprobada de SoftEdu-MCS-Activity después de incorporar y cerrar la solicitud de cambio CR-001.

La línea base BL-001 permanece disponible mediante la etiqueta `v1.0`, mientras que BL-002 será identificada mediante la etiqueta `v1.1`.

Las ramas y Pull Requests adicionales generados durante las correcciones forman parte de la evidencia del proceso de gestión colaborativa de cambios y permiten reconstruir las modificaciones realizadas antes del establecimiento de esta línea base.