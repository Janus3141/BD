
/* Ejercicio 5 */

USE Inmobiliaria;


/* a */
SELECT nombre,apellido FROM Propietario
INNER JOIN Persona ON Propietario.codigo = Persona.codigo;

/* b */
SELECT codigo FROM Inmueble WHERE Precio >= 600000 AND Precio <= 700000;

/* c */
SELECT Persona.nombre, Persona.apellido FROM Persona
INNER JOIN PrefiereZona ON Persona.codigo = PrefiereZona.codigo_cliente
WHERE PrefiereZona.nombre_poblacion = 'Santa Fe'
AND PrefiereZona.nombre_zona = 'Norte'
AND NOT EXISTS
	(SELECT * FROM PrefiereZona AS PZ WHERE PrefiereZona.codigo_cliente = PZ.codigo_cliente AND
	 PZ.nombre_poblacion != 'Santa Fe' OR PZ.nombre_zona != 'Norte');
     
/* d */
SELECT Persona.nombre, Persona.apellido FROM Vendedor
INNER JOIN Persona ON Vendedor.codigo = Persona.codigo
WHERE EXISTS
	(SELECT * FROM Cliente 
     INNER JOIN PrefiereZona 
     ON Cliente.codigo = PrefiereZona.codigo_cliente
	 WHERE Cliente.vendedor = Vendedor.codigo 
     AND PrefiereZona.nombre_poblacion = 'Rosario'
     AND PrefiereZona.nombre_zona = 'Centro');
     
/* e */
SELECT Persona.nombre, Persona.apellido FROM Persona
INNER JOIN Vendedor ON Vendedor.codigo = Persona.codigo
INNER JOIN Cliente ON Cliente.vendedor = Vendedor.codigo
WHERE Cliente.codigo IN (SELECT Vend.codigo FROM Vendedor);

/* f */
SELECT Persona.nombre, Persona.apellido FROM Persona
INNER JOIN PrefiereZona ON PrefiereZona.codigo_cliente = Persona.codigo
WHERE PrefiereZona.nombre_poblacion = 'Rosario'
GROUP BY PrefiereZona.codigo_cliente
HAVING COUNT(PrefiereZona.nombre_zona) = 5;

/* g */
