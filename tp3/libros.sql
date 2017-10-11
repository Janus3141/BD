
/*Ejercicio 1 */

DROP DATABASE Libreria;

CREATE DATABASE Libreria;

USE Libreria;

CREATE TABLE Autor (
    ID INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(20) NOT NULL,
    Apellido VARCHAR(30) NOT NULL,
    Nacionalidad VARCHAR(30),
    Residencia VARCHAR(50)
);

CREATE TABLE Libro (
    ISBN INT UNSIGNED PRIMARY KEY,
    Titulo VARCHAR(50) NOT NULL,
    Editorial VARCHAR(50),
    Precio INT UNSIGNED NOT NULL
);

CREATE TABLE Escribe (
    ID INT UNSIGNED,
    ISBN INT UNSIGNED,
    Año DATE,
	PRIMARY KEY(ID, ISBN),
    FOREIGN KEY(ID) REFERENCES Autor(ID) ON DELETE cascade,
    FOREIGN KEY(ISBN) REFERENCES Libro(ISBN) ON DELETE cascade
);

/* Ejercicio 2 */

CREATE INDEX TITULO_INDEX
ON Libro(Titulo);

CREATE INDEX AUTOR_INDEX
ON Autor(Apellido);

/* Ejercicio 3 */

INSERT INTO Autor(Nombre,Apellido,Nacionalidad,Residencia) VALUES ("Abelardo","Castillo","Suiza","Alpes");
INSERT INTO Autor(Nombre,Apellido,Nacionalidad,Residencia) VALUES ("Luis","Lopez","Mexico","Mexico DF");

INSERT INTO Libro VALUES (1000,"El quijote","UNR",1500);
INSERT INTO Libro VALUES (1001,"Parry Hotter","L.A. Rowling",2000);

INSERT INTO Escribe VALUES (1,1000,'1901-09-30');
INSERT INTO Escribe VALUES (2,1001,'1998-05-04');

/* Ejercicio 4 */

UPDATE Autor SET Residencia="Buenos Aires" WHERE Nombre="Abelardo" AND Apellido="Castillo";

UPDATE Libro SET Precio= Precio+Precio*0.1 WHERE Editorial="UNR";

UPDATE Libro SET Precio = CASE
	WHEN Precio < 200 THEN Precio+Precio*0.2
	ELSE Precio+Precio*0.1
END WHERE ISBN IN
	(SELECT ISBN FROM Escribe where ID IN
	(SELECT ID FROM Autor WHERE Nacionalidad != "Argentina"));

DELETE FROM Libro WHERE ISBN IN (SELECT ISBN FROM Escribe WHERE Año > '1998-1-1' AND Año < '1998-12-31');

/* Ejercicio 5 */




