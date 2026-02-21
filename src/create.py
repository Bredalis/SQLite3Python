
# Programa para crear una base de datos

from CRUD import CRUD

# Crear instancia de CRUD y configurar la base de datos y tabla
crear_bbdd = CRUD("BBDD.db", "Informe", "Nombre", "Apellido", "Fecha_Nacimiento")
crear_bbdd.crear_tabla()
crear_bbdd.cerrar_bbdd() # Cerrar la conexión de la bbdd