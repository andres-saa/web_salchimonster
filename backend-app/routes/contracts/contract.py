from fastapi import APIRouter
from models.contracts.contract import Contract
from schema.contracts.contract import EmployerContractPost,contract_type,soft_delete,days_to_alert
from models.contracts.contract_types import ContractTypes
contract_router = APIRouter()


@contract_router.get('/get-all-contracts', tags=['contract => contract'])
def get_all_contract():
    contrat_instance = Contract()
    return contrat_instance.get_all_contracts()



@contract_router.get('/get-all-vigent-contracts', tags=['contract => contract'])
def get_all_contract():
    contrat_instance = Contract()
    return contrat_instance.get_all_vigent_contracts()


@contract_router.get('/get-all-to-finish-contracts', tags=['contract => contract'])
def get_all_contract():
    contrat_instance = Contract()
    return contrat_instance.get_all_contracts_to_finish()

@contract_router.get('/get-all-finished-contracts', tags=['contract => contract'])
def get_all_contract():
    contrat_instance = Contract()
    return contrat_instance.get_all_finished_contracts()



@contract_router.get('/get-all-future-contracts', tags=['contract => contract'])
def get_all_contract():
    contrat_instance = Contract()
    return contrat_instance.get_all_future_contracts()








@contract_router.get('/get-all-contract-types', tags=['contract => types'])
def get_all_contract():
    contrat_instance = ContractTypes()
    return contrat_instance.get_all_contract_types()


@contract_router.get('/get-days-to-alert', tags=['contract => types'])
def get_all_contract():
    contrat_instance = ContractTypes()
    return contrat_instance.get_days_to_alert()

@contract_router.put('/update-contract-type/{id}', tags=['contract => types'])
def get_all_contract(id:int, data:contract_type):
    contrat_instance = ContractTypes()
    return contrat_instance.update_contract_type(id,data)


@contract_router.post('/insert-contract-type', tags=['contract => types'])
def get_all_contract(data:contract_type):
    contrat_instance = ContractTypes()
    return contrat_instance.insert_contract_type(data)

@contract_router.put('/update-contract-days-to-alert/{id}', tags=['contract => types'])
def get_all_contract(id:int, data:days_to_alert):
    contrat_instance = ContractTypes()
    return contrat_instance.update_days_to_alert(id,data)


@contract_router.delete('/delete-contract-type/{id}', tags=['contract => types'])
def get_all_contract(id:int):
    contrat_instance = ContractTypes()
    return contrat_instance.soft_delete_contract_type(id,soft_delete(exist=False))


@contract_router.get('/get-all-contracts-by-contract-id/{contract_id}', tags=['contract => contract'])
def get_all_contract(contract_id:int):
    contrat_instance = Contract()
    return contrat_instance.get_all_contracts_by_employer_id(contract_id)



@contract_router.post('/create-new-contract/', tags=['contract => contract'])
def create_contract(data:EmployerContractPost):
    contrat_instance = Contract()
    return contrat_instance.create_new_contract(data)



@contract_router.delete('/delete-contract/{contract_id}', tags=['contract => contract'])
def create_contract(contract_id:int):
    contrat_instance = Contract()
    return contrat_instance.soft_delete_contract(contract_id)[0]