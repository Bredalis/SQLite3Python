
from crud import Crud

crud = Crud("../data/database.db", "report")

crud.insert_data(1, "Perla", "Mendoza", "15-9-1998")
crud.close_database()
