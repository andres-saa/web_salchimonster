from db.db import Db as DataBase
from pydantic import BaseModel
from typing import List, Optional


class aditional_type_schema(BaseModel):
    name:str
    max_selected:int



class BannerAppSchema(BaseModel):
    index: int
    img_identifier: str

class BannerReorderSchema(BaseModel):
    banners: List[BannerAppSchema]

class group_sabor_schema(BaseModel):
    flavor_id:int
    flavor_group_id:int
    

class aditional_schema(BaseModel):
    name:str
    type_id:int
    price:int


class ProductCategorySchema(BaseModel):
    name: str
    index: int
    restaurant_id: int
    main: bool
    

class Banners:
    
    
    def __init__(self):
        self.db = DataBase()
    
    def create_banner(self, data: BannerAppSchema):
        query, params = self.db.build_insert_query(
            table_name='app.banner_app',
            data=data,
            returning='id'
        )
        result = self.db.execute_query(query=query, params=params, fetch=True)
        return result

    def get_banners(self):
        query = self.db.build_select_query(
            'app.banner_app',
            fields=["*"],
            order_by='id',
              condition='exist = true'  # Ordenar por id
        )
        result = self.db.execute_query(query=query,fetch=True)
        return result

    def get_banner_by_id(self, banner_id: int):
        query = self.db.build_select_query(
            'app.banner_app',
            fields=["*"],
            condition=f'id = {banner_id}'
        )
        result = self.db.fetch_one(query=query)
        return result

    def update_banner(self, banner_id: int, data: BannerAppSchema):
        query, params = self.db.build_update_query(
            table_name='app.banner_app',
            data=data,
            condition=f'id = {banner_id}',
            returning='id'
        )
        result = self.db.execute_query(query=query, params=params, fetch=True)
        return result

    def delete_banner(self, banner_id: int):
        query = self.db.build_soft_delete_query(
            'app.banner_app',
            condition=f'id = {banner_id}',
            returning='id'
        )
        result = self.db.execute_query(query=query, fetch=True)
        return result

    # Método para reordenar banners
    def reorder_banners(self, banners: List[BannerAppSchema]):
        # Construir la consulta para actualizar múltiples filas en una sola operación
        update_queries = []
        for banner in banners:
            update_queries.append(
                f"UPDATE app.banner_app SET index = {banner.index} WHERE id = {banner.id}"
            )
        
        # Unir todas las consultas en un solo comando usando un punto y coma
        final_query = ";\n".join(update_queries)
        
        # Ejecutar la consulta final
        self.db.execute_query(query=final_query, fetch=False)
        return {"status": "success", "message": "Banners reordered successfully"}




