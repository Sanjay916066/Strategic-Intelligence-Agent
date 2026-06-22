import pandas as pd
import chromadb
from sentence_transformers import SentenceTransformer
from config import EMBEDDING_MODEL, CHROMA_DB_PATH, COLLECTION_NAME

print("Loading embedding model...")

model = SentenceTransformer(EMBEDDING_MODEL)

print("Connecting to ChromaDB...")

client = chromadb.PersistentClient(path=CHROMA_DB_PATH)

collection = client.get_or_create_collection(
    name=COLLECTION_NAME
)

print("Loading chunks...")

df = pd.read_csv("data/processed/chunks.csv")

print(f"Found {len(df)} chunks")

# Optional: clear old data
try:
    client.delete_collection(COLLECTION_NAME)
except Exception:
    pass

collection = client.get_or_create_collection(name=COLLECTION_NAME)

for idx, row in df.iterrows():

    embedding = model.encode(row["text"]).tolist()

    collection.add(
        ids=[str(idx)],
        documents=[row["text"]],
        embeddings=[embedding],
        metadatas=[{
            "title": row["title"],
            "source": row["source"],
            "link": row["link"]
        }]
    )

print("\nEmbedding complete!")
print(f"Stored {collection.count()} documents in ChromaDB")