from typing import Optional
from pydantic import BaseModel
from datetime import datetime



class Video(BaseModel):
    id:Optional[int] = None
    name:str
    exist:bool
    index:int
    created_at:datetime
    created_by:int
    link:str
    description:str


class VideoPost(BaseModel):
    name:str
    description:str
    created_by:int
    link:str
    sequence_id:int



class VideoUpdate(BaseModel):
    name:str
    description:str
    link:str


class markVideo(BaseModel):
    user_id:int
    video_id:int