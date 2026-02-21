
from crud import Crud

crud = Crud("../data/database.db", "report")

crud.read_all()
crud.close_database()
