#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
from datetime import date
db_file = "Libreria.sqlite3"

def connect_db():
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    return conn, cur

def insert_data_compradores(conn, cur):
    cur.execute('''INSERT INTO Compradores 
                (registro, nombre, fecha_nacim, telefono, domicilio, poblacion, anotaciones) 
                VALUES (?,?,?,?,?,?,?)''',
                (1, "Juan Miedo", date(1995,10,23), "608900890", "La isla del tesoro,33", 
                "Getafe", "Buen comprador"))
    cur.execute('''INSERT INTO Compradores 
                (registro, nombre, fecha_nacim, telefono, domicilio, poblacion)
                VALUES (?,?,?,?,?,?)''', 
                (2, "Pepe Pepino", date(1961,12,13), "607899005", "Plaza mayor,56", "Pozuelo"))
    cur.execute('''INSERT INTO Compradores 
                (registro, nombre, fecha_nacim, telefono, domicilio, poblacion)
                VALUES (?,?,?,?,?,?)''', 
                (3, "Pepe Mur", date(1976,04,02), "917895679", "Esparteros,5","Getafe"))
    cur.execute('''INSERT INTO Compradores 
                (registro, nombre, fecha_nacim, telefono, domicilio, poblacion, anotaciones)
                VALUES (?,?,?,?,?,?,?)''', 
                (4, u"Mohamed Alí", date(1968,11,12), "609440567", "Juan sin miedo,4", 
                "Pozuelo", u"Le gusta la ciencia ficción"))
    cur.execute('''INSERT INTO Compradores 
                (registro, nombre, fecha_nacim, telefono, domicilio, poblacion, anotaciones)
                VALUES (?,?,?,?,?,?,?)''', 
                (5, "Alfredo Mesa", date(1986,8,17), "690890456", u"Gran vía,56", 
                "Getafe", "Le gustan los ensayos"))
    cur.execute('''INSERT INTO Compradores 
                (registro, nombre, fecha_nacim, telefono, domicilio, poblacion, anotaciones)
                VALUES (?,?,?,?,?,?,?)''', 
                (6, "Pedro Reyes", date(1957,8,25), "917890056", u"Plaza de España,34", "Pozuelo", "Le gusta la historia"))
    cur.execute('''INSERT INTO Compradores 
                (registro, nombre, fecha_nacim, telefono, domicilio, poblacion, anotaciones)
                VALUES (?,?,?,?,?,?,?)''', 
                (7, "Isabel Olvido", date(1977,07,20), "915678900", "Principal,3", 
                "Getafe", "Le gusta la novela de terror"))
    cur.execute('''INSERT INTO Compradores 
                (registro, nombre, fecha_nacim, telefono, domicilio, poblacion)
                VALUES (?,?,?,?,?,?)''', 
                (8, "Mariano Calcetines", date(1996,11,9), "634567876", u"Aviación,34", "Getafe"))
    cur.execute('''INSERT INTO Compradores 
                (registro, nombre, fecha_nacim, telefono, domicilio, poblacion)
                VALUES (?,?,?,?,?,?)''', 
                (9, u"María Calero", date(1984,11,8), "645666900", u"Río Ebro,4", "Getafe"))

    conn.commit()

def insert_data_libros(conn, cur):
    cur.execute('''INSERT INTO Libros 
                (registro, titulo, escritor, editorial, fecha_entrada, pais, importe)
                VALUES (?,?,?,?,?,?,?)''',
                (1, "El Quijote", "Miguel de Cervantes", "Alianza", date(1988,06,11), u"España", 12))
    cur.execute('''INSERT INTO Libros 
                (registro, titulo, escritor, editorial, soporte, fecha_entrada, pais, importe)
                VALUES (?,?,?,?,?,?,?,?)''',
                (2, "Marina", u"Carlos Ruíz Zafón", u"Edebé", "CD", date(2003,05,10), u"España", 18.95))
    cur.execute('''INSERT INTO Libros 
                (registro, titulo, escritor, editorial, soporte, fecha_entrada, pais, importe)
                VALUES (?,?,?,?,?,?,?,?)''',
                (3, "La hoguera de la vanidadaes", "Tom Wolfe", "RBA editores", "DVD", date(2005,11,9), 
                "USA", 22.25))
    cur.execute('''INSERT INTO Libros 
                (registro, titulo, escritor, editorial, fecha_entrada, pais, importe)
                VALUES (?,?,?,?,?,?,?)''',
                (4, "Los pilares de la Tierra", "Ken Follet", "Faber", date(2014,12,01), "USA", 12.95)) 
    cur.execute('''INSERT INTO Libros 
                (registro, titulo, escritor, editorial, fecha_entrada, pais, importe) 
                VALUES (?,?,?,?,?,?,?)''', 
                (5, "Otelo", "William Shakespeare", "Anaya", date(2013,04,11), "Inglaterra", 14.95))
    cur.execute('''INSERT INTO Libros 
                (registro, titulo, escritor, editorial, fecha_entrada, pais, importe)
                VALUES (?,?,?,?,?,?,?)''',
                (6, "Rimas y Leyendas", "Gustavo Adolfo Becquer", "Roca", date(2008,01,8), u"España", 
                25.95))
    cur.execute('''INSERT INTO Libros 
                (registro, titulo, escritor, editorial, fecha_entrada, pais, importe)
                VALUES (?,?,?,?,?,?,?)''',
                (7, u"Poesía", u"Juan Ramón Jimenez", "P&J", date(2002,04,07), u"España", 10.95))
    
    conn.commit()

def insert_data_compras(conn, cur):
    cur.execute("INSERT INTO Compras (registro, id_comprador, id_libro) VALUES(?,?,?)", (1,9,7))
    cur.execute("INSERT INTO Compras (registro, id_comprador, id_libro) VALUES(?,?,?)", (2,9,3))
    cur.execute("INSERT INTO Compras (registro, id_comprador, id_libro) VALUES(?,?,?)", (3,8,2))
    cur.execute("INSERT INTO Compras (registro, id_comprador, id_libro) VALUES(?,?,?)", (4,7,1))
    cur.execute("INSERT INTO Compras (registro, id_comprador, id_libro) VALUES(?,?,?)", (5,8,1))
    cur.execute("INSERT INTO Compras (registro, id_comprador, id_libro) VALUES(?,?,?)", (6,1,1))
    cur.execute("INSERT INTO Compras (registro, id_comprador, id_libro) VALUES(?,?,?)", (7,7,1))
    cur.execute("INSERT INTO Compras (registro, id_comprador, id_libro) VALUES(?,?,?)", (8,6,2))
    cur.execute("INSERT INTO Compras (registro, id_comprador, id_libro) VALUES(?,?,?)", (9,3,5))
    cur.execute("INSERT INTO Compras (registro, id_comprador, id_libro) VALUES(?,?,?)", (10,3,1))
    cur.execute("INSERT INTO Compras (registro, id_comprador, id_libro) VALUES(?,?,?)", (11,3,2))
    conn.commit()

if __name__ == "__main__":
    conn, cur = connect_db()
    insert_data_compradores(conn, cur)
    insert_data_libros(conn, cur)
    insert_data_compras(conn, cur)

    cur.close()
    conn.close()
