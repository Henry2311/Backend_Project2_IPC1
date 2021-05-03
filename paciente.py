class Paciente:
    # NUESTRO NUEVO CONSTRUCTO   
    def __init__(self,nombre,apellido,user,contraseña,fecha,telefono,genero,carrito):
        self.nombre = nombre
        self.apellido = apellido
        self.user = user
        self.contraseña = contraseña
        self.fecha = fecha
        self.telefono = telefono
        self.genero = genero
        self.carrito = carrito

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
    
    def getGenero(self):
        return self.genero

    def getCarrito(self):
        return self.carrito

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
    
    def setGenero(self,genero):
        self.genero = genero  

    def setCarrito(self,carrito):
        self.carrito = carrito  
