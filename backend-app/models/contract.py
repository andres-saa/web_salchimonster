from typing import Optional
from pydantic import BaseModel
import psycopg2
from dotenv import load_dotenv
import os
from db.db import Db as DataBase
from schema.video_training.sesion import Sesion as sesion_schema, SesionUpdate as sesion_update_schema
from schema.contracts.contract import EmployerContractPost




class Contract:
    def __init__(self):
        self.db = DataBase()

    def get_all_contracts(self):
        query =  self.db.build_select_query(table_name=' hhrr.latest_contract_view',fields=['*'],condition='')
        return self.db.fetch_all(query)
    
    def get_all_vigent_contracts(self):
        query =  self.db.build_select_query(table_name=' hhrr.vigent_contract_view_order_by_remaining',fields=['*'],condition='')
        return self.db.fetch_all(query)
    

    def get_all_contracts_to_finish(self):
        query =  self.db.build_select_query(table_name=' hhrr.to_finish_contract_view_order_by_remaining',fields=['*'],condition='')
        return self.db.fetch_all(query)
    

    def get_all_finished_contracts(self):
        query =  self.db.build_select_query(table_name=' hhrr.fihished_contract_view_order_by_remaining',fields=['*'],condition='')
        return self.db.fetch_all(query)
    
    
    def get_all_future_contracts(self):
        query =  self.db.build_select_query(table_name=' hhrr.future_contract_view_order_by_remaining',fields=['*'],condition='')
        return self.db.fetch_all(query)
    
    
    
    def get_all_contracts_by_employer_id(self,employer_id):
        query = self.db.build_select_query('hhrr.contract_view',['*'],f'employer_id = {employer_id}')
        result = self.db.fetch_all(query)
        return result
    

    def create_new_contract (self, data:EmployerContractPost):
        query, params = self.db.build_insert_query('hhrr.contract' , data , returning='id')
        return self.db.execute_query(query,params,fetch=True)[0]
    

    def soft_delete_contract (self, contrat_id:int):
        query = self.db.build_soft_delete_query(table_name='hhrr.contract',condition= f'id = {contrat_id}',returning='id')
        return self.db.execute_query(query=query, params=[] , fetch=True)


    def close_connection(self):
        self.db.conn.close()