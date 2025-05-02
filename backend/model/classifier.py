import torch
from transformers import pipeline

torch.cuda.empty_cache()

# Check if GPU is available
device = 0 if torch.cuda.is_available() else -1

# Load BERT classifier with GPU support
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli", device=device)

# Update categories to match BNS sections
LEGAL_CATEGORIES = [
    "Murder and Homicide",
    "Theft and Property Crime",
    "Fraud and Cheating",
    "Sexual Offences",
    "Public Order Offences",
    "Cyber Crime",
    "Economic Offences"
]

def classify_intent(query):
    """
    Classify the legal query into relevant categories
    Args:
        query (str): User's query text
    Returns:
        dict: Classification results with scores
    """
    try:
        result = classifier(query, LEGAL_CATEGORIES)
        return {
            'category': result['labels'][0],
            'confidence': result['scores'][0],
            'all_categories': dict(zip(result['labels'], result['scores']))
        }
    except Exception as e:
        print(f"Classification error: {str(e)}")
        return None

if __name__ == "__main__":
    print(classify_intent("Someone stole my television from my house"))
