"""ChromaDB vectorstore management (placeholder)."""


class VectorStore:
    def __init__(self, persist_dir: str | None = None):
        self.persist_dir = persist_dir

    def add(self, ids, embeddings, metadatas):
        pass

    def query(self, embedding, top_k=5):
        return []
