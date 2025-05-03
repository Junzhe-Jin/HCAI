# backend/app/models/prompt_schema.py

from pydantic import BaseModel
from typing import List, Dict, Optional

class PromptRequest(BaseModel):
    prompt: str
    api_key: str
    # 🔥 新增这一行，给 create_answer 一个默认值
    create_answer: bool = False

class TokenInfo(BaseModel):
    index: int
    text: str
    pos: str
    dep: str
    head: str

class AnalyzeResponse(BaseModel):
    tokens: List[TokenInfo]
    scores: Dict[str, int]
    reason: Dict[str, str]
    suggestions: List[str]
    # 🔥 后端返回时可能会有 model_response
    model_response: Optional[str] = None


