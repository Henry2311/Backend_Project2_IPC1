class Carrito:
    # NUESTRO NUEVO CONSTRUCTO   
    def __init__(self,idPaciente,medicina,cantidad,precio,subtotal):
        self.idPaciente = idPaciente
        self.medicina=medicina
        self.cantidad=cantidad
        self.precio=precio
        self.subtotal=subtotal

    # METODOS GET
    def getIdPaciente(self):
        return self.idPaciente
    
    def getMedicina(self):
        return self.medicina
    
    def getCantidad(self):
        return self.cantidad
    
    def getPrecio(self):
        return self.precio
    
    def getSubtotal(self):
        return self.subtotal

     # METODOS SET
    def setIdPaciente(self, idPaciente):
        self.idPaciente = idPaciente

    def setMedicina(self,medicina):
        self.medicina=medicina
    
    def setCantidad(self,cantidad):
        self.cantidad=cantidad
    
    def setPrecio(self,precio):
        self.precio=precio
    
    def setSubtotal(self,subtotal):
        self.subtotal=subtotal