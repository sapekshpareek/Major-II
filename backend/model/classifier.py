import torch
from transformers import pipeline

# Check if GPU is available
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load BERT classifier with GPU support
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli", device=0 if torch.cuda.is_available() else -1)

LEGAL_CATEGORIES = ["Murder Case", "FIR Filing", "Property Dispute", "Divorce", "Theft Case"]

def classify_intent(query):
    result = classifier(query, LEGAL_CATEGORIES)
    return result

if __name__ == "__main__":
    print(classify_intent("My friend was murdered. What should I do?"))
