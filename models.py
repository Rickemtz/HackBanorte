from pydantic import BaseModel

class UserData(BaseModel):
    income: float
    debts: float
    savings: float
    risk_level: str
    investment_duration: int
