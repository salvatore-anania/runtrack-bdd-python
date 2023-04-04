from gitignore.connection import conn

conn=conn()
cursor=conn.cursor()
#verifie l'existence de la table etage
stmt = "SHOW TABLES LIKE 'etage'"
cursor.execute(stmt)
result = cursor.fetchone()

if result:
    #lis la table etage si existante
    cursor.execute("select * from etage")
    resultat=cursor.fetchall()
    print(resultat)
else:
    #creer la table etage si inexistante
    cursor.execute("CREATE TABLE etage (id INT PRIMARY KEY NOT NULL, nom varchar(255),numero int, superficie int)")

#verifie l'existence de la table salles
stmt = "SHOW TABLES LIKE 'salles'"
cursor.execute(stmt)
result = cursor.fetchone()

if result:
    #lis la table salles si existante
    cursor.execute("select * from salles")
    resultat=cursor.fetchall()
    print(resultat)
else:
    #creer la table salles si inexistante
    cursor.execute("CREATE TABLE salles(id INT PRIMARY KEY NOT NULL, nom varchar(255), id_etage int, capacite int)")
    
cursor.close()
conn.close()