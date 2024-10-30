
from db.db import Db as DataBase
from pydantic import BaseModel
from schema.pqr import pqrs
from schema.user import user_schema_post
from models.orders.order2 import Order2
from datetime import date



class StatusHistory(BaseModel):
    pqr_request_id: int
    status_id: int
    notes: str
    
    
    
class ChangeStatusRequest(BaseModel):
    pqr_request_id: int
    status_id: int
    responsible_id: int
    value: float = 0.0
    notes: str = ''
    order_id:str
    

class filtered_schema(BaseModel):
    sites:tuple[int]
    start_date:str
    end_date:str
    

class cachier_money_entry(BaseModel):
    cachier_id:int
    work_schedule_id:int
    value:int
    date:str
    money_cachier_delivery_id:int   


class Output(BaseModel):
    date: date
    content: str
    value: int
    output_type_id: int
    responsible_id: int
    work_schedule_id:int


class CachierMoney:
    
    def __init__(self):
        self.db = DataBase()
        
        
    
    def get_all_cachier_money(self):
        query = self.db.build_select_query(table_name='cachier.v_cachier_entry_detail',fields=["*"])
        pqr_id = self.db.execute_query(query=query,fetch=True)
        return pqr_id
    
        
      
    def get_cachier_money_by_site_id(self,site_id:int):
        query = self.db.build_select_query(table_name='cachier.v_cachier_entry_detail',fields=["*"],condition=f"site_id={site_id}")
        pqr_id = self.db.execute_query(query=query,fetch=True)
        return pqr_id
    
    def get_call_work_schedule(self):
        query = self.db.build_select_query(table_name='cachier.work_schedule',fields=["*"])
        pqr_id = self.db.execute_query(query=query,fetch=True)
        return pqr_id



    def get_call_output_types(self):
        query = self.db.build_select_query(table_name='cachier.output_types',fields=["*"])
        pqr_id = self.db.execute_query(query=query,fetch=True)
        return pqr_id
         
    
    def get_cachier_money_filtered(self, data: filtered_schema):
        
    # Convertir a tupla y manejar el caso de un solo elemento
        sites = tuple(data.sites) if len(data.sites) > 1 else f'({data.sites[0]})'

        query = self.db.build_select_query(
            table_name='cachier.v_cachier_entry_detail',
            fields=["*"],
            condition=f"site_id IN {sites} and date BETWEEN '{data.start_date}' AND '{data.end_date}'"
        )
        
        
        query_outputs = self.db.build_select_query(
            table_name='cachier.v_output',
            fields=["*"],
            condition=f"site_id IN {sites} and output_type_id = 5 AND  date  BETWEEN '{data.start_date}' AND '{data.end_date}' "
        )
        
        query_outputs_shop = self.db.build_select_query(
            table_name='cachier.v_output',
            fields=["*"],
            condition=f"site_id IN {sites}  AND output_type_id = 6 and  date  BETWEEN '{data.start_date}' AND '{data.end_date}'"
        )
        

        

        pqr_id = self.db.execute_query(query=query, fetch=True)
        query_outputs_data = self.db.execute_query(query_outputs,fetch=True)
        query_outputs_shop_data = self.db.execute_query(query=query_outputs_shop,fetch=True)
        return {"report":pqr_id, "outputs":query_outputs_data, "shops":query_outputs_shop_data} 
    
  
  
    def create_output(self,data:Output,site_id:int):
        
        
        
        query_site_id = self.db.build_select_query(table_name='cachier.money_cachier_delivery',condition=f"site_id = {site_id}",fields=["*"])
        
        query_site_id_result = self.db.execute_query(query_site_id,fetch=True)
        money_cachier_delivery_id = query_site_id_result[0]['id']
        
        
        
        class final_data(Output):
            money_cachier_site_id:int
            
        
        last_data = final_data(
            date=data.date,
            content=data.content,
            value=data.value,
            responsible_id=data.responsible_id,
            output_type_id=data.output_type_id,
            money_cachier_site_id=money_cachier_delivery_id,
            work_schedule_id = data.work_schedule_id
        )
            
        query,params = self.db.build_insert_query(table_name='cachier.output_entry',data=last_data,returning='id')
        result = self.db.execute_query(query=query,params=params,fetch=True)
        return result
  

    def create_cachier_money_entry(self,data:cachier_money_entry):
        
        
        class complete_cachier_entry_schema(BaseModel):
                cachier_id:int
                work_schedule_id:int
                value:int
                money_cachier_delivery_id:int
                date:date
                site_id:int
        
        query_site_id = self.db.build_select_query(table_name='cachier.money_cachier_delivery',condition=f"site_id = {data.site_id}",fields=["*"])
        
        query_site_id_result = self.db.execute_query(query_site_id,fetch=True)
        money_cachier_delivery_id = query_site_id_result[0]['id']
        
        print(money_cachier_delivery_id)
        
        
        if money_cachier_delivery_id:
            
            complete_cachier_entry_schema = cachier_money_entry(
                cachier_id=data.cachier_id,
                work_schedule_id=data.work_schedule_id,
                value=data.value,
                money_cachier_delivery_id = money_cachier_delivery_id,
                date=data.date,
            )
        
            query, params = self.db.build_insert_query(table_name='cachier.money_cachier_delivery_entry',data=complete_cachier_entry_schema,returning='id')
            
            results = self.db.execute_query(query=query,params=params,fetch=True)
            return results
    
        return results