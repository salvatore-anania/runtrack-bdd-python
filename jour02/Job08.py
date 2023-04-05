from connection import conn
from classes.CRUD_zoo import CRUD_zoo

conn=conn()
cursor=conn.cursor()
#verifie l'existence de la database Zoo
stmt = "SHOW databases LIKE 'Zoo'"
cursor.execute(stmt)
result = cursor.fetchone()

if not result:
    #creer la database Zoo si inexistante
    cursor.execute("CREATE database Zoo")
    
#verifie l'existence de la table zoo
stmt = "SHOW TABLES LIKE 'zoo'"
cursor.execute(stmt)
result = cursor.fetchone()
if result:
    #supprime la table zoo si existante
    cursor.execute("drop table zoo")
#creer la table zoo si inexistante et la remplie
cursor.execute("CREATE TABLE zoo(id INT PRIMARY KEY NOT NULL, name varchar(255),race varchar(255), id_type_cage int, date_naissance varchar(255),pays_origine varchar(255))")
crud=CRUD_zoo(conn)
crud.create_animaux(['jaques', 'chat', 1,'04/04/2023','france'])
crud.create_animaux(['paul', 'chien', 2,'04/04/2023','france'])
crud.create_animaux(['pierre', 'oiseau', 3,'04/04/2023','france'])
crud.create_animaux(['charle', 'insectes', 4,'04/04/2023','france'])
crud.create_animaux(['harry', 'souris', 5,'04/04/2023','france'])
crud.create_animaux(['henry', 'poisson', 5,'04/04/2023','france'])


stmt = "SHOW TABLES LIKE 'cage'"
cursor.execute(stmt)
result = cursor.fetchone()

if result:
    #supprime la table cage si existante
    cursor.execute("drop table cage")
#creer la table services si inexistante et la remplie
cursor.execute("CREATE TABLE cage(id INT PRIMARY KEY NOT NULL, superficie int,capacite int)")
cursor.execute("insert into cage values (1,50,5), (2,100,10),(3,150,15), (4,200,20), (5,250,25), (6,300,30)")


    
crud.create_animaux(["test", "chat", 1,'04/04/2023','france'])
go=True
while go:
    print("Que voulez vous faire ?")
    print("1) Modifier animal.")
    print("2) Modifier cage.")
    print("3) Lister animaux.")
    print("4) Lister cage.")
    print("5) Afficher superficie total des cages.")
    print("6) Quitter.")
    choice=int(input())
    if choice==1:
        print("Que voulez vous faire ?")
        print("1) Modifier animal.")
        print("2) Supprimer animal.")
        print("3) Ajouter animal.")
        choice=int(input())
        if choice==1:
            crud.update_line_animal()
        if choice==2:
            crud.delete_animal()
        if choice==3:
            crud.add_animaux()
    elif choice==2:
        print("Que voulez vous faire ?")
        print("1) Modifier cage.")
        print("2) Supprimer cage.")
        print("3) Ajouter cage.")
        choice=int(input())
        if choice==1:
            crud.update_line_cage()
        if choice==2:
            crud.delete_cage()
        if choice==3:
            crud.add_cage()
    elif choice==3:
        crud.read_zoo()
    elif choice==4:
        crud.read_cage()
    elif choice==5:
        crud.calcul_superficie_zoo()
    elif choice==6:
        go=False