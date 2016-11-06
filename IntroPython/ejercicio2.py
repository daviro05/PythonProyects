# David Rodriguez Marco

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from smtplib import SMTP

def pedirDatos():
    repetir = True 

    while repetir:
        servidor = raw_input("Servidor: ")
        puerto = raw_input("Puerto: ")
        remitente = raw_input("Remitente: ")
        password = raw_input("Password del remitente: ")
        destinatario = raw_input("Destinatario: ")
        mensaje = raw_input("Mensaje: ")
        enviar = raw_input("Desea enviar (Si/No): ")
        
        try:
            servidor = SMTP(servidor,puerto)
            servidor.ehlo()
            servidor.starttls()
            servidor.ehlo()
            servidor.login(remitente,password)
            servidor.sendmail(remitente, destinatario, mensaje)
            servidor.quit()
            print "Mensaje enviado correctamente"
        except:
            print "Error al mandar el correo"

        if enviar == "No":
            enviar = raw_input("Mandar otro mensaje: (Si/No): ")
            repetir = enviar == "Si"

if __name__ == "__main__":
    pedirDatos()
    