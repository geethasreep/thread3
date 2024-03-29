import streamlit as st
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from PIL import Image
import re
import string
import nltk
import spacy

import streamlit as st#used to create web application with simple python code
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

from PIL import Image

with open("svm_model.pkl","rb") as file:
  model=pickle.load(file)

with open("tfidf_vectorizer.pkl", "rb") as file:
    vectorizer = pickle.load(file)

nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('english')

def clean_text(text):
    text = text.lower()
    return text.strip()

def remove_punctuation(text):
    punctuation_free = "".join([i for i in text if i not in string.punctuation])
    return punctuation_free

def tokenization(text):
    tokens = re.split(' ', text)
    return tokens

def remove_stopwords(text):
    output = " ".join(i for i in text if i not in stopwords)
    return output

def lemmatizer(text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    sent = [token.lemma_ for token in doc if not token.text in set(stopwords)]
    return ' '.join(sent)

st.title("Sentiment Analysis App")
st.markdown("Geethasree")
image = Image.open("sentiment.jpeg")
st.image(image, use_column_width=True)

st.subheader("Enter your text here:")
user_input = st.text_area("")

if user_input:
    user_input = clean_text(user_input)
    user_input = remove_punctuation(user_input)
    user_input = user_input.lower()
    user_input = tokenization(user_input)
    user_input = remove_stopwords(user_input)
    user_input = lemmatizer(user_input)

if st.button("Predict"):
    if user_input:
        text_vectorized = vectorizer.transform([user_input])
        prediction = model.predict(text_vectorized)[0]
        st.header("Prediction:")
        if prediction == -1:
            st.subheader("The sentiment of the given text is: Negative")
        elif prediction == 0:
            st.subheader("The sentiment of the given text is: Neutral")
        elif prediction == 1:
            st.subheader("The sentiment of the given text is: Positive")
    else:
        st.subheader("Please enter a text for prediction.")
import streamlit as st
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from PIL import Image
import re
import string
import nltk
import spacy
import sklearn
import joblib

# Check the version of Streamlit
print(f"Streamlit version: {st.__version__}")

# Check the version of PIL (Pillow)
pillow_version = Image.__version__
print(f"Pillow version: {pillow_version}")

# Check the version of re (regular expressions)
print(f"Python re (regular expressions) version: {re.__version__}")

# Check the version of NLTK (Natural Language Toolkit)
nltk_version = nltk.__version__
print(f"NLTK version: {nltk_version}")

# Check the version of spaCy
spacy_version = spacy.__version__
print(f"spaCy version: {spacy_version}")
# Check the version of scikit-learn
sklearn_version = sklearn.__version__
print(f"scikit-learn version: {sklearn_version}")

# Check the version of joblib
joblib_version = joblib.__version__
print(f"joblib version: {joblib_version}")

