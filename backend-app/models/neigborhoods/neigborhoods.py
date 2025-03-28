from db.db import Db as DataBase
from pydantic import BaseModel


class get_neiborghoo(BaseModel):
    site_ids:list[int]


class Neigborhoods:
    
    def __init__(self):
        self.db = DataBase()
    
    def get_neiborhoods_report(self,data:get_neiborghoo):
        # query = self.db.cargar_archivo_sql('./sql.sql')
        query = f"""SELECT json_agg(
                    json_build_object(
                        'hoja', site_name,
                        'title', site_name,
                        'column_widths', json_build_object(
                            'id',10,
                            'nombre del barrio', 50,
                            'valor del domicilio', 30
                        ),
                        'data', barrios
                    )
                ) AS hojas
            FROM (
                SELECT 
                    s.site_name,
                    json_agg(
                        json_build_object(
                            'id', n.neighborhood_id,
                            'nombre del barrio', n.name,
                            'valor del domicilio', n.delivery_price
                        )
                    ) AS barrios
                FROM sites s
                JOIN neighborhoods n 
                ON s.site_id = n.site_id
                WHERE s.show_on_web = true
                AND s.site_id IN ({",".join(map(str, data.site_ids))})
                GROUP BY s.site_id, s.site_name
            ) subquery;
            """
        result = self.db.execute_query(query=query,fetch=True)
        return result
    
    
    def update_neigborhoods(self, data:dict):
        
        for sede in data["hojas"]:
            query1 = f"select site_id , city_id from sites where site_name = '{sede["hoja"]}'"
            response1 = self.db.execute_query(query1,fetch=True)
            site_id = response1[0]["site_id"]
            city_id = response1[0]["city_id"]
            query2 = f"delete from neighborhoods where site_id = {site_id} and city_id = {city_id}"
            response2 = self.db.execute_query(query2,fetch=False)
            print(site_id,city_id)
            for barrio in sede["data"]:
                name = barrio["nombre del barrio"]
                delivery_price = barrio["valor del domicilio"]
                
                query3 = f"insert into neighborhoods(name, delivery_price,site_id,city_id) values ('{name}',{delivery_price},{site_id},{city_id})"
                response3 = self.db.execute_query(query3,fetch=False)

                # print (name, delivery_price)
                


        # for sede in data["hojas"]:
        #     # -- 1) Obtenemos site_id y city_id para esta sede
        #     query_site = f"SELECT site_id, city_id FROM sites WHERE site_name = '{sede['hoja']}'"
        #     response_site = self.db.execute_query(query_site, fetch=True)
        #     site_id = response_site[0]["site_id"]
        #     city_id = response_site[0]["city_id"]
            
        #     # -- 2) Armamos la sentencia DELETE para limpiar todos los barrios de esa sede
        #     delete_query = f"DELETE FROM neighborhoods WHERE site_id = {site_id} AND city_id = {city_id}"
            
        #     # -- 3) Construimos el INSERT multi-row
        #     #    Básicamente: INSERT INTO tabla (...) VALUES (..), (..), (..)
        #     #    Esto evita ejecutar un INSERT por cada barrio.
        #     values_list = []
        #     for barrio in sede["data"]:
        #         name = barrio["nombre del barrio"]
        #         delivery_price = barrio["valor del domicilio"]
        #         # OJO con inyección SQL, lo ideal es usar parámetros, 
        #         # pero aquí se muestra con f-string a modo de ejemplo:
        #         values_list.append(f"('{name}', {delivery_price}, {site_id}, {city_id})")

        #     # Si no hay barrios que insertar, te evitas el INSERT
        #     # para no meter un INSERT sin valores.
        #     if values_list:
        #         insert_query = (
        #             "INSERT INTO neighborhoods (name, delivery_price, site_id, city_id) "
        #             f"VALUES {', '.join(values_list)}"
        #         )
        #     else:
        #         # Si no hay barrios, puedes saltarte el INSERT
        #         insert_query = None
            
        #     # -- 4) Ejecutamos todo en una sola llamada
        #     #    Puedes envolverlo en BEGIN/COMMIT si deseas transacción atómica:
        #     #    "BEGIN; {delete_query}; {insert_query}; COMMIT;"
            
        #     if insert_query:
        #         final_query = f"{delete_query}; {insert_query};"
        #     else:
        #         final_query = f"{delete_query};"
            
        #     self.db.execute_query(final_query, fetch=False)
