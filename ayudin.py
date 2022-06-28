class Usuario:
    def __init__(self, nombre, permiso) -> None:
        self.nombre = nombre
        self.permiso = permiso


nombreUsuario = input("Ingrese el nombre del usuario")
permisoUsuario = input("Ingrese el nivel de Permiso")

nuevoUsuario = Usuario(nombreUsuario, permisoUsuario)

if nuevoUsuario.permiso == "3":
    print("3: Agregar Vehiculo")

    # motos = []

# biciletas = []

# def baseAutos(cars):
#     for car in cars:
#         if car != 'Falcon':
#             return car

# def baseMotos(motos):
#     for i in motos():
#         print(i)
#from colectivo import Colectivo, colectivo

#CREAR UN COLECTIVO
opc = input("Elija el número de la opcion que desea realizar: \n 1.agregar un vehiculo:")
print(opc)
if opc == '1':
    crearColectivo()
    crearColectivo()
else:
    print("no se creo nada")


print(colectivo[0].mostrar())
#colectivo[0].cambiarKM(2342342)
#print(colectivo[0].mostrar())
    def __str__(self):
        print("marca", self.var1)
        print("estado=", end=" ")
        return self.estado

            def __str__(self) -> str:
        return (self.marca , 
        self.color , 
        self.motor , 
        self.precio ,
        self.pasajeros ,
        self.km ,
        self.estado )

def bondiVision():
    print("COLECTIVOS EN EL CONCECIONARIO:""\n""marca  ","color  ","motor  ","precio  ")
    for bondi in bondis["marca"]:
        indexBondi = bondis["marca"].index(bondi)
        print(bondis["marca"][indexBondi], "  ", bondis["color"][indexBondi], "  ", bondis["motor"][indexBondi], "  ", bondis["precio"][indexBondi])



def autoVision(usuariologeado):
    if usuariologeado ["permiso"] == "Admin":
        print("marca  ","color  ","motor  ","precio  ")
        for auto in autos["marca"]:
            indexauto = autos["marca"].index(auto)
            print(autos["marca"][indexauto], "  ", autos["color"][indexauto], "  ", autos["motor"][indexauto], "  ", autos["precio"][indexauto])
    else:
        print("marca  ","color  ","motor  ")
        for auto in autos["marca"]:
            indexauto = autos["marca"].index(auto)
            print(autos["marca"][indexauto], "  ", autos["color"][indexauto], " ", autos["motor"][indexauto])

