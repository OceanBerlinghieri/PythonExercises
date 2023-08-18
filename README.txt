Este es un documento para pensar en distintas aplicacones que pueden tener las principales herramientas de Python
Estas ideas no tienen porque desarrollarse, es un ejercicio de comprensión y reflexión sobre el lenguaje.
También puede servir como Cheatsheet del lenguaje donde almacenemos y podamos consultar rapidamente las distintas
herramientas y usos de estas.

Comenzaremos con una enumeración de las herramientas caracteristicas asi como las generales de Python:
	
	1. Listas
		Las listas en Python son objetos mutables (a diferencia de las tuplas).
		Pueden almacenar datos de distintos tipos de manera ordenada.
		Pueden anidarse e iterarse

		Entre otros metodos encontramos:
			- list.extend(<iterable>): añade una lista a la lista inicial
			- list.insert(<index>, <obj>): Añade un elemento en el índice especificado
			- list.remove(<obj>): Elimina el objeto proporcionado de la lista
			- list.pop(<index=-1>): Elimina por defecto el último elemento de la lista
			- list.reverse(): Invierte el orden de la lista
			- list.sort(): Ordena de menos a más los elementos.
				(Con el parametro reverse = True ordenará de mayor a menor)
				(Recomendado realizarlo con listas que tengan el mismo tipo de elementos)
			- list.index(<obj>): Devuelve el primer indice donde aparece el objeto parametro
				(Un segundo parametro sería para la cantidad de indices que queremos 
				que devuelva)

	2. Tuplas
		Las tuplas son colecciones inmutables, es decir, no pueden modificarse como las listas
		Cada vez que modificamos una tupla, creamos una nueva tupla, no la extendemos,
		ni insertamos elementos ni los eliminamos.


	3. Diccionarios
		Los diccionarios son colecciones que almacenan valores para unas determiandas claves
		Pueden ser muy útiles en operaciones de conteo, como por ejemplo, conteo de la misma
		palabra en una frase

	4. Excepciones
		Usamos las excepciones para el control de errores, divididas en tres bloques 
		principales: try, except y finally

	5. Comprensión de listas y colecciones
		La comprensión de listas y colecciones nos permite crear colecciones de datos con
		una sitaxis más compacta, elegante y legible

	6. Cadenas
		1. Operaciones con cadenas
		2. Cadenas como secuencias
		3. Metodos de cadenas
	
	7. Programacion Orientada a Objetos
		1. Propiedades globales vs de instancia
		2. Métodos
		3. Herencia
		4. Excepciones como clases
	
	8. Funciones lambda 
	9. Generadores
	10. Iteradores
	11. Cierres
