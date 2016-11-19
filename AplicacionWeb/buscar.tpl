<!DOCTYPE html>
<html lang="es" xmlns="http://www.w3.org/1999/html">
<head>
<title>Peliculas 2HD</title>
<meta http-equiv="content-type" content="text/html; charset=utf-8" />
<link rel="stylesheet" type="text/css" href="/static/style/style.css" />
</head>

<body>
    <header>
       <div id="panel"><img id="logo" src="/static/style/logo.png" alt="Peliculas 2HD" /></div>
    </header>
	  
	  <div id="contenido">
		  <div id="tabla">
			  <ul id="menu">
				<li><a href="/peliculas">Peliculas</a>
				<li><a href="/anadir">Añadir</a>
				<li><a href="/buscar">Buscar</a>
				<li><a href="/logout">Salir</a>
			 </ul>
		 </div>
		<div id="mostrar">
	  
	 <form name="ejemplo" action="/buscar" method="POST">
		Buscar Película: <input type="search" name="busqueda">
		<input type="submit" value="Buscar">
	</form>

	  
	  </div>
	  </div>
	  
</body>
</html>
