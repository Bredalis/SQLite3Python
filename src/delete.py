
from crud import Crud

crud = Crud("../data/database.db", "report")

crud.delete("name", "")
crud.close_database()
