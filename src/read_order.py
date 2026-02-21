
from crud import Crud

crud = Crud("../data/database.db", "report")

crud.read_ordered("name")
crud.close_database()
