from .state import AgentState

def retrieve_memory(state: AgentState) -> AgentState:
    # TODO: Connect to Pinecone/Neo4j to retrieve relevant memories based on input_message
    
    # Mock retrieval
    state["retrieved_memories"] = [
        "User is interested in AI and Cloud Computing.",
        "User is building a final-year project named CogniMind AI."
    ]
    return state

def extract_memory(state: AgentState) -> AgentState:
    # TODO: Use LLM to extract new memories from the input_message and final_response
    # Then save to vector db / neo4j
    
    return state
