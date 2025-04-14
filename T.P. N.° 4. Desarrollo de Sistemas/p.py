from datetime import datetime

class Cita:
    def __init__(self, paciente, fecha):
        self.paciente = paciente
        self.fecha = fecha

    def descripcion(self):
        return "Descripción de la cita."

class CitaMedicaGeneral(Cita):
    def descripcion(self):
        return f"Cita médica general para {self.paciente} el {self.fecha.strftime('%d/%m/%Y a las %H:%M')}."

class CitaOdontologica(Cita):
    def descripcion(self):
        return f"Cita odontológica para {self.paciente} el {self.fecha.strftime('%d/%m/%Y a las %H:%M')}."

class CitaPediatrica(Cita):
    def descripcion(self):
        return f"Cita pediátrica para {self.paciente} el {self.fecha.strftime('%d/%m/%Y a las %H:%M')}."

class CitaFactory:
    @staticmethod
    def crear_cita(tipo, paciente, fecha):
        if tipo == "medica":
            return CitaMedicaGeneral(paciente, fecha)
        elif tipo == "odontologica":
            return CitaOdontologica(paciente, fecha)
        elif tipo == "pediatrica":
            return CitaPediatrica(paciente, fecha)
        else:
            raise ValueError("Tipo de cita no válido.")