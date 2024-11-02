
from CRUD import CRUD

# Crear una instancia para leer las columna de la tabla
leer_orden = CRUD("BBDD.db", "Informe")

# Leer y mostrar datos ordenados por la columna 'Nombre'
leer_orden.leer_orden("Nombre") 
leer_orden.cerrar_bbdd()