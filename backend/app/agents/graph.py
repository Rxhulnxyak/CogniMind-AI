from langgraph.graph import StateGraph, END
from .state import AgentState
from .conversation import conversation_agent
from .memory_agent import extract_memory, retrieve_memory

def build_graph():
    workflow = StateGraph(AgentState)
    
    # Add nodes
    workflow.add_node("retrieve_memory", retrieve_memory)
    workflow.add_node("conversation", conversation_agent)
    workflow.add_node("extract_memory", extract_memory)
    
    # Set entry point
    workflow.set_entry_point("retrieve_memory")
    
    # Add edges
    workflow.add_edge("retrieve_memory", "conversation")
    workflow.add_edge("conversation", "extract_memory")
    workflow.add_edge("extract_memory", END)
    
    return workflow.compile()

graph = build_graph()
