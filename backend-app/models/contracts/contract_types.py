from typing import Optional
from pydantic import BaseModel
import psycopg2
from dotenv import load_dotenv
import os
from db.db import Db as DataBase
from schema.video_training.sesion import Sesion as sesion_schema, SesionUpdate as sesion_update_schema
from schema.contracts.contract import EmployerContractPost
from schema.contracts.contract import contract_type,soft_delete,days_to_alert


class ContractTypes:
    def __init__(self):
        self.db = DataBase()

    def get_all_contract_types(self):
        query =  self.db.build_select_query(table_name=' hhrr.contract_type',fields=['*'],condition='exist = true')
        return self.db.fetch_all(query)
    


    def get_days_to_alert(self):
        query =  self.db.build_select_query(table_name=' hhrr.days_to_alert',fields=['*'],condition='id = 1')
        return self.db.fetch_all(query)[0]
    

    def update_contract_type(self, id:int, data:contract_type):
        query, params =  self.db.build_update_query( 'hhrr.contract_type',data,f'id = {id}','id' )
        return self.db.execute_query(query,params,fetch=True)[0]
    
    def insert_contract_type(self, data:contract_type):
        query, params =  self.db.build_insert_query( 'hhrr.contract_type',data,'id')
        return self.db.execute_query(query,params,fetch=True)[0]
    


    def update_days_to_alert(self, id:int, data:days_to_alert):
        query, params =  self.db.build_update_query( 'hhrr.days_to_alert',data,f'id = {id}','id' )
        return self.db.execute_query(query,params,fetch=True)[0]
    

    def soft_delete_contract_type(self, id:int, data:soft_delete):
        query, params =  self.db.build_update_query( 'hhrr.contract_type',data,f'id = {id}','id' )
        return self.db.execute_query(query,params,fetch=True)[0]

    
    # def get_all_vigent_contracts(self):
    #     query =  self.db.build_select_query(table_name=' hhrr.vigent_contract_view',fields=['*'],condition='')
    #     return self.db.fetch_all(query)
    
    
    # def get_all_contracts_by_employer_id(self,employer_id):
    #     query = self.db.build_select_query('hhrr.contract_view',['*'],f'employer_id = {employer_id}')
    #     result = self.db.fetch_all(query)
    #     return result
    

    # def create_new_contract (self, data:EmployerContractPost):
    #     query, params = self.db.build_instert_query('hhrr.contract' , data , returning='id')
    #     return self.db.execute_query(query,params,fetch=True)[0]
    

    # def soft_delete_contract (self, contrat_id:int):
    #     query = self.db.build_soft_delete_query(table_name='hhrr.contract',condition= f'id = {contrat_id}',returning='id')
    #     return self.db.execute_query(query=query, params=[] , fetch=True)


    def close_connection(self):
        self.db.conn.close()