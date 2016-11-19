#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3

db_file = "Libreria.sqlite3"

def connect_db():
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    return conn, cur

def create_db(cur):
    cur.execute("DROP TABLE IF EXISTS Compradores")
    cur.execute('''CREATE TABLE Compradores
                ( registro INT(4) PRIMARY KEY NOT NULL UNIQUE,
                  nombre VARCHAR(35) NOT NULL DEFAULT ' ' UNIQUE,
                  fecha_nacim DATE NOT NULL DEFAULT '0000-00-00',
                  telefono VARCHAR(10) DEFAULT NULL,
                  domicilio VARCHAR(35) DEFAULT NULL,
                  poblacion VARCHAR(25) DEFAULT NULL,
                  anotaciones TEXT
                )''')

    cur.execute("DROP TABLE IF EXISTS Libros")
    cur.execute('''CREATE TABLE Libros
                ( registro INT(4) PRIMARY KEY NOT NULL UNIQUE,
                  titulo VARCHAR(35) NOT NULL DEFAULT ' ' UNIQUE,
                  escritor VARCHAR(35) NOT NULL DEFAULT ' ',
                  editorial VARCHAR(20) NOT NULL DEFAULT ' ',
                  soporte VARCHAR(35) NOT NULL DEFAULT 'LIBRO',
                  fecha_entrada DATE NOT NULL DEFAULT NULL,
                  pais VARCHAR(20) NOT NULL DEFAULT '',
                  importe DECIMAL(8,2) NOT NULL DEFAULT 0.0,
                  anotaciones BLOB
                )''')

    cur.execute("DROP TABLE IF EXISTS Compras")
    cur.execute('''CREATE TABLE Compras
                ( registro INT(4) NOT NULL PRIMARY KEY UNIQUE,
                  id_comprador INT(4) NOT NULL DEFAULT ' ',
                  id_libro INT(4) NOT NULL DEFAULT ' ',
                  FOREIGN KEY(id_comprador) REFERENCES compradores(registro),
                  FOREIGN KEY(id_libro) REFERENCES Libros(registro)
                )''')

if __name__ == '__main__':
    conn, cur = connect_db()
    create_db(cur)

    conn.close()
