from datetime import datetime
from pydantic import BaseModel, validator

class ConnectivityLogSchema(BaseModel):
    # log_id: int
    site_id: int
    # event_timestamp: datetime
    event_type: str