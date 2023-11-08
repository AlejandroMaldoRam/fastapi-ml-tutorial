# Script to define the data schema for validation using pydantic
from pydantic import BaseModel

class TitanicPassenger(BaseModel):
    Age: int
    Sex: str
    Embarked: str