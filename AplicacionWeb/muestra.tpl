<!DOCTYPE html>
<html lang="es" xmlns="http://www.w3.org/1999/html">
<head>
<title>Peliculas 2HD</title>
<meta http-equiv="content-type" content="text/html; charset=utf-8" />
<link rel="stylesheet" type="text/css" href="/static/style/style.css" />

<script type="text/javascript">
function cambiar(elemento)
{
	var elem_eliminar = document.getElementsByClassName("b_eliminar");
	var elem_mod =	document.getElementsByClassName("b_modificar");
	var datos_t = document.getElementsByClassName("datos_t");
	var datos_d = document.getElementsByClassName("datos_d");
	var opcion = document.getElementsByClassName("elegir");
	
	if(elemento.value == "modificar"){
		for (var i=0;i<elem_mod.length;i++){
			elem_eliminar[i].style.display = 'none';
			elem_mod[i].style.display = 'block';
			opcion[i].value = "modificar";
			datos_t[i].disabled=false;
			datos_d[i].disabled=false;
		}
		
	}
	else{
		for (var i=0;i<elem_mod.length;i++){
			elem_eliminar[i].style.display = 'block';
			elem_mod[i].style.display = 'none';
			opcion[i].value = "eliminar";
			datos_t[i].disabled=true;
			datos_d[i].disabled=true;
		}
		
	}
		
}

</script>

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
		<div class="mostrar">

		% if info != None:
			<p><strong>{{info}}</strong></p>
		% end

		<div id="opciones">Modificar<input id="mo" type="radio" name="mod"  value="modificar" checked="checked" onclick="cambiar(this)"/>
		Eliminar<input id="el" type="radio" name="mod"  value="eliminar" onclick="cambiar(this)"/></div>
	  <br>
		<table border=1>
			<tr>
				<td><strong>T&iacute;tulo</strong></td>
				<td><strong>Duraci&oacute;n</strong></td>
				<td><strong>Acci&oacute;n</strong></td>
			</tr>
			
			% for n in rows:
			<form action="/peliculas" method="POST">
				<input class="elegir" type="hidden" name="op" value="modificar">
					<tr>
						<input type="hidden" name="id" value="{{n[0]}}">
						<td><input class="datos_t" type="text" name="titulo" value="{{n[1]}}"></td>
						<td><input class="datos_d" type="text" name="duracion" value="{{n[2]}}"></td>
						<td><input class="b_modificar" type="submit" value="Modificar">
						<input class="b_eliminar" type="submit" value="Eliminar"></td>
					</tr>
			</form>
			% end
		</table>
	  
	  </div>
	  </div>
	  
</body>
</html>
