
from CRUD import CRUD

# Insertar un nuevo registro en la base de datos - Fecha en formato (d-m-yyyy)
insertar = CRUD("BBDD.db", "Informe", "Lucia", "Mendoza", "15-9-1998")
print(insertar.insertar_datos(1)) # Insertar el valor del 'ID'
insertar.cerrar_bbdd()