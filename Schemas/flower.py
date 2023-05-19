import datetime
from pydantic import BaseModel, Field
from typing import Optional



class Iris(BaseModel):
    id: Optional[int] = None 
    sepalLength: float = Field(ge=0, le=7)
    sepalWidth: float = Field(ge=0, le=7)
    petalLength: float = Field(ge=0, le=7)
    petalWidth: float = Field(ge=0, le=7)
 
    
    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "sepalLength": 5.1,
                "sepalWidth": 3.5,
                "petalLength": 1.4,
                "petalWidth": 0.2,
            }
        }
        exclude = ['id']
    