class Administrador:
    # NUESTRO NUEVO CONSTRUCTO   
    def __init__(self,nombre,apellido,user,contraseña):
        self.nombre = nombre
        self.apellido = apellido
        self.user = user
        self.contraseña = contraseña

    # METODOS GET
    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido
    
    def getUser(self):
        return self.user
    
    def getContraseña(self):
        return self.contraseña

    # METODOS SET
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setApellido(self, apellido):
        self.apellido = apellido
    
    def setUser(self, user):
        self.user = user

    def setContraseña(self,contraseña):
        self.contraseña = contraseña

