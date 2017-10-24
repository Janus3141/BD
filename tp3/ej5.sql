
/* Ejercicio 5 */

USE Inmobiliaria;


/* a */
SELECT Persona.nombre, Persona.apellido FROM Propietario
INNER JOIN Persona ON Propietario.codigo = Persona.codigo;

/* b */
SELECT codigo FROM Inmueble WHERE Precio >= 600000 AND Precio <= 700000;

/* c */
SELECT Persona.nombre, Persona.apellido FROM Persona
WHERE codigo IN (SELECT PZ.codigo_cliente FROM PrefiereZona AS PZ)
AND codigo NOT IN (SELECT codigo_cliente FROM PrefiereZona
                   WHERE nombre_poblacion != 'Santa Fe'
                   OR nombre_zona != 'Norte');
     
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
WHERE Cliente.codigo IN (SELECT Vend.codigo FROM Vendedor AS Vend);

/* f */
SELECT Persona.nombre, Persona.apellido FROM Persona
INNER JOIN PrefiereZona ON PrefiereZona.codigo_cliente = Persona.codigo
WHERE PrefiereZona.nombre_poblacion = 'Rosario'
GROUP BY PrefiereZona.codigo_cliente
HAVING COUNT(PrefiereZona.nombre_zona) =
    (SELECT COUNT(*) FROM Zona WHERE nombre_poblacion = 'Rosario');

/* g */
SELECT Persona.nombre, Persona.apellido, Inm.codigo, Inm.nombre_poblacion, Inm.nombre_zona, Inm.precio
FROM Persona, Inmueble AS Inm
WHERE Inm.codigo IN
    (SELECT Inm2.codigo FROM Inmueble AS Inm2
     /* Filtramos inmuebles no limitrofes */
     WHERE EXISTS (SELECT * FROM Limita
                   INNER JOIN PrefiereZona AS PZ1
                   ON Limita.nombre_poblacion = PZ1.nombre_poblacion
                   AND Limita.nombre_zona = PZ1.nombre_zona
                   WHERE Inm2.nombre_poblacion = Limita.nombre_poblacion_2
                   AND Inm2.nombre_zona = Limita.nombre_zona_2
                   AND Persona.codigo = PZ1.codigo_cliente)
     /* Lo mismo que antes invirtiendo los campos de Limita */
     OR EXISTS (SELECT * FROM Limita AS Lim2 
                INNER JOIN PrefiereZona AS PZ2
                ON Lim2.nombre_poblacion_2 = PZ2.nombre_poblacion
                AND Lim2.nombre_zona_2 = PZ2.nombre_zona
                WHERE Inm2.nombre_poblacion = Lim2.nombre_poblacion
                AND Inm2.nombre_zona = Lim2.nombre_zona
                AND Persona.codigo = PZ2.codigo_cliente)
     /* Filtramos inmuebles en las zonas preferidas */
     AND Inm2.codigo NOT IN (SELECT Inm3.codigo FROM Inmueble AS Inm3
                             INNER JOIN PrefiereZona AS PZ3
                             ON Inm3.nombre_zona = PZ3.nombre_zona
                             AND Inm3.nombre_poblacion = PZ3.nombre_poblacion
                             WHERE Persona.codigo = PZ3.codigo_cliente))
AND Persona.codigo NOT IN 
    /* Personas que no visitaron todas sus zonas preferidas */
    (SELECT PrefiereZona.codigo_cliente FROM PrefiereZona
     INNER JOIN Inmueble ON PrefiereZona.nombre_poblacion = Inmueble.nombre_poblacion
     AND PrefiereZona.nombre_zona = Inmueble.nombre_zona
     WHERE NOT EXISTS (SELECT * FROM Visitas 
                       WHERE PrefiereZona.codigo_cliente = Visitas.codigo_cliente
                       AND Visitas.codigo_inmueble = Inmueble.codigo))