import faiss
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer

# Load Sentence Transformer Model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load BNS Dataset
def load_bns_data():
    df = pd.read_csv('../../data/BNS_Dataset.csv')
    # Create comprehensive text representation for each section
    df['full_text'] = df.apply(lambda row: f"""
        BNS Section {row['Section Number']}: {row['Name']}
        Description: {row['Description']}
        Offence: {row['Offence']}
        Punishment: {row['Punishment']}
        Cognizable: {row['Cognizable']}
        Bailable: {row['Bailable']}
        Court Level: {row['Court Level']}
    """, axis=1)
    return df

# Initialize data and create embeddings
df = load_bns_data()
LEGAL_TEXTS = df['full_text'].tolist()
LEGAL_EMBEDDINGS = np.array([model.encode(text) for text in LEGAL_TEXTS])

# Create FAISS index
index = faiss.IndexFlatL2(LEGAL_EMBEDDINGS.shape[1])
index.add(LEGAL_EMBEDDINGS)

def search_legal_text(query, top_k=3):
    """
    Search for relevant BNS sections based on the query
    Args:
        query (str): User's query text
        top_k (int): Number of results to return
    Returns:
        list: List of tuples containing (section_info, similarity_score)
    """
    query_embedding = model.encode(query).reshape(1, -1)
    distances, indices = index.search(query_embedding, top_k)
    results = []
    for idx, i in enumerate(indices[0]):
        section_info = {
            'section_number': df.iloc[i]['Section Number'],
            'name': df.iloc[i]['Name'],
            'description': df.iloc[i]['Description'],
            'punishment': df.iloc[i]['Punishment'],
            'bailable': df.iloc[i]['Bailable'],
            'cognizable': df.iloc[i]['Cognizable'],
            'court_level': df.iloc[i]['Court Level'],
            'similarity_score': float(1 / (1 + distances[0][idx]))
        }
        results.append(section_info)
    return results

if __name__ == "__main__":
    # Test cases
    test_queries = [
        "My friend was murdered",
    ]
    
    for query in test_queries:
        print(f"\nQuery: {query}")
        results = search_legal_text(query)
        for result in results:
            print(f"\nSection {result['section_number']}: {result['name']}")
            print(f"Description: {result['description']}")
            print(f"Punishment: {result['punishment']}")
            print(f"Bailable: {result['bailable']}")
            print(f"Cognizable: {result['cognizable']}")
            print(f"Court Level: {result['court_level']}")
            print(f"Similarity Score: {result['similarity_score']:.2f}")
