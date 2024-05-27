
# Actualiza valores de las columnas 
# de la tabla

from CRUD import *

actualizar = CRUD("BBDD.db", "Informe")
actualizar.actualizar("Nombre", "Lucas", "ID", "4")
actualizar.ejecucion()
actualizar.guardar_cambios()
actualizar.cerrar_bbdd()