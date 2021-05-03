class Cita:
    # NUESTRO NUEVO CONSTRUCTO   
    def __init__(self,idPaciente,fecha,hora,motivo,idDoctor,idCita,estado):
        self.idPaciente = idPaciente
        self.fecha = fecha
        self.hora  = hora
        self.motivo = motivo
        self.idDoctor = idDoctor
        self.idCita= idCita
        self.estado = estado



    # METODOS GET
    def getIdPaciente(self):
        return self.idPaciente

    def getFecha(self):
        return self.fecha

    def getHora(self):
        return self.hora
    
    def getMotivo(self):
        return self.motivo
    
    def getIdDoctor(self):
        return self.idDoctor
    
    def getIdCita(self):
        return self.idCita

    def getEstado(self):
        return self.estado

     # METODOS SET
    def setIdPaciente(self, idPaciente):
        self.idPaciente = idPaciente
    
    def setFecha(self, fecha):
        self.fecha = fecha
    
    def setHora (self, hora):
        self.hora = hora

    def setMotivo(self, motivo):
        self.motivo = motivo

    def setIdDoctor(self, idDoctor):
        self.idDoctor = idDoctor
    
    def setIdCita(self, idCita):
        self.idCita = idCita

    def setEstado(self, estado):
        self.estado = estado