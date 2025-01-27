from fastapi import APIRouter
from models.neigborhoods.neigborhoods import Neigborhoods


neiborhoods_route = APIRouter()



@neiborhoods_route.get('/get-neigborhoods-report/', tags = ['neigborhoods'])
def get_neigborhoods():
    neigborhood_instance = Neigborhoods()
    result = neigborhood_instance.get_neiborhoods_report()
    return result[0] if result else []
