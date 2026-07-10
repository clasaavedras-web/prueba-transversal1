# transporte = []

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
         

