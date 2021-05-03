class Doctor:
    # NUESTRO NUEVO CONSTRUCTOR   
    def __init__(self,nombre,apellido,user,contraseña,fecha,telefono,especialidad,genero,atendidas):
        self.nombre = nombre
        self.apellido = apellido
        self.user = user
        self.contraseña = contraseña
        self.fecha = fecha
        self.telefono = telefono
        self.especialidad = especialidad
        self.genero = genero
        self.atendidas = atendidas

    # METODOS GET
    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido
    
    def getUser(self):
        return self.user
    
    def getContraseña(self):
        return self.contraseña
    
    def getFecha(self):
        return self.fecha
    
    def getTelefono(self):
        return self.telefono
    
    def getEspecialidad(self):
        return self.especialidad
    
    def getGenero(self):
        return self.genero

    def getAtendidas(self):
        return self.atendidas 

    # METODOS SET
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setApellido(self, apellido):
        self.apellido = apellido
    
    def setUser(self, user):
        self.user = user

    def setContraseña(self,contraseña):
        self.contraseña = contraseña
    
    def setFecha(self,fecha):
        self.fecha = fecha
    
    def setTelefono(self,telefono):
        self.telefono = telefono
    
    def setEspecialidad(self,especialidad):
        self.especialidad = especialidad 
    
    def setGenero(self,genero):
        self.genero = genero     
    
    def setAtendidas(self,atendidas):
        self.atendidas = atendidas