from pydantic import BaseModel

class CreateCheckoutSession(BaseModel):
    package_name: str
    success_url: str
    cancel_url: str
