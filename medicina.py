class Medicina:
    # NUESTRO NUEVO CONSTRUCTO   
    def __init__(self,nombre,precio,descripcion,cantidad,idMed,compradas):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.idMed = idMed
        self.compradas = compradas

        
        

    # METODOS GET
    def getNombre(self):
        return self.nombre
    
    def getPrecio(self):
        return self.precio
    
    def getDescripicion(self):
        return self.descripcion
    
    def getCantidad(self):
        return self.cantidad

    def getIdmed(self):
        return self.idMed

    def getCompradas(self):
        return self.compradas
         
    # METODOS SET
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setPrecio(self, precio):
        self.precio = precio
    
    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def setCantidad(self,cantidad):
        self.cantidad = cantidad

    def setIdmed(self,idMed):
        self.idMed = idMed
    
    def setCompradas(self,compradas):
        self.compradas = compradas