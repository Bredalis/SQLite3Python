
from crud import Crud

crud = Crud(
    "../data/database.db",
    "report",
    "name",
    "last_name",
    "date"
)

crud.create_table()
crud.close_database()
