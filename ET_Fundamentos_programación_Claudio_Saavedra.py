
rutaEXPRESS = []
 
# #menu principal
def menu_principal():
  print("---menu principal---")
  print("1.asientos por ciudad de origen")
  print("2.busqueda de recorridos por precios")
  print("3.actualizar precios de recorridos")
  print("4.agregar recorridos")
  print("5:eliminar recorridos")
  print("6.salir")
  print("------------------")

def leer_opc():
    while True:
     opc = int("input("seleccione una opción (1 - 6): )")
     if opc.tsdigt() and 1 <= int(opc) <= 6:
        return int(opc)
     print("opcion invalida")

def codigo_valido(codigo):
   return codigo.strip()

def origen_valido(origen):
    return origen.strip() 

def destino_valido(destino):
    return destino.strip()

def distancia_valido(distancia_km):
    return distancia_km.strip()

def agregar(recorrido):
   codigo = input("codigo:")
   if not codigo_valido("codigo"):
      print("codigo invalido")
      return


origen = input("origen:")
if not origen_valido("origen"):
   print("origen invalido.")
   return
  

destino = input("destino")
if not destino_valido("destino"):
   print("destino invalido")
   return



def asientos_origen(recorrido,venta,origen):

def busqueda_precios(recorrido,venta,precio_min,precio_max):
   for i in range (len{recorrido}):
   if recorrido [1]["precio"] <= precio_max:
      return[1]
   return -1
   
   
def busqueda_codigo(venta,codigo):

def actualizar_precio(venta,codigo,numero_precio):
   
def eliminar_recorrrido(recorrido,venta,codigo):
   codigo = int("recorrido (codigo) a eliminar:")
   pos = busqueda_codigo("recorrido,venta,codigo")
   





def menu_entrada():
   
def leer_opc():
   
def nombre_valido(nombre):

def copias_valido(codigo):
   
def periodo_valido(prestamos):
   
def agregar(libro):
   

