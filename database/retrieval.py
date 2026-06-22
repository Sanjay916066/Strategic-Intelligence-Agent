import chromadb
from sentence_transformers import SentenceTransformer
from config import EMBEDDING_MODEL, CHROMA_DB_PATH, COLLECTION_NAME

print("Loading embedding model...")
model = SentenceTransformer(EMBEDDING_MODEL)

print("Connecting to ChromaDB...")
client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
collection = client.get_collection(COLLECTION_NAME)


def search(query, n_results=5):
    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    return results


if __name__ == "__main__":

    query = input("Enter your question: ")

    results = search(query)

    print("\nTop Results:\n")

    for i, doc in enumerate(results["documents"][0], start=1):
        metadata = results["metadatas"][0][i-1]

        print("=" * 60)
        print(f"Result {i}")
        print(f"Title : {metadata['title']}")
        print(f"Source: {metadata['source']}")
        print(f"Link  : {metadata['link']}")
        print()
        print(doc[:500])
        print()