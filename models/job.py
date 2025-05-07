from pydantic import BaseModel

class Job(BaseModel):
    id: str
    name : str
    main_activity : str
    prerequisites : str
    differentials : str