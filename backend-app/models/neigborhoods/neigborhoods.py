from db.db import Db as DataBase





class Neigborhoods:
    
    def __init__(self):
        self.db = DataBase()
    
    def get_neiborhoods_report(self):
        query = self.db.cargar_archivo_sql('./sql.sql')
        result = self.db.fetch_all(query=query)
        return result
    