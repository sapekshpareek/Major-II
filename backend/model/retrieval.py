import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load Sentence Transformer Model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Sample legal documents
LEGAL_TEXTS = [
    "IPC 302 states that murder is punishable by death or life imprisonment.",
    "FIR must be filed at the nearest police station immediately after a crime.",
    "IPC 307 covers attempt to murder with up to 10 years of imprisonment.",
]

# Convert text to embeddings
LEGAL_EMBEDDINGS = np.array([model.encode(text) for text in LEGAL_TEXTS])

# Create FAISS index
index = faiss.IndexFlatL2(LEGAL_EMBEDDINGS.shape[1])
index.add(LEGAL_EMBEDDINGS)

def search_legal_text(query, top_k=1):
    query_embedding = model.encode(query).reshape(1, -1)
    distances, indices = index.search(query_embedding, top_k)
    return [(LEGAL_TEXTS[i], distances[0][idx]) for idx, i in enumerate(indices[0])]

if __name__ == "__main__":
    print(search_legal_text("What is the punishment for Killing someone?"))
