
import sqlite3 as sql

def create_db():
    con = sql.connect("spj.db")
    con.executescript("""
        CREATE TABLE S (SID INTEGER PRIMARY KEY,
                        SNOMBRE TEXT,
                        SITUACION INTEGER,
                        CIUDAD TEXT);

        CREATE TABLE P (PID INTEGER PRIMARY KEY,
                        PNOMBRE TEXT,
                        COLOR TEXT,
                        PESO INTEGER,
                        CIUDAD TEXT);

        CREATE TABLE J (JID INTEGER PRIMARY KEY,
                        JNOMBRE TEXT,
                        CIUDAD TEXT);

        CREATE TABLE SPJ (SID INTEGER,
                          PID INTEGER,
                          JID INTEGER,
                          CANT INTEGER,
                          FOREIGN KEY(SID) REFERENCES S(SID),
                          FOREIGN KEY(PID) REFERENCES P(PID),
                          FOREIGN KEY(JID) REFERENCES J(JID));

        INSERT INTO S VALUES (1,'Salazar',20,'Londres'),
                             (2,'Jaimes',10,'Paris'),
                             (3,'Bernal',30,'Paris'),
                             (4,'Corona',20,'Londres'),
                             (5,'Aldana',30,'Atenas');

        INSERT INTO P VALUES (1,'Tuerca','Rojo',12,'Londres'),
                             (2,'Perno','Verde',17,'Paris'),
                             (3,'Burlete','Azul',17,'Roma'),
                             (4,'Burlete','Rojo',14,'Londres'),
                             (5,'Leva','Azul',12,'Paris'),
                             (6,'Engranaje','Rojo',19,'Londres');

        INSERT INTO J VALUES (1,'Clasificador','Paris'),
                             (2,'Perforadora','Roma'),
                             (3,'Lectora','Atenas'),
                             (4,'Consola','Atenas'),
                             (5,'Compaginador','Londres'),
                             (6,'Terminal','Oslo'),
                             (7,'Cinta','Londres');

        INSERT INTO SPJ VALUES (1,1,1,200), (1,1,4,700),
                               (2,3,1,400), (2,3,2,200),
                               (2,3,3,200), (2,3,4,500),
                               (2,3,5,600), (2,3,6,400),
                               (2,3,7,800), (2,5,2,100),
                               (3,3,1,200), (3,4,2,500),
                               (4,6,3,300), (4,6,7,300),
                               (5,2,2,200), (5,2,4,100),
                               (5,5,5,500), (5,5,7,100),
                               (5,1,4,100), (5,3,4,200),
                               (5,4,4,800), (5,5,4,400),
                               (5,6,4,500);
    """)
    con.commit()
    con.close()


def query(*args):
    conn = sql.connect("spj.db")
    curs = conn.cursor()
    curs.execute(*args)
    result = curs.fetchall()
    conn.commit()
    conn.close()
    return result



