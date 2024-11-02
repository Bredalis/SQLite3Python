
from CRUD import CRUD

# Crear instancia de CRUD para buscar registros en la tabla
buscar = CRUD("BBDD.db", "Informe")

# Buscar registros donde el campo 'Nombre' sea 'Lucas' 
buscar.buscar("Nombre", "Lucas")
buscar.cerrar_bbdd()