import os
import sqlite3

class DatabaseCartao:
    @classmethod
    def get_db_connection(cls):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Diretório do db.py
        db_path = os.path.join(BASE_DIR, "cartao.db")  # Caminho correto do banco de dados
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        return conn  


       

    @classmethod
    def create_table(cls):
        conn = cls.get_db_connection()  
        conn.execute("""
            CREATE TABLE IF NOT EXISTS Cartao (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Nome TEXT NOT NULL,
                Local TEXT NOT NULL,
                Valor REAL,
                Data TEXT NOT NULL,
                Cartao TEXT NOT NULL,
                Parcelado INTEGER
            )
        """)
        conn.commit()
        conn.close()

    @classmethod
    def query(cls, texto, params=None):
         conn = cls.get_db_connection()
         cursor = conn.execute(texto, params or ())
         results = cursor.fetchall()  # Pegamos os resultados antes de fechar a conexão
         conn.commit()
         conn.close()
         return results  # Retornamos os resultados já processados
   



DatabaseCartao.create_table()

    