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
nlp = spacy.load("en_core_web_trf")


def preprocess_text(text):
    """
    Preprocess the query text for better matching
    Args:
        text (str): Input query text
    Returns:
        dict: Processed text information
    """
    try:
        # Tokenization
        tokens = word_tokenize(text.lower())

        # Stopword removal
        stop_words = set(stopwords.words("english"))
        filtered_tokens = [word for word in tokens if word not in stop_words]

        # Lemmatization
        lemmatizer = WordNetLemmatizer()
        lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]

        # Named Entity Recognition (NER)
        doc = nlp(text)
        entities = {ent.text: ent.label_ for ent in doc.ents}

        # Extract section numbers if present
        section_numbers = [
            token.text for token in doc 
            if token.like_num and any(
                section in text.lower() 
                for section in ['section', 'bns', 'bharatiya nyaya sanhita']
            )
        ]

        return {
            "processed_text": " ".join(lemmatized_tokens),
            "entities": entities,
            "section_numbers": section_numbers
        }
    except Exception as e:
        print(f"Preprocessing error: {str(e)}")
        return None


if __name__ == "__main__":
    print(preprocess_text("My friend was murdered by someone"))


