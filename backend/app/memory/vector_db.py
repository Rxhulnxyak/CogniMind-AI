from pinecone import Pinecone
from app.core.config import settings

pc = Pinecone(api_key=settings.PINECONE_API_KEY) if settings.PINECONE_API_KEY else None

def get_pinecone_index(index_name: str = "cognimind-memory"):
    if pc is None:
        return None
    return pc.Index(index_name)

def store_memory_vector(user_id: str, memory_id: str, vector: list, metadata: dict):
    index = get_pinecone_index()
    if index:
        index.upsert(vectors=[{"id": memory_id, "values": vector, "metadata": metadata}])
        return True
    return False

def query_memory_vector(user_id: str, query_vector: list, top_k: int = 5):
    index = get_pinecone_index()
    if index:
        return index.query(vector=query_vector, top_k=top_k, filter={"user_id": user_id}, include_metadata=True)
    return {"matches": []}
