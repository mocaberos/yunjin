from typing import *
from pydantic import BaseModel


class UserID(BaseModel):
    user_id: Optional[str]
