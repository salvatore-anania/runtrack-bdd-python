from gitignore.connection import conn

class CRUD_zoo:
    def __init__(self,conn):
        self.conn=conn
        self.__database=conn.cursor()
    
    def delete_table(self):
        self.__database.execute("drop table zoo")
    
    def delete_animal(self):
        print("Id de l'animal à supprimer : ")
        id=input()
        self.__database.execute(f"delete from zoo where id={id}")
        
    def delete_cage(self):
        print("Id de la cage à supprimer : ")
        id=input()
        self.__database.execute(f"delete from cage where id={id}")
        
    def create_animaux(self,info):
        self.__database.execute("select count(id) from zoo")
        id=self.__database.fetchone()
        info.insert(0,id[0]+1)
        self.__database.execute("insert into zoo values (%s,%s,%s,%s,%s,%s)",info)
        self.conn.commit()
        
    def add_animaux(self):
        info=[]
        print("Nom de l'animal : ")
        info.append(input())
        print("Race de l'animal : ")
        info.append(input())
        print("Id de la cage : ")
        info.append(input())
        print("Date de l'animal : ")
        info.append(input())
        print("Pays d'origine de la cage : ")
        info.append(input())
        self.__database.execute("select count(id) from zoo")
        id=self.__database.fetchone()
        info.insert(0,id[0]+1)
        self.__database.execute("insert into zoo values (%s,%s,%s,%s,%s,%s)",info)
        self.conn.commit()
    
    def add_cage(self):
        info=[]
        print("Superficie de la cage : ")
        info.append(input())
        print("capacite de la cage : ")
        info.append(input())
        self.__database.execute("select count(id) from zoo")
        id=self.__database.fetchone()
        info.insert(0,id[0]+1)
        self.__database.execute("insert into zoo values (%s,%s,%s)",info)
        self.conn.commit()
        print(f"Ajout de la cage ID numero {id} terminer")
        
    def read_zoo(self):
        print("---------------------\nListe des animaux dans le zoo : \n")
        self.__database.execute("SELECT id,name,race,date_naissance,pays_origine FROM zoo")
        zoo=self.__database.fetchall()
        for animal in zoo:
            print(animal)
            
    def read_cage(self):
        print("---------------------\ncage : \n")
        self.__database.execute("SELECT cage.id,name,race,superficie FROM cage inner JOIN zoo ON id_type_cage = cage.id order by cage.id")
        cage=self.__database.fetchall()
        for animal in cage:
            print(animal)
        
    def read_column(self,column):
        self.__database.execute(f"SELECT {column} FROM zoo")
        resultat=self.__database.fetchall()
        print(resultat)
        
    def update_line_animal(self):
        print("Id de l'animal à modifier : ")
        id=input()
        print("Clé à modifier : ")
        column=input()
        print("Valeur à entrer : ")
        value=input()
        self.__database.execute(f"UPDATE zoo set {column} = '{value}' where id={id}")
        
    def update_line_cage(self):
        print("Id de l'anima à modifier : ")
        id=input()
        print("Clé à modifier : ")
        column=input()
        print("Valeur à entrer : ")
        value=input()
        self.__database.execute(f"UPDATE cage set {column} = '{value}' where id={id}")
        
    def calcul_superficie_zoo(self):
        self.__database.execute("select sum(superficie) from cage")
        resultat=self.__database.fetchone()
        print(resultat[0])

    
