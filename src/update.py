
from crud import Crud

crud = Crud("../data/database.db", "report")

crud.update("name", "Lucas", "id", "1")
crud.close_database()
