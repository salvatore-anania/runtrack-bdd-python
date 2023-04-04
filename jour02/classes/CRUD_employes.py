from gitignore.connection import conn

class CRUD_employes:
    def __init__(self,conn):
        self.conn=conn
        self.__database=conn.cursor()
    
    def delete_table(self):
        self.__database.execute("drop table employes")
        
    def delete_employe(self,id):
        self.__database.execute(f"delete from employes where id={id}")
        
    def add_employe(self,info):
        self.__database.execute("select count(id) from employes")
        id=self.__database.fetchone()
        info.insert(0,id[0]+1)
        self.__database.execute("insert into employes values (%s,%s,%s,%s,%s)",info)
        conn.commit()
        
    def read(self):
        self.__database.execute("SELECT name,prenom,salaire,nom FROM employes INNER JOIN services ON employes.id_service = services.id")

        resultat=self.__database.fetchall()
        print(resultat)
        
    def read_column(self,column):
        self.__database.execute(f"SELECT {column} FROM employes")
        resultat=self.__database.fetchall()
        print(resultat)
        
    def update_column(self,column,value,id):
        self.__database.execute(f"UPDATE employes set {column} = {value} where id={id}")

    
