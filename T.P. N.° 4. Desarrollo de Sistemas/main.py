from datetime import datetime
from p import CitaFactory

if __name__ == "__main__":
    paciente = "Juan Pérez"
    tipo_cita = "odontologica"
    fecha_cita = datetime(2025, 5, 10, 14, 30)

    cita = CitaFactory.crear_cita(tipo_cita, paciente, fecha_cita)
    print(cita.descripcion())