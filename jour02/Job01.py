from gitignore.connection import conn

conn=conn()
cursor=conn.cursor()

cursor.execute("select * from etudiants")
resultat = cursor.fetchall()

print(resultat)

cursor.close()
conn.close()