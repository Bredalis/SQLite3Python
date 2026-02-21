
from CRUD import CRUD

# Crear instancia de CRUD para borrar registros de la tabla
borrar = CRUD("BBDD.db", "Informe")

# Borrar registros donde el campo 'Nombre' sea 'Lucia'
borrar.borrar("Nombre", "Lucia")
borrar.cerrar_bbdd()