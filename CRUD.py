
import sqlite3 as sqlite
import pandas as pd
import time

class CRUD:
    def __init__(self, bbdd, tabla, columna_1 = "", columna_2 = "", columna_3 = ""):
        self.bbdd = sqlite.connect(bbdd)
        self.cursor = self.bbdd.cursor()
        self.tabla = tabla
        self.columna_1 = columna_1
        self.columna_2 = columna_2
        self.columna_3 = columna_3

    def crear_tabla(self):
        self.instruccion = f"""
            CREATE TABLE IF NOT EXISTS {self.tabla} (
                ID INTEGER PRIMARY KEY,
                {self.columna_1} TEXT,
                {self.columna_2} DATE,
                {self.columna_3} INTEGER
            )
        """
        self.ejecucion()

    def validar_fecha(self, fecha):
        try:
            dia, mes, anio = map(int, fecha.split("-"))
            if 1920 <= anio <= int(time.strftime("%Y")) and 1 <= mes <= 12 and 1 <= dia <= 31:
                return "Fecha válida"
            else:
                return "Fecha no válida"
        except ValueError:
            return "Formato incorrecto de la fecha"

    def insertar_datos(self, ID):
        if self.validar_fecha(self.columna_3) != "Fecha válida":
            return "No se insertarón los datos"

        self.instruccion = f"""
    		INSERT INTO {self.tabla} 
    		VALUES(
    		{ID}, 
    		'{self.columna_1}', 
    		'{self.columna_2}', 
    		'{self.columna_3}'
    	)
    	"""
        self.ejecucion()

    def leer_columnas(self):
        self.instruccion = f"SELECT * FROM {self.tabla}"
        self.mostrar_datos()

    def leer_orden(self, campo):
        self.instruccion = f"SELECT * FROM {self.tabla} ORDER BY {campo}"
        self.mostrar_datos()

    def buscar(self, columna, valor):
        self.instruccion = f"SELECT * FROM {self.tabla} WHERE {columna} = '{valor}'"
        self.mostrar_datos()

    def actualizar(self, columna, valor_1, ubicacion, valor_2):
        self.instruccion = f"UPDATE {self.tabla} SET {columna} = '{valor_1}' WHERE {ubicacion} = '{valor_2}'"
        self.ejecucion()

    def borrar(self, columna, valor):
        self.instruccion = f"DELETE FROM {self.tabla} WHERE {columna} = '{valor}'"
        self.ejecucion()

    def ejecucion(self):
        try:
            self.cursor.execute(self.instruccion)
            self.guardar_cambios()

        except Exception as e:
            print(f"Error: {e}")

    def mostrar_datos(self):
        self.cursor.execute(self.instruccion)
        datos = self.cursor.fetchall()
        df = pd.DataFrame(
            datos, columns = ["ID", "Nombre", "Apellido", "Fecha_Nacimiento"]
        )
        
        print(df)

    def guardar_cambios(self):
        self.bbdd.commit()

    def cerrar_bbdd(self):
        self.bbdd.close()