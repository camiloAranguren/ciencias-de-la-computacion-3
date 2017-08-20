class Nodo():
    def __init__(self,valor,izq=None,der=None):
        self.valor = valor
        self.izq = izq
        self.der = der

class Pila:
    def __init__(self):
        self.pila=[]        
    def apilar(self,x):
      # funcion para agregar un elemento a la pila
        self.pila.append(x)
      # print "se apilo correctmente"
    def desapilar(self):
      # funcion para eliminar un elemento de la pila
       if (self.pila != []):
      # print "se desapilo"
        return self.pila.pop()
       else: 
        return "Lista vacia"
    

def evaluar(arbol):
    try:
      if(arbol.valor == '+'):
         return (evaluar(arbol.izq) + evaluar(arbol.der))
      if(arbol.valor == '-'):
         return (evaluar(arbol.izq) - evaluar(arbol.der))
      if(arbol.valor == '*'):
         return (evaluar(arbol.izq) * evaluar(arbol.der))
      if(arbol.valor == '/'):
         return (evaluar(arbol.izq) / evaluar(arbol.der))   
      return int(arbol.valor)
    except AttributeError:
      return int(arbol)
        
cadena = raw_input("Ingrese una cadena:")
lista = cadena.split(" ")
pila= Pila()
tam = len(lista)
i = 0
while(i < tam):
    if(lista[i] in "+ - * /"):
       der = pila.desapilar()
       izq = pila.desapilar()
       nodo = Nodo(lista[i],izq,der) 
       pila.apilar(nodo)
    else:        
        pila.apilar(lista[i])
    i = i+1
    
print "el resultado al evaluar el arbol es: " + str(evaluar(pila.desapilar()))
    




