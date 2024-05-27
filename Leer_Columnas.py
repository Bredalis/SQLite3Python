
from CRUD import *

leer_columnas = CRUD("BBDD.db", "Informe")
leer_columnas.leer_columnas()
leer_columnas.ejecucion()
leer_columnas.mostrar_datos()
leer_columnas.cerrar_bbdd()