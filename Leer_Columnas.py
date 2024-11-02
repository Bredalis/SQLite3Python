
from CRUD import CRUD

# Crear instancia de CRUD
leer_columnas = CRUD("BBDD.db", "Informe")
leer_columnas.leer_columnas() # Leer y mostras las columnas de la tabla
leer_columnas.cerrar_bbdd() # Cerrar la conexión de la bbdd