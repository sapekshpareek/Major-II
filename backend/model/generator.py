import torch
from transformers import pipeline

device = "cuda" if torch.cuda.is_available() else "cpu"

# Load GPT-2 model on GPU
generator = pipeline("text-generation", model="gpt2", device=0 if torch.cuda.is_available() else -1)

def generate_response(query):
    response = generator(query, max_length=50, num_return_sequences=1)
    return response[0]["generated_text"]

if __name__ == "__main__":
    print(generate_response("My friend was murdered. What should I do?"))
