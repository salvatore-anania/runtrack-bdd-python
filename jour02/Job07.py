from gitignore.connection import conn
from classes.CRUD_employes import CRUD_employes

conn=conn()
cursor=conn.cursor()
#verifie l'existence de la database etage
stmt = "SHOW databases LIKE 'temporaire'"
cursor.execute(stmt)
result = cursor.fetchone()

if result:
    #lis la database temporaire si existante
    cursor.execute("show tables ")
    resultat=cursor.fetchall()
    print(resultat)
else:
    #creer la database temporaire si inexistante
    cursor.execute("CREATE database temporaire")
    
#verifie l'existence de la table employes
stmt = "SHOW TABLES LIKE 'employes'"
cursor.execute(stmt)
result = cursor.fetchone()
if result:
    #supprime la table employes si existante
    cursor.execute("drop table employes")
#creer la table employes si inexistante et la remplie
cursor.execute("CREATE TABLE employes(id INT PRIMARY KEY NOT NULL, name varchar(255),prenom varchar(255),salaire decimal, id_service int)")
crud=CRUD_employes(conn)
crud.add_employe(['chirac', 'jacque', 3500,2])
crud.add_employe(['paul', 'henry', 3000.67,3])
crud.add_employe(['starck', 'tony', 1456.67,4])
crud.add_employe(['deux', 'charle', 1456.67,6])
crud.add_employe(['potter', 'harry', 1456.67,1])
crud.add_employe(['bocuse', 'paul', 3050.67,5])

cursor.execute("select * from employes where salaire>3000.0")
resultat=cursor.fetchall()
print(resultat)

stmt = "SHOW TABLES LIKE 'services'"
cursor.execute(stmt)
result = cursor.fetchone()

if result:
    #supprime la table services si existante
    cursor.execute("drop table services")

cursor.execute("CREATE TABLE services(id INT PRIMARY KEY NOT NULL, nom varchar(255))")
cursor.execute("insert into services values (1,'developpement'), (2,'data_science'), (3,'web'), (4,'graphiste'), (5,'compta'), (6,'R-H')")
conn.commit()

crud.read_column("prenom")
crud.add_employe(["test", "go", 1,2])
crud.update_column("salaire",1000,1)
crud.read()

conn.commit()