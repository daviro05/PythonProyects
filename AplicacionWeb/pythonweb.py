# -*- coding: cp1252 -*-
from bottle import route, run, request, template, response, static_file, redirect, error, default_app
import sqlite3

def check_login(username, password):
    db = sqlite3.connect('peliculas.sqlite3')
    c = db.cursor()
    c.execute("SELECT * FROM usuarios WHERE username = ? AND password = ?", (username, password))
    id_exists = c.fetchone()
    c.close()
    if id_exists:
        return True
    else:
        return False

def registrar(username, password, nombre, apellidos, email):
    db = sqlite3.connect('peliculas.sqlite3')
    c = db.cursor()
    c.execute('''INSERT INTO usuarios 
                (username, password, nombre, apellidos, email) 
                VALUES (?,?,?,?,?)''', 
                (username, password, nombre, apellidos, email))

    db.commit()
    c.close()
    return True

@route('/')
@route('/login')
def login():
    return template("login.tpl")


@route('/login', method='POST')
def do_login():
    username = request.forms.get('user')
    password = request.forms.get('password')

    if check_login(username, password):
        response.set_cookie("account", username, secret='clave-secreta-muahahaha')
        redirect('/mainPage')
    else:
        return template("login.tpl", incorrecto=True)


@route('/register')
def register():
    return template("registro.tpl")
		
@route('/anadir')
def anadir():
    username = request.get_cookie("account", secret='clave-secreta-muahahaha')
    if username:
        return template("anadir.tpl", info=None)
    else:
        return "No puedes entrar aqui sin estar logueado."	
		
    return template("anadir.tpl", info=None)

@route('/anadir', method='POST')
def anadir():
    titulo = request.forms.get('titulo')
    duracion = request.forms.get('duracion')
    db = sqlite3.connect('peliculas.sqlite3')
    c = db.cursor()
    c.execute("INSERT INTO peliculas(titulo, duracion) VALUES(?,?)", (titulo, duracion))
    prueba = "Película añadida"
    db.commit()
    c.close()
    return template("anadir.tpl", info=prueba)

@route('/buscar')
def buscar():
    username = request.get_cookie("account", secret='clave-secreta-muahahaha')
    if username:
        return template("buscar.tpl")
    else:
        return "No puedes entrar aqui sin estar logueado."	

@route('/buscar', method='POST')
def buscar():
    name = request.forms.get('busqueda')
    db = sqlite3.connect('peliculas.sqlite3')
    c = db.cursor()
    c.execute("SELECT titulo, duracion FROM peliculas WHERE titulo LIKE (?)", ['%' + name + '%'])
    data = c.fetchall()
    c.close()
    output = template('buscar_sql.tpl', rows=data)

    return output
	
@route('/register', method='POST')
def register():
    username = request.forms.get('user')
    password = request.forms.get('password')
    nombre = request.forms.get('nombre')
    apellidos = request.forms.get('apellidos')
    email = request.forms.get('email')
    if registrar(username, password, nombre, apellidos, email):
        redirect('/login')
    else:
        return template("registro.tpl")

@route('/peliculas', method='POST')
def modificar():
    _id = request.forms.get('id')
    titulo = request.forms.get('titulo')
    opcion = request.forms.get('op')
    duracion = request.forms.get('duracion')

    db = sqlite3.connect('peliculas.sqlite3')
    c = db.cursor()
    mensaje = ""
    if opcion == "modificar":
        print _id, duracion
        c.execute("UPDATE peliculas SET titulo = ?, duracion = ? WHERE id = ?", 
                (titulo, duracion, _id))
        mensaje = "Datos actualizados"
    elif opcion == "eliminar":
        c.execute("DELETE FROM peliculas WHERE id = (?)", [_id])
        mensaje = "Dato eliminado"
    db.commit()
    c.execute("SELECT * FROM peliculas")
    data = c.fetchall()
    c.close()
    return template("muestra.tpl", rows=data, info=mensaje)
		
@route('/peliculas')
def mostrar_peliculas():
    db = sqlite3.connect('peliculas.sqlite3')
    c = db.cursor()
    c.execute("SELECT * FROM peliculas")
    data = c.fetchall()
    c.close()
    output = template('muestra', rows=data, info=None)

    return output
		
@route('/mainPage')
def restricted_area():
    username = request.get_cookie("account", secret='clave-secreta-muahahaha')
    if username:
        return template("template.tpl", name=username)
    else:
        return "No puedes entrar aqui sin estar logueado."

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')
	

@route('/logout')
def logout():
    response.delete_cookie("account")
    redirect ("/login");



run(host='localhost', port=8080)
