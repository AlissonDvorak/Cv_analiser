from pydantic import BaseModel
from typing import List

class analysis(BaseModel):
    id: str
    job_id: str
    name: str
    resum_id: str
    skills : List[str]
    education : List[str]
    languages : List[str]
    score : float