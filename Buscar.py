
# Pragrama que busca 
# y muestra valores

from CRUD import *

buscar = CRUD("BBDD.db", "Informe")
buscar.buscar("Nombre", "Lucas")
buscar.ejecucion()
buscar.mostrar_datos()
buscar.cerrar_bbdd()