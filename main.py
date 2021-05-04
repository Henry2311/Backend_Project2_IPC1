from flask import Flask,jsonify,request 
from flask_cors import CORS
from datetime import datetime
from admin import Administrador
from doctor import Doctor
from enfermera import Enfermera
from paciente import Paciente
from medicina import Medicina
from citas import Cita
import json

idMed=1
idCitas=1
Doctores=[]
Enfermeras=[]
Pacientes=[]
Medicinas=[]
Citas=[]
carrito=[]
CantInicial = []

Admin=Administrador('Abner','Cardona','admin',1234)

#Citas.append(Cita("henry23","14/05/2021","14:00","Dolor de Cabeza","xd",1,"Pendiente"))

app = Flask(__name__)
CORS(app)

#METODOS DE PRUEBA
@app.route('/', methods=['GET']) 
def rutaInicial():
    prueba = {
                "Nombre":"Henry",
                "Edad":19
             }
    return(jsonify(prueba))

@app.route('/', methods=['POST']) 
def rutaPost(): 
    print("prueba post")
    prueba = {"MENSAJE":"Se hizo el post correctamente"}
    return(jsonify(prueba))


#METODOS PARA DOCTORES

@app.route('/Doctores', methods=['GET'])
def getDoctores():
    global Doctores
    Datos = []
    for doctor in Doctores:
        objeto = {
            'Nombre': doctor.getNombre(),
            'Apellido': doctor.getApellido(),
            'User': doctor.getUser(),
            'Contraseña' : doctor.getContraseña(),
            'Fecha' : doctor.getFecha(),
            'Teléfono' : doctor.getTelefono(),
            'Especialidad' : doctor.getEspecialidad(),
            'Género' : doctor.getGenero()
        }
        Datos.append(objeto)  
    return(jsonify(Datos))


@app.route('/Doctores/<string:nombre>', methods=['GET'])
def ObtenerDoctor(nombre): 
    global Doctores
    for doctor in Doctores:
        if doctor.getUser() == nombre:
            objeto = {
            'Nombre': doctor.getNombre(),
            'Apellido': doctor.getApellido(),
            'User': doctor.getUser(),
            'Contraseña' : doctor.getContraseña(),
            'Fecha' : doctor.getFecha(),
            'Teléfono' : doctor.getTelefono(),
            'Especialidad' : doctor.getEspecialidad(),
            'Género' : doctor.getGenero()
            }
            return(jsonify(objeto))      
    salida = { "Mensaje": "No existe el usuario con ese nombre"}
    return(jsonify(salida))


@app.route('/Doctores', methods=['POST'])
def AgregarDoctor():
    global Doctores
    nombre = request.json['Nombre']
    apellido = request.json['Apellido']
    user = request.json['User']
    contraseña = request.json['Contraseña']
    fecha = request.json['Fecha']
    telefono = request.json['Teléfono']
    especialidad = request.json['Especialidad']
    genero = request.json['Género']


    nuevo = Doctor(nombre,apellido,user,contraseña,fecha,telefono,especialidad,genero,0)
    Doctores.append(nuevo)
    return jsonify({'Mensaje':'Se añadió el usuario'})


@app.route('/Doctores/<string:nombre>', methods=['PUT'])
def ActualizarDoctores(nombre):
    global Doctores

    for i in range(len(Doctores)):

        if nombre == Doctores[i].getUser():

            Doctores[i].setNombre(request.json['Nombre'])
            Doctores[i].setApellido(request.json['Apellido'])
            Doctores[i].setUser(request.json['User'])
            Doctores[i].setContraseña(request.json['Contraseña'])
            Doctores[i].setFecha(request.json['Fecha'])
            Doctores[i].setTelefono(request.json['Teléfono'])
            Doctores[i].setEspecialidad(request.json['Especialidad'])
            Doctores[i].setGenero(request.json['Género'])
            return jsonify({'Mensaje':'Se actualizo el dato exitosamente'})

    return jsonify({'Mensaje':'No se encontro el dato para actualizar'})



@app.route('/Doctores/<string:nombre>', methods=['DELETE'])
def EliminarDoctor(nombre):
    global Doctores

    for i in range(len(Doctores)):

        if nombre == Doctores[i].getUser():

            del Doctores[i]
            
            return jsonify({'Mensaje':'Se elimino el dato exitosamente'})
       
    return jsonify({'Mensaje':'No se encontro el dato para eliminar'})

#METODOS PARA ENFERMERAS

@app.route('/Enfermeras', methods=['GET'])
def getEnfermera():
    global Enfermeras
    Datos = []
    for enfermera in Enfermeras:
        objeto = {
            'Nombre':enfermera.getNombre(),
            'Apellido': enfermera.getApellido(),
            'User': enfermera.getUser(),
            'Contraseña' : enfermera.getContraseña(),
            'Fecha' : enfermera.getFecha(),
            'Teléfono' : enfermera.getTelefono(),
            'Género' : enfermera.getGenero()
        }
        Datos.append(objeto)  
    return(jsonify(Datos))
    

@app.route('/Enfermeras/<string:nombre>', methods=['GET'])
def ObtenerEnfermera(nombre): 
    global Enfermeras
    for enfermera in Enfermeras:
        if enfermera.getUser() == nombre:
            objeto = {
            'Nombre':enfermera.getNombre(),
            'Apellido': enfermera.getApellido(),
            'User': enfermera.getUser(),
            'Contraseña' : enfermera.getContraseña(),
            'Fecha' : enfermera.getFecha(),
            'Teléfono' : enfermera.getTelefono(),
            'Género' : enfermera.getGenero()
            }
            return(jsonify(objeto))      
    salida = { "Mensaje": "No existe el usuario con ese nombre"}
    return(jsonify(salida))


@app.route('/Enfermeras', methods=['POST'])
def AgregarEnfermera():
    global Enfermeras
    nombre = request.json['Nombre']
    apellido = request.json['Apellido']
    user = request.json['User']
    contraseña = request.json['Contraseña']
    fecha = request.json['Fecha']
    telefono = request.json['Teléfono']
    genero = request.json['Género']


    nuevo = Enfermera(nombre,apellido,user,contraseña,fecha,telefono,genero)
    Enfermeras.append(nuevo)
    return jsonify({'Mensaje':'Se añadió el usuario'})


@app.route('/Enfermeras/<string:nombre>', methods=['PUT'])
def ActualizarEnfermera(nombre):
    global Enfermeras

    for i in range(len(Enfermeras)):

        if nombre == Enfermeras[i].getUser():

            Enfermeras[i].setNombre(request.json['Nombre'])
            Enfermeras[i].setApellido(request.json['Apellido'])
            Enfermeras[i].setUser(request.json['User'])
            Enfermeras[i].setContraseña(request.json['Contraseña'])
            Enfermeras[i].setFecha(request.json['Fecha'])
            Enfermeras[i].setTelefono(request.json['Teléfono'])
            Enfermeras[i].setGenero(request.json['Género'])
            return jsonify({'Mensaje':'Se actualizo el dato exitosamente'})

    return jsonify({'Mensaje':'No se encontro el dato para actualizar'})



@app.route('/Enfermeras/<string:nombre>', methods=['DELETE'])
def EliminarEnfermera(nombre):
    global Enfermeras

    for i in range(len(Enfermeras)):

        if nombre == Enfermeras[i].getUser():

            del Enfermeras[i]
            
            return jsonify({'Mensaje':'Se elimino el dato exitosamente'})
       
    return jsonify({'Mensaje':'No se encontro el dato para eliminar'})


#METODOS PARA PACIENTES

@app.route('/Pacientes', methods=['GET'])
def getPacientes():
    global Pacientes
    Datos = []
    for paciente in Pacientes:
        objeto = {
            'Nombre': paciente.getNombre(),
            'Apellido': paciente.getApellido(),
            'User': paciente.getUser(),
            'Contraseña' : paciente.getContraseña(),
            'Fecha' : paciente.getFecha(),
            'Teléfono' : paciente.getTelefono(),
            'Género' : paciente.getGenero()
        }
        Datos.append(objeto)  
    return(jsonify(Datos))


@app.route('/Pacientes/<string:nombre>', methods=['GET'])
def ObtenerPaciente(nombre): 
    global Pacientes
    for paciente in Pacientes:
        if paciente.getUser() == nombre:
            objeto = {
            'Nombre': paciente.getNombre(),
            'Apellido': paciente.getApellido(),
            'User': paciente.getUser(),
            'Contraseña' : paciente.getContraseña(),
            'Fecha' : paciente.getFecha(),
            'Teléfono' : paciente.getTelefono(),
            'Género' : paciente.getGenero()
            }
            return(jsonify(objeto))      
    salida = { "Mensaje": "No existe el usuario con ese nombre"}
    return(jsonify(salida))


@app.route('/Pacientes', methods=['POST'])
def AgregarPaciente():
    global Pacientes
    compra=[]
    nombre = request.json['Nombre']
    apellido = request.json['Apellido']
    user = request.json['User']
    contraseña = request.json['Contraseña']
    fecha = request.json['Fecha']
    telefono = request.json['Teléfono']
    genero = request.json['Género']


    nuevo = Paciente(nombre,apellido,user,contraseña,fecha,telefono,genero,compra)  
    Pacientes.append(nuevo)
    mensaje={'Mensaje':'Se añadió el usuario'}
            

    
    return jsonify(mensaje)


@app.route('/Pacientes/<string:nombre>', methods=['PUT'])
def ActualizarPaciente(nombre):
    global Pacientes

    for i in range(len(Pacientes)):

        if nombre == Pacientes[i].getUser():

            Pacientes[i].setNombre(request.json['Nombre'])
            Pacientes[i].setApellido(request.json['Apellido'])
            Pacientes[i].setUser(request.json['User'])
            Pacientes[i].setContraseña(request.json['Contraseña'])
            Pacientes[i].setFecha(request.json['Fecha'])
            Pacientes[i].setTelefono(request.json['Teléfono'])
            Pacientes[i].setGenero(request.json['Género'])
            return jsonify({'Mensaje':'Se actualizo el dato exitosamente'})

    return jsonify({'Mensaje':'No se encontro el dato para actualizar'})



@app.route('/Pacientes/<string:nombre>', methods=['DELETE'])
def EliminarPaciente(nombre):
    global Pacientes

    for i in range(len(Pacientes)):

        if nombre == Pacientes[i].getUser():

            del Pacientes[i]
            
            return jsonify({'Mensaje':'Se elimino el dato exitosamente'})
       
    return jsonify({'Mensaje':'No se encontro el dato para eliminar'})


#METODOS PARA MEDICINA

@app.route('/Medicinas', methods=['GET'])
def getMedicinas():
    global Medicinas
    Datos = []
    for medicina in Medicinas:
        objeto = {
            'Nombre': medicina.getNombre(),
            'Precio': medicina.getPrecio(),
            'Descripción': medicina.getDescripicion(),
            'Cantidad' : medicina.getCantidad(),
            'Id':medicina.getIdmed()
        }
        Datos.append(objeto)  
    return(jsonify(Datos))


@app.route('/Medicinas', methods=['POST'])
def AgregarMedicina():
    global CantInicial
    global Medicinas
    global idMed
    nombre = request.json['Nombre']
    precio = float(request.json['Precio'])
    descripcion = request.json['Descripción']
    cantidad = request.json['Cantidad']

    nuevo = Medicina(nombre,precio,descripcion,cantidad,idMed,0)
    Medicinas.append(nuevo)
    CantInicial.append(cantidad)
    idMed+=1
    return jsonify({'Mensaje':'Se añadió el medicamento'})

@app.route('/Medicinas/<int:nombre>', methods=['GET'])
def ObtenerMedicina(nombre): 
    global Medicinas
    for medicina in Medicinas:
        if medicina.getIdmed() == nombre:
            objeto = {
            'Nombre': medicina.getNombre(),
            'Precio': medicina.getPrecio(),
            'Descripción': medicina.getDescripicion(),
            'Cantidad' : medicina.getCantidad()
            }
            return(jsonify(objeto))      
    salida = { "Mensaje": "No existe el usuario con ese nombre"}
    return(jsonify(salida))


@app.route('/Medicinas/<int:nombre>', methods=['PUT'])
def ActualizarMedicina(nombre):
    global Medicinas

    for i in range(len(Medicinas)):

        if nombre == Medicinas[i].getIdmed():

            Medicinas[i].setNombre(request.json['Nombre'])
            Medicinas[i].setPrecio(request.json['Precio'])
            Medicinas[i].setDescripcion(request.json['Descripción'])
            Medicinas[i].setCantidad(request.json['Cantidad'])
            
            return jsonify({'Mensaje':'Se actualizo el dato exitosamente'})

    return jsonify({'Mensaje':'No se encontro el dato para actualizar'})



@app.route('/Medicinas/<int:nombre>', methods=['DELETE'])
def EliminarMedicina(nombre):
    global Medicinas

    for i in range(len(Medicinas)):

        if nombre == Medicinas[i].getIdmed():

            del Medicinas[i]
            
            return jsonify({'Mensaje':'Se elimino el dato exitosamente'})
       
    return jsonify({'Mensaje':'No se encontro el dato para eliminar'})

#CITAS

@app.route('/Citas/<string:nombre>', methods=['GET'])
def getCitas(nombre):
    global Citas
    global idCitas
    global Doctores
    for cita in Citas:
        if cita.getIdPaciente() == nombre and (cita.getEstado()=='Pendiente' or cita.getEstado()=='Aceptada' or cita.getEstado()=='Rechazada'):

            auxDoc=cita.getIdDoctor()
            for doc in Doctores:
                if doc.getUser() == auxDoc:
                    auxDoc=doc.getNombre()+" "+doc.getApellido()

            objeto = {
                'Motivo': cita.getMotivo(),
                'Fecha': cita.getFecha(),
                'Hora': cita.getHora(),
                'Doctor':auxDoc,
                'Estado' : cita.getEstado(),
                'IdCita' : cita.getIdCita()
            }
            return(jsonify(objeto))      
    salida = { "Mensaje": "No existe el usuario con ese nombre"}
    return(jsonify(salida))

@app.route('/Citas', methods=['POST'])
def asignarCita():
    global Citas
    global idCitas
    global Pacientes
        
    paciente = request.json['Paciente']
    fecha = request.json['Fecha']
    hora = request.json['Hora']
    motivo = request.json['Motivo']
    doctor = "Pendiente"
    estado = "Pendiente"

    for aux in Pacientes:
        if aux.getUser== paciente:
            paciente=aux.getNombre+" "+aux.getApellido


    nuevo = Cita(paciente,fecha,hora,motivo,doctor,idCitas,estado)
    Citas.append(nuevo)
    idCitas+=1
    return jsonify({'Mensaje':'Se registró la cita'})

@app.route('/Citas', methods=['GET'])
def getCitasP():
    global Citas
    Datos = []
    for cita in Citas:
        objeto = {
            'Paciente': cita.getIdPaciente(),
            'Fecha': cita.getFecha(),
            'Hora': cita.getHora(),
            'Motivo' : cita.getMotivo(),
            'Doctor': cita.getIdDoctor(),
            'Id' : cita.getIdCita(),
            'Estado' : cita.getEstado()
        }
        Datos.append(objeto)  
    return(jsonify(Datos))

@app.route('/Cita/<int:idcita>', methods=['PUT'])
def AprobarCita(idcita):
    global Citas

    for i in range(len(Citas)):

        if idcita == Citas[i].getIdCita():

            Citas[i].setEstado(request.json['Estado'])
            Citas[i].setIdDoctor(request.json['IdDoctor'])
            
            return jsonify({'Mensaje':'Se agendo la cita exitosamente'})

    return jsonify({'Mensaje':'No se encontro el dato para actualizar'})

@app.route('/CitasA/<int:idcita>', methods=['PUT'])
def AprobarCitaD(idcita):
    global Citas

    for i in range(len(Citas)):

        if idcita == Citas[i].getIdCita():

            Citas[i].setEstado(request.json['Estado'])
            doctor = request.json['IdDoctor']
            Cita_atendida(doctor)

            return jsonify({'Mensaje':'Se agendo la cita exitosamente'})

    return jsonify({'Mensaje':'No se encontro el dato para actualizar'})

def Cita_atendida(IdDoctor):
    global Doctores

    for doctor in Doctores:
        if doctor.getUser == IdDoctor:
            doctor.setAtendidas(doctor.getAtendidas()+1)



@app.route('/CitasA', methods=['GET'])
def getCitasAprobadas():
    global Citas
    global idCitas
    global Doctores
    Datos=[]
    for cita in Citas:
        print("estoy en el for de citas")
        auxDoc=cita.getIdDoctor()
        for doc in Doctores:
           if doc.getUser() == auxDoc:
               auxDoc=doc.getNombre()+" "+doc.getApellido()
                

        objeto = {
            'Motivo': cita.getMotivo(),
            'Fecha': cita.getFecha(),
            'Hora': cita.getHora(),
            'Doctor':auxDoc,
            'Estado' : cita.getEstado()
            }
        Datos.append(objeto)
    return(jsonify(Datos))      

@app.route('/CitasA/<string:nombre>', methods=['GET'])
def getCitasPorDoc(nombre):
    global Citas
    global idCitas
    global Doctores
    Datos=[]
    for cita in Citas:
        if cita.getIdDoctor() == nombre:    
            objeto = {
                'Motivo': cita.getMotivo(),
                'Fecha': cita.getFecha(),
                'Hora': cita.getHora(),
                'Doctor': cita.getIdDoctor(),
                'Estado' : cita.getEstado(),
                'Id': cita.getIdCita()
            }
            Datos.append(objeto)
    return(jsonify(Datos))  


@app.route('/Cita/<int:idcita>', methods=['DELETE'])
def EliminarCita(idcita):
    global Citas

    for i in range(len(Citas)):

        if idcita == Citas[i].getIdCita():

           del Citas[i]
            
        return jsonify({'Mensaje':'Se eliminó la cita rechazada'})

    return jsonify({'Mensaje':'No se encontro el dato para actualizar'})    


#carrito
@app.route('/Carrito/<string:nombre>', methods=['GET'])
def getCompra(nombre):
    global Pacientes
    
    for paciente in Pacientes:
        if paciente.getUser() == nombre:
            carrito = paciente.getCarrito()

            obj = {
                'Nombre':paciente.getNombre()+" "+paciente.getApellido(),
                'Carrito': carrito
            }

            return(jsonify(obj))      
    salida = { "Mensaje": "No existe el usuario con ese nombre"}
    return(jsonify(salida))

@app.route('/Carrito/<int:ide>', methods=['GET'])
def AgregarAlCarrito(ide): 
    global Medicinas
    for medicina in Medicinas:
        if medicina.getIdmed() == ide:
            
            objeto = {
            'Nombre': medicina.getNombre(),
            'Descripción': medicina.getDescripicion(),
            'Precio': medicina.getPrecio(),
            'Cantidad' : 1,
            'Id': medicina.getIdmed()
            }
            return(jsonify(objeto))      
    salida = { "Mensaje": "No existe medicamento"}
    return(jsonify(salida))

@app.route('/Carrito/<string:nombre>', methods=['POST'])
def guardarCarrito(nombre):
    global Pacientes

    for i in range(len(Pacientes)):

        if nombre == Pacientes[i].getUser():

            Pacientes[i].getCarrito().append(request.json['Carrito'])
            print(Pacientes[i].getCarrito())
            return jsonify({'Mensaje':'Se actualizo el dato exitosamente'})

    return jsonify({'Mensaje':'No se encontro el dato para actualizar'})

@app.route('/Carrito/<int:nombre>', methods=['PUT'])
def ActualizarMedicinaMas(nombre):
    global Medicinas

    for i in range(len(Medicinas)):
        Ncantidad=0
        if nombre == Medicinas[i].getIdmed():
            cantidad = request.json['Cantidad']
            print(1+cantidad)
            cant=int(Medicinas[i].getCantidad())
            Ncantidad = float(cant+1)
            Medicinas[i].setCantidad(Ncantidad)
            
            return jsonify({'Mensaje':'Se actualizo el dato exitosamente'})

    return jsonify({'Mensaje':'No se encontro el dato para actualizar'})

@app.route('/Carritos/<int:nombre>', methods=['PUT'])
def ActualizarMedicinaMenos(nombre):
    global Medicinas

    for i in range(len(Medicinas)):
        Ncantidad=0
        if nombre == Medicinas[i].getIdmed():
            cantidad = request.json['Cantidad']
            print(1+cantidad)
            cant=int(Medicinas[i].getCantidad())
            print(cant)
            Ncantidad=float(cant-1)
            Medicinas[i].setCantidad(Ncantidad)
            
            return jsonify({'Mensaje':'Se actualizo el dato exitosamente'})

    return jsonify({'Mensaje':'No se encontro el dato para actualizar'})

#ADMIN
@app.route('/Admin', methods=['GET'])
def ObtenerAdmin(): 
    global Admin
    objeto = {
            'Nombre': Admin.getNombre(),
            'Apellido': Admin.getApellido(),
            'User': Admin.getUser(),
            'Contraseña' : Admin.getContraseña()
            }
    return(jsonify(objeto))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
