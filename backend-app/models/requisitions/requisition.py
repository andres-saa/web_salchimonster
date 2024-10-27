from schema.requisitions.requisition import Requisition,LapHistory,Vacancy,Applicant,cvFile
from db.db import Db as DataBase




class Requisitions:
    
    
    def __init__(self):
        self.db = DataBase()
        
    def get_all_requisitions(self):
        query = self.db.build_select_query(
            table_name='requisitions.requisition_view',
            fields=['*'],
            condition='',
            order_by='id',
            )
        result = self.db.execute_query(query=query,fetch=True)
        return result 
        
    def get_all_vacancies(self):
        query = self.db.build_select_query(
            table_name='requisitions.vacancy_view',
            fields=['*'],
            condition='',
            order_by='id',
            )
    
        result = self.db.execute_query(query=query,fetch=True)
        return result
    
    def create_requisition(self, data:Requisition):
        
        query_lap = self.db.build_select_query('requisitions.requisition_area',['validation_type_id'],f"id = {data.area_id}")
        
        validation_type = self.db.execute_query(query_lap,fetch=True)[0]
        
        lap_desition = 0
        if (validation_type and validation_type["validation_type_id"] == 1):
            lap_desition = 1
        else:
            lap_desition = 12

        data_to_create_requisition = Requisition(
            requisition_id=data.requester_id,
            area_id=data.area_id,
            requester_id=data.requester_id,
            created_by=data.created_by,
            description=data.description,
            requisition_lap_id= lap_desition
        )
        
        query,params = self.db.build_insert_query(table_name="requisitions.requisition",data=data_to_create_requisition,returning='id',)
        
        result = self.db.execute_query(query=query,params=params,fetch=True)[0]
        
        requisition_id = result["id"]
        

        lap = LapHistory(
            requisition_id=requisition_id,
            requisition_lap_id=lap_desition,
            responsible_id=data.requester_id
        )
        
        lap2 = LapHistory(
            requisition_id=requisition_id,
            requisition_lap_id=14,
            responsible_id=1132
        )
        
        lapinicial = LapHistory(
            requisition_id=requisition_id,
            requisition_lap_id=15,
            responsible_id=data.requester_id
        )
        
        
        queryHistoryInit,paramsHistoryInit = self.db.build_insert_query(table_name="requisitions.lap_history",data=lapinicial,returning='id',)
        result_lapInit = self.db.execute_query(query=queryHistoryInit,params=paramsHistoryInit,fetch=True)[0]
        
        if lap_desition == 12:
            queryHistory2,paramsHistory2 = self.db.build_insert_query(table_name="requisitions.lap_history",data=lap2,returning='id',)
            esult_lap2 = self.db.execute_query(query=queryHistory2,params=paramsHistory2,fetch=True)[0]
        
        
        queryHistory,paramsHistory = self.db.build_insert_query(table_name="requisitions.lap_history",data=lap,returning='id',)
        
        result_lap = self.db.execute_query(query=queryHistory,params=paramsHistory,fetch=True)[0]
        
        return result
       
    def authorize_requisition(self, requisition_id, responsible_id):
        # Inserta lap_history con id 2
        query_insert_lap2 = "INSERT INTO requisitions.lap_history (requisition_id, requisition_lap_id, responsible_id) VALUES (%s, 2, %s) RETURNING id"
        result_lap2 = self.db.execute_query(query=query_insert_lap2, params=[requisition_id, responsible_id], fetch=True)[0]

        # Inserta lap_history con id 12 sin responsible_id
        query_insert_lap12 = "INSERT INTO requisitions.lap_history (requisition_id, requisition_lap_id) VALUES (%s, 12) RETURNING id"
        result_lap12 = self.db.execute_query(query=query_insert_lap12, params=[requisition_id], fetch=True)[0]

        # Actualiza la requisition para establecer requisition_lap_id en 12
        query_update_requisition = "UPDATE requisitions.requisition SET requisition_lap_id = 12 WHERE id = %s"
        self.db.execute_query(query=query_update_requisition, params=[requisition_id])

        return {"lap_history_2_id": result_lap2['id'], "lap_history_12_id": result_lap12['id']}

    def reject_requisition(self, requisition_id, responsible_id):
        # Inserta lap_history con id 13 indicando rechazo
        query_insert_lap = "INSERT INTO requisitions.lap_history (requisition_id, requisition_lap_id, responsible_id) VALUES (%s, 13, %s) RETURNING id"
        result_lap = self.db.execute_query(query=query_insert_lap, params=[requisition_id, responsible_id], fetch=True)[0]

        # Actualiza la requisition para establecer requisition_lap_id en 13, indicando rechazo
        query_update_requisition = "UPDATE requisitions.requisition SET requisition_lap_id = 13 WHERE id = %s"
        self.db.execute_query(query=query_update_requisition, params=[requisition_id])

        return {"lap_history_id": result_lap['id']}
    
    def create_vacancy(self,data:Vacancy):
        query, params = self.db.build_insert_query("requisitions.vacancy",data=data,returning='id')
        
        vacancy_id = self.db.execute_query(
            query=query,
            params=params,
            fetch=True)
        
        return vacancy_id[0]
    
    def create_applicant(self, data:Applicant,cv_file:cvFile ):
        
      
        
        query_file, params_file = self.db.build_insert_query(table_name="requisitions.cv_file",data=cv_file,returning='id')
        
        file = self.db.execute_query(query=query_file,params=params_file,fetch=True)[0]
        file_id = file["id"]
        
        
        applicant_data = Applicant(
            name=data.name,
            email=data.email,
            phone=data.phone,
            cv_file_id=file_id,
            vacancy_id=data.vacancy_id,
            lap_id=1
        )
        query, params = self.db.build_insert_query(table_name="requisitions.applicant", data=applicant_data, returning='id')
        
        applicant_id = self.db.execute_query(query=query,params=params,fetch=True)
        return applicant_id
     
    def get_areas(self):
        query = self.db.build_select_query(table_name="requisitions.requisition_area",fields=['*'])
        result = self.db.execute_query(query=query,fetch=True)
        return result
     
    def reject_requisition_by_hr(self, requisition_id, responsible_id):
        # Inserta lap_history con id 16 indicando rechazo por gestión humana
        query_insert_lap = "INSERT INTO requisitions.lap_history (requisition_id, requisition_lap_id, responsible_id) VALUES (%s, 16, %s) RETURNING id"
        result_lap = self.db.execute_query(query=query_insert_lap, params=[requisition_id, responsible_id], fetch=True)[0]

        # Actualiza la requisition para establecer requisition_lap_id en 16, indicando rechazo por gestión humana
        query_update_requisition = "UPDATE requisitions.requisition SET requisition_lap_id = 16 WHERE id = %s"
        self.db.execute_query(query=query_update_requisition, params=[requisition_id])

        return {"lap_history_id": result_lap['id']}