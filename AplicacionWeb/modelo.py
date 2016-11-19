import sqlite3

db = sqlite3.connect('peliculas.sqlite3')
db.execute("DROP TABLE IF EXISTS peliculas")
db.execute("DROP TABLE IF EXISTS usuarios")
db.execute("CREATE TABLE peliculas ( id INTEGER PRIMARY KEY, titulo CHAR(100) NOT NULL, duracion REAL NOT NULL )")
db.execute("CREATE TABLE usuarios (id INTEGER PRIMARY KEY, username CHAR(100) NOT NULL, password CHAR(100) NOT NULL, nombre CHAR(100), apellidos CHAR(100), email CHAR(100) NOT NULL)")

db.execute("INSERT INTO usuarios (username, password, nombre, apellidos, email) VALUES ('hector', '1234', 'Hector', 'Perez Fernandez', 'hector@hotmail.com')")

db.execute("INSERT INTO peliculas (titulo,duracion) VALUES ('Titanic', 3.2)")
db.execute("INSERT INTO peliculas (titulo,duracion) VALUES ('Returned', 2.4)")
db.execute("INSERT INTO peliculas (titulo,duracion) VALUES ('Avatar', 1.5)")
db.execute("INSERT INTO peliculas (titulo,duracion) VALUES ('El padrino', 1.8)")
db.execute("INSERT INTO peliculas (titulo,duracion) VALUES ('Batman', 2.1)")
db.execute("INSERT INTO peliculas (titulo,duracion) VALUES ('Yo Robot', 2.55)")

db.commit()
