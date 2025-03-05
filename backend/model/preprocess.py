import spacy
# import nltk
# nltk.download("punkt")        # For Tokenization
# nltk.download("stopwords")    # For Stopword Removal
# nltk.download("wordnet")      # For Lemmatization
# nltk.download('omw-1.4')      # Optional for lemmatization
# nltk.download('punkt_tab')


from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    # Tokenization
    tokens = word_tokenize(text)
    
    # Stopword removal
    stop_words = set(stopwords.words("english"))
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
    
    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]
    
    # Named Entity Recognition (NER)
    doc = nlp(text)
    entities = {ent.text: ent.label_ for ent in doc.ents}
    
    return {"tokens": lemmatized_tokens, "entities": entities}

if __name__ == "__main__":
    print(preprocess_text("My friend was murdered in Delhi under IPC 302."))
