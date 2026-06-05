from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    user_id: str

class ChatResponse(BaseModel):
    response: str
    agents_involved: List[str]

@router.post("/", response_model=ChatResponse)
async def chat_with_agent(request: ChatRequest):
    from app.agents.graph import graph
    from app.agents.state import AgentState
    
    initial_state = AgentState(
        user_id=request.user_id,
        input_message=request.message,
        conversation_history=[],
        retrieved_memories=[],
        knowledge_graph_context=[],
        current_agent="",
        reflection="",
        final_response=""
    )
    
    result = graph.invoke(initial_state)
    
    return ChatResponse(
        response=result.get("final_response", "Error generating response."),
        agents_involved=["retrieve_memory", "conversation", "extract_memory"]
    )
