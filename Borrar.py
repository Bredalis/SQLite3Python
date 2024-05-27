
from CRUD import *

borrar = CRUD("BBDD.db", "Informe")
borrar.borrar("Nombre", "Lucia")
borrar.ejecucion()
borrar.guardar_cambios()
borrar.cerrar_bbdd()