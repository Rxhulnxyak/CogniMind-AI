from typing import TypedDict, Annotated, List, Dict, Any
import operator

class AgentState(TypedDict):
    user_id: str
    input_message: str
    conversation_history: List[Dict[str, str]]
    retrieved_memories: List[str]
    knowledge_graph_context: List[str]
    current_agent: str
    reflection: str
    final_response: str
