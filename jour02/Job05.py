from gitignore.connection import conn

conn=conn()
cursor=conn.cursor()

cursor.execute("select sum(superficie) from etage")
resultat = cursor.fetchone()[0]

print("La superficie de la Plateforme est de",resultat,"m2")

cursor.close()
conn.close()