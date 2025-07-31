# modules/memory.py

import chromadb
from sentence_transformers import SentenceTransformer
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)

# === Setup ChromaDB and embedding model ===
client = chromadb.PersistentClient(path="./chroma_store")
collection = client.get_or_create_collection(name="everest_db_1")
embedder = SentenceTransformer('all-MiniLM-L6-v2')

def embed(text: str) -> list:
    return embedder.encode([text])[0].tolist()

def store_memory(role: str, text: str):
    doc_id = f"{role}_{abs(hash(text)) % (10 ** 12)}"  # unique ID
    collection.add(
        documents=[text],
        embeddings=[embed(text)],
        ids=[doc_id]
    )

def retrieve_memory(query: str, n_results: int = 5) -> list:
    query_embedding = embed(query)
    results = collection.query(query_embeddings=[query_embedding], n_results=n_results)
    return results['documents'][0] if results['documents'] else []
