from typing import List, Dict, Any, Optional
from pydantic import BaseModel

class ContentState(BaseModel):
    query: str = ""
    content_type: str = ""
    search_results: List[Dict] = []
    verified_sources: List[Dict] = []
    content_plan: Dict = {}
    generated_content: Dict = {}
    visuals: List[Dict] = []
    template: str = ""
    final_output: Dict = {}
    retry_count: int = 0
    quality_score: float = 0.0 