from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from .state import AgentState

def conversation_agent(state: AgentState) -> AgentState:
    # Initialize LLM
    llm = ChatOpenAI(model="gpt-4o", temperature=0.7)
    
    # Construct context from memory
    memories = "\n".join(state.get("retrieved_memories", []))
    
    system_prompt = f"""You are CogniMind AI, a highly advanced personal assistant with persistent memory.
Use the following retrieved memories to personalize your response and maintain context:
<memories>
{memories}
</memories>

Respond intelligently to the user.
"""
    
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=state["input_message"])
    ]
    
    response = llm.invoke(messages)
    
    state["final_response"] = response.content
    state["current_agent"] = "conversation_agent"
    return state
