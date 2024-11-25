from pydantic import BaseModel

class User(BaseModel):
    name: str
    email_id: str
    password: str 


class EmailAndPassword(BaseModel):
    email: str
    password: str 
