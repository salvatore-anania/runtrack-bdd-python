from gitignore.connection import conn

conn=conn()
cursor=conn.cursor()

cursor.execute("select sum(capacite) from salles")
resultat = cursor.fetchone()[0]

print("La capacité de toutes les salles est de :",resultat)

cursor.close()
conn.close()