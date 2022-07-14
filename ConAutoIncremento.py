import sqlite3

def crear_tabla():
	c.execute("CREATE TABLE IF NOT EXISTS Alumnos(ID INTEGER PRIMARY KEY AUTOINCREMENT, Nombre TEXT, Apellido TEXT)")

	
def incluir_datos():
        datos= [('Rita','Morales'),
                ('Alonso','Alamo'),
                ('Adolfo','Ramos'),
                ('Zaida','Linares'),
                ('Rosa','Sarmiento'),
                ('Amanda','Ramirez'),
                ('Susana','Azul'),
                ('Brandon','Rosales')]
        c.executemany('INSERT INTO Alumnos VALUES(NULL,?,?)', datos)
        
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
