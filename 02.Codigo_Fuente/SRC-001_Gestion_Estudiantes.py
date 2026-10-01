# SRC-001 - Gestión de Estudiantes
# Proyecto: SoftEdu-MSC-Activity
# Versión: 1.1
# Estado: Aprobado.
# Fecha: 9/24/2026
# Responsable: Equipo SoftEdu-MCS-Activity
# Responsable del cambio: Revant11y

# Nota de actualización documental — 29/09/2026:
# Se actualiza el estado de SRC-001 a Aprobado, conforme a la aprobación
# de CR-001 registrada por Revant11y en el PR #2, ya integrado en main.
# Se conserva la versión 1.1 y el código funcional.
# Responsable de la actualización: SaraArias801.


class Estudiante:
    def __init__(self, identificacion, nombre_completo, correo_electronico,telefono):
        self.identificacion = identificacion
        self.nombre_completo = nombre_completo
        self.correo_electronico = correo_electronico
        self.telefono =telefono

    def mostrar_informacion(self):
        return {
            "identificacion": self.identificacion,
            "nombre_completo": self.nombre_completo,
            "correo_electronico": self.correo_electronico,
            "telefono": self.telefono
        }


def registrar_estudiante(identificacion, nombre_completo, correo_electronico):
    estudiante = Estudiante(
        identificacion,
        nombre_completo,
        correo_electronico
    )

    return estudiante
