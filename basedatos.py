import sqlite3

def crear_tabla():
	c.execute("CREATE TABLE IF NOT EXISTS Alumnos(id INTEGER Primary Key, Nombre TEXT, Apellido TEXT)")

	
def incluir_datos():
	c.execute("INSERT INTO Alumnos VALUES (1, 'José', 'Hernandez')")
	c.execute("INSERT INTO Alumnos VALUES (2, 'Josefina', 'Hernandez')")
	c.execute("INSERT INTO Alumnos VALUES (3, 'Mario', 'Morales')")
	c.execute("INSERT INTO Alumnos VALUES (4, 'Adolfo', 'Pereira')")
	c.execute("INSERT INTO Alumnos VALUES (5, 'Mariana', 'Chaparro')")
	c.execute("INSERT INTO Alumnos VALUES (6, 'Ana', 'Rondón')")
	c.execute("INSERT INTO Alumnos VALUES (7, 'Julia', 'Ramirez')")
	c.execute("INSERT INTO Alumnos VALUES (8, 'Rita', 'Lomas')")
	
	

def consulta():
	rows=c.execute("SELECT * FROM Alumnos WHERE Nombre ='Adolfo'")
	for row in rows: 
		print(row)

conn = sqlite3.connect('baseDatos.db')
c = conn.cursor()

crear_tabla()
incluir_datos()
consulta() 

conn.commit()
c.close()
