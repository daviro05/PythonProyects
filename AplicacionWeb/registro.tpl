<!DOCTYPE HTML>
<html lang="es" xmlns="http://www.w3.org/1999/html">

  <head>
 	<title>Peliculas 2HD</title>
		<link rel="stylesheet" href="static/style/style_login.css" />
		
		
   </head>
    <body>
				<form action="/register" class="form3" name="log" method="post">
					<p class="logo">
				        <img id="logo2" src="static/style/logo.png">
				    </p>
					<br>
					<p class="ti">Registro</p>
					<br>
				    <p class="a">
				        <label for="login">Usuario</label>
				        <input type="text" name="user" id="login" placeholder="Usuario" required>
				    </p>
				    <p class="a">
				        <label for="password">Contraseña</label>
				        <input type="password" name="password" id="password" placeholder="Contraseña" required> 
				    </p>
				    <p class="a">
				        <label for="nombre">Nombre</label>
				        <input type="text" name="nombre" id="nombre" placeholder="Nombre" required> 
				    </p>
				    <p class="a">
				        <label for="apellidos">Apellidos</label>
				        <input type="text" name="apellidos" id="apellidos" placeholder="Apellidos" required> 
				    </p>
				    <p class="a">
				        <label for="email">Email</label>
				        <input type="text" name="email" id="email" placeholder="Email" required> 
				    </p>
				    <p class="a">
				        <p id="entra"><input class="botones" type="submit" value="Registro"/></p>
				    </p>
					<p id="reg"><a href='login'>Volver atrás</p></a>
				</form>
				
    </body>
</html>
