from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Dict

router = APIRouter()

class GraphNode(BaseModel):
    id: str
    label: str
    properties: Dict[str, str]

class GraphEdge(BaseModel):
    source: str
    target: str
    relationship: str

class KnowledgeGraphResponse(BaseModel):
    nodes: List[GraphNode]
    edges: List[GraphEdge]

@router.get("/{user_id}", response_model=KnowledgeGraphResponse)
async def get_knowledge_graph(user_id: str):
    # TODO: Connect to Neo4j
    return KnowledgeGraphResponse(nodes=[], edges=[])
