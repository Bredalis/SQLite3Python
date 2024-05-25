
# Programa que crea BBDD

from CRUD import *

crear_bbdd = CRUD("BBDD.db", "Informe", "Nombre", "Apellido", "Edad")
crear_bbdd.crear_tabla()
crear_bbdd.ejecucion()
crear_bbdd.guardar_cambios()
crear_bbdd.cerrar_bbdd()