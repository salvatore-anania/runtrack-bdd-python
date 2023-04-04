from gitignore.connection import conn

conn=conn()
cursor=conn.cursor()

cursor.execute("select nom,capacite from salles")
resultat = cursor.fetchall()

print(resultat)

cursor.close()
conn.close()