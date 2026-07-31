from sklearn.feature_extraction.text import TfidfVectorizer
from utils import clean_text

def extract_keywords(text, num_keywords=5):
    text = clean_text(text)

    vectorizer = TfidfVectorizer(max_features=num_keywords)
    X = vectorizer.fit_transform([text])

    keywords = vectorizer.get_feature_names_out()
    return list(keywords)