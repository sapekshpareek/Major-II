import torch
from transformers import pipeline

torch.cuda.empty_cache()

# Check if GPU is available
device = 0 if torch.cuda.is_available() else -1  # Use GPU only if available
print(f"Using device: {'GPU' if device == 0 else 'CPU'}")  # Debugging


# Load BERT classifier with GPU support
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli", device=0 if torch.cuda.is_available() else -1)

LEGAL_CATEGORIES = ["Murder Case", "FIR Filing", "Property Dispute", "Divorce", "Theft Case"]

def classify_intent(query):
    result = classifier(query, LEGAL_CATEGORIES)
    return result

if __name__ == "__main__":
    print(classify_intent("Someone stole my television from my house"))
