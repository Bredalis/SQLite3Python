
from crud import Crud

crud = Crud("../data/database.db", "report")

crud.search("name", "Lucas")
crud.close_database()
