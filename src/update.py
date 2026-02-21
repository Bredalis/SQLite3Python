
# Actualización de valores en las columnas de la tabla

from CRUD import CRUD

# Crear instancia de CRUD para actualizar registros de la tabla
actualizar = CRUD("BBDD.db", "Informe")

# Actualizar el campo 'Nombre' a 'Lucas' donde 'ID' sea '4'
actualizar.actualizar("Nombre", "Lucas", "ID", "4")
actualizar.cerrar_bbdd()