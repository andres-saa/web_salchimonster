from pydantic import BaseModel, constr, conint, condecimal
from typing import Optional
from datetime import date, datetime







class EmployerContractPost ( BaseModel):

     employer_id:int
     contract_type_id:int
     start_date:datetime
     end_date:datetime
     created_by:int
     alert_date:datetime
     Salary:float






class EmployerContract ( EmployerContractPost):
     id:Optional[int] = None
     active:bool
     exist:bool



class contract_type(BaseModel):
     name:str
     description:str



class soft_delete (BaseModel):
     exist:bool = False


class days_to_alert (BaseModel):
     days:int