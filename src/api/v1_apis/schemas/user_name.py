from typing import *
from pydantic import BaseModel


class UserName(BaseModel):
    user_name: Optional[str]
