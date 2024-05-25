
# Programa que inserta 
# nuevos datos a las 
# columnas de la tabla

from CRUD import *

insertar = CRUD("BBDD.db", "Informe", "Lucia", "Mendoza", 15)
insertar.insertar_datos("1")
insertar.ejecucion()
insertar.guardar_cambios()
insertar.cerrar_bbdd()