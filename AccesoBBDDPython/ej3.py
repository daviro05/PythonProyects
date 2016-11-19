#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
db_file = "Libreria.sqlite3"

def connect_db():
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    return conn, cur

def select_1(cur):
    print "1- Obtener los países y el número de libros vendidos agrupados por país y ordenados de manera descendente respecto al total de ventas.\n"
    cur.execute('''SELECT pais, COUNT(pais) AS cuenta 
                   FROM (Libros LEFT JOIN Compras ON Libros.registro=Compras.id_libro) 
                   WHERE Compras.registro IS NOT NULL GROUP BY pais ORDER BY cuenta DESC;
                ''')
    print "Pais".ljust(10, " ") + "Libros vendidos"
    print "-------------------------"
    for rec in cur.fetchall():
        print rec[0].ljust(15, " ") + str(rec[1])
    print

def select_2(conn, cur):
    print "2- Obtener la media de los importes gastados por los compradores, agrupados por población y ordenados decrecientemente por el importe medio.\n"
    
    cur.execute(''' SELECT poblacion, AVG(media) 
                    FROM (SELECT nombre, AVG(importe) AS media, poblacion 
                        FROM Libros INNER JOIN Compras ON Libros.registro=Compras.id_libro 
                                    INNER JOIN Compradores ON Compradores.registro=Compras.id_comprador 
                        GROUP BY Compradores.nombre) 
                    GROUP BY poblacion ORDER BY media DESC;
                ''')
    print "Poblacion".ljust(14, " ") + "Media"
    print "--------------------"
    for rec in cur.fetchall():
        print rec[0].ljust(14, " ") + str(rec[1])
    print

def select_3(conn, cur):
    print "3- Actualizar la tabla Compras, cambiando los registros 10 y 11 de forma que las filas tengan los valores(3,3) y (3,7) respectivamente.\n"
    cur.execute("UPDATE Compras SET id_comprador=3, id_libro=3 WHERE registro=10")
    cur.execute("UPDATE Compras SET id_comprador=3, id_libro=7 WHERE registro=11")
    conn.commit() 

    cur.execute("SELECT * FROM Compras WHERE registro=10 OR registro=11")
    print "Registro".ljust(10, " ") + "Id_comprador".ljust(14, " ") + "Id_libro"
    print "--------------------------------"
    for rec in cur.fetchall():
        print str(rec[0]).ljust(10, " ") + str(rec[1]).ljust(14, " ") + str(rec[2]) 
    print

def select_4(conn, cur):
    print "4- Obtener la media del precio de los libros agrupadas por soporte.\n"

    cur.execute("SELECT soporte, AVG(importe) AS media FROM Libros GROUP BY soporte;")
    print "Soporte".ljust(10, " ") + "Media"
    print "----------------"
    for rec in cur.fetchall():
        print str(rec[0]).ljust(10, " ") + str(rec[1])
    print

def select_5(conn, cur):
    print "5- Borrar los compradores que no han comprado nunca ningún libro.\n"
    cur.execute('''DELETE FROM Compradores WHERE registro IN 
                    (SELECT c.registro FROM Compradores c 
                    LEFT OUTER JOIN Compras co 
                    ON co.id_comprador=c.registro 
                    WHERE co.id_comprador IS NULL);
                ''')
    conn.commit()
    cur.execute("SELECT * FROM Compradores")
    print "Registro".ljust(12, " ") + "Nombre"
    print "-------------------------------"
    for rec in cur.fetchall():
        print str(rec[0]).ljust(12, " ") + rec[1] 
    print
    
if __name__ == "__main__":
    conn, cur = connect_db()
    
    select_1(cur)
    select_2(conn, cur)
    select_3(conn, cur)
    select_4(conn, cur)
    select_5(conn, cur)

    cur.close()
    conn.close()
