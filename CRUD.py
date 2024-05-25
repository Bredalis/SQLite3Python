
import sqlite3 as sqlite

class CRUD:

	def __init__(self, bbdd, tabla, columna_1 = "", columna_2 = "", columna_3 = ""):

		self.bbdd = sqlite.connect(bbdd)
		self.cursor = self.bbdd.cursor()
		self.tabla = tabla
		self.columna_1 = columna_1
		self.columna_2 = columna_2
		self.columna_3 = columna_3

	def crear_tabla(self):
		self.instruccion = f"CREATE TABLE IF NOT EXISTS {self.tabla} ('ID' INTEGER PRIMARY KEY, '{self.columna_1}' TEXT, '{self.columna_2}' TEXT, '{self.columna_3}' INTEGER)"

	def insertar_datos(self, ID):
		self.instruccion = f"INSERT INTO {self.tabla} VALUES('{ID}', '{self.columna_1}', '{self.columna_2}', {self.columna_3})"

	def leer_columnas(self):
		self.instruccion = f"SELECT * FROM {self.tabla}"

	def leer_orden(self, campo):
		self.instruccion = f"SELECT * FROM {self.tabla} ORDER BY {campo}"

	def buscar(self, columna, valor):
		self.instruccion = f"SELECT * FROM {self.tabla} WHERE {columna} = '{valor}'"

	def actualizar(self, columna, valor_1, ubicacion, valor_2):
		self.instruccion = f"UPDATE {self.tabla} SET {columna} = '{valor_1}' WHERE {ubicacion} = '{valor_2}'"

	def borrar(self, columna, valor):
		self.instruccion = f"DELETE FROM {self.tabla} WHERE {columna} = '{valor}'"
		
	def ejecucion(self):
		self.cursor.execute(self.instruccion)

	def mostrar_datos(self):
		
		self.cursor.execute(self.instruccion)
		self.datos = self.cursor.fetchall()

		print(self.datos)

	def guardar_cambios(self):
		self.bbdd.commit()
		
	def cerrar_bbdd(self):
		self.bbdd.close()