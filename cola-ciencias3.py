import random

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
        self.beneficiados=[]
    def encolar(self, x):
        # funcion para agregar un elemento a la cola
        self.moto.append(x)
    def desencolar(self):
        # funcion para eliminar un elemento de la cola
        if (self.moto != []):
        #  print "elimino correctamente de la cola principal"
          return self.moto.pop(0)
        else:
          return "Cola vacia"
    def atender(self,cupos):
 # funcion que segiun el numero de cupos atendera a esa antidad de motos
        i = 0
        print "el random dio " + str(cupos) + " cupos para motos"
        while ( i != cupos):
           self.beneficiados.append(self.moto[0])
           cola.desencolar()
           i = i + 1
        if ( i == cupos):
            print "las motos atendidas fueron"
            for s in self.beneficiados:
                print s


moto = Moto()
cola = Cola()

cola.encolar(moto.a)
cola.encolar(moto.b)
cola.encolar(moto.c)
cola.encolar(moto.d)
cola.encolar(moto.e)
cola.encolar(moto.f)
cola.encolar(moto.g)

cola.atender(random.randrange(len(cola.moto))) 
