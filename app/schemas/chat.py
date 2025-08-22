from pydantic import BaseModel
from typing import List, Optional

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[ChatMessage]
    model: str = "orionix-coder"
    temperature: Optional[float] = 0.7
    max_tokens: Optional[int] = 1000
