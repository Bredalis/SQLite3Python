
# Programa que muestra los
# datos de las columnas en orden

from CRUD import *

leer_orden = CRUD("BBDD.db", "Informe")
leer_orden.leer_orden("Nombre")
leer_orden.ejecucion()
leer_orden.mostrar_datos()
leer_orden.cerrar_bbdd()