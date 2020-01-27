import MySQLdb
from model.backend import BackEnd
from dao.conexao import Conexao

class Back_dao(Conexao):
    def select_all(self):
        self.cursor.execute('SELECT * FROM 02_JM_BackEnd')
        selectcomand = self.cursor.fetchall()
        return selectcomand

    def select_by_id(self,id):
        self.cursor.execute(f"SELECT * FROM 02_JM_BackEnd")
        idcomand =  self.cursor.fetchone()
        return idcomand
        
    def update(self, back : BackEnd):
        comand = f"UPDATE 02_JM_BackEnd  SET Nome = '{back.nome}', Descricao = '{back.descricao}', Versao = '{back.versao}' WHERE ID = {back.id}"
        self.cursor.execute(comand)
        self.conexao.commit()

    def insert(self, back: BackEnd):
        comand = f"""INSERT INTO 02_JM_BackEnd
        ( 
            Nome
           ,Descricao
           ,Versao
        )
        VALUES(
            '{back.nome}'
            ,'{back.descricao}'
            ,'{back.versao}'
        )"""
        self.cursor.execute(comand)
        self.conexao.commit()
    
    def delete(self,id):
        comand = f"DELETE FROM 02_JM_BackEnd WHERE ID={id}"
        deletecomand = self.cursor.execute(comand)
        self.conexao.commit()
        return deletecomand
        
