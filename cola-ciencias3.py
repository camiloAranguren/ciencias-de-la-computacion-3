class Moto:
  def __init__(self):
#  datos de la moto (placa, dueño)
   self.a = ["ABCD12","Juan Perez"]
   self.b = ["AGHTR3","Maria Gomez"]
   self.c = ["GDHY15","Pedro Moreno"]
   self.d = ["KLSTE4","Jhon Quiroga"]
   self.e = ["KHFD77","Camilo Jimenez"]
   self.f = ["LF3FD5","David Toro"]
   self.g = ["XK08T4","Laura Ramirez"]

class Cola:
    def __init__(self):
        # # secrean dos listas vacias para encolar las motos
        self.moto=[]
        #self.beneficiados=[]
    def encolar(self, x):
        # funcion para agregar un elemento a la cola
        self.moto.append(x)
    def desencolar(self):
        # funcion para eliminar un elemento de la cola
        if (self.moto != []):
        #  print "elimino correctamente de la cola principal"
        else:
          return "Cola vacia"
    def atender(self,cupos):
        # funcion que segun el numero de cupos atendera a esa cantidad de motos
        i = 0
        print ("El cupo para motos es de:  " + cupos)        
        while ( i <= int(cupos)):
            if ( i == int(cupos)):
                print ("Los cupos fueron atendidos")                
            else:
                aux = cola.desencolar() #Se retira de una cola y se guarda como aux
                beneficiados.encolar(aux)#Se guarda en otra cola de beneficiados
                print(aux)  #Muestra los datos del beneficiado
                print("Beneficiado")
            i = i + 1
       
moto = Moto()
cola = Cola()
beneficiados= Cola()

cola.encolar(moto.a)
cola.encolar(moto.b)
cola.encolar(moto.c)
cola.encolar(moto.d)
cola.encolar(moto.e)
cola.encolar(moto.f)
cola.encolar(moto.g)

parqueaderos = input ("Introduzca la cantidad de parqueaderos: ")
cola.atender(parqueaderos)
