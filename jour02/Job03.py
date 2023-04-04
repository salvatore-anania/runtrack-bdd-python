from gitignore.connection import conn

conn=conn()
cursor=conn.cursor()

val=[]

cursor.execute("insert into etage values (1,'RDC', 0, 500),(2,'RDC+1', 1, 500)")

cursor.execute("select * from etage")
resultat = cursor.fetchall()
print(resultat)
cursor.execute("insert into salles values (1,'Lounge', 1, 100), (2,'Studio Son', 1, 5), (3,'Broadcasting', 2, 50), (4,'Bocal Peda', 2, 4), (5,'Coworking', 2, 80), (6,'Studio Video', 2, 5)")
conn.commit()
cursor.execute("select * from salles")
resultat = cursor.fetchall()
print(resultat)

cursor.close()
conn.close()