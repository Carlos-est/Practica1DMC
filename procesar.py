import re 
from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer
import spacy
from spacy.lang.es.stop_words import STOP_WORDS

def lematizacion_text(text):
    nlp = spacy.load("en_core_web_sm")
    text = nlp(text)
    doc_lematizacion = [token.lemma_.strip() for token in text if token.lemma_.strip()]
    result = ' '.join(doc_lematizacion)
    return result
def stemming_text(text):
    nlp = spacy.load("en_core_web_sm")
    text = nlp(text)
    stemmer = SnowballStemmer("english")
    doc_stemming = [stemmer.stem(token.text) for token in text]
    result = ' '.join(doc_stemming)
    return result

def remove_characters(text):
    if isinstance(text, str):
        return re.sub(r'[^\w\s]', '', text)
    else:
        return text

def remove_stopwords(text):
    if isinstance(text, list):
        stop_words = set(stopwords.words('english'))
        return ' '.join([word for word in text if word.lower() not in stop_words])

def convert_to_lowercase(text):
    if isinstance(text, str):
        return text.lower()

def remove_emojis(text):
    if isinstance(text, str):
        emoji_pattern = re.compile("["
                                    u"\U0001F600-\U0001F64F"  
                                    u"\U0001F300-\U0001F5FF"  
                                    u"\U0001F680-\U0001F6FF"  
                                    u"\U0001F1E0-\U0001F1FF"  
                                    "]+", flags=re.UNICODE)
        return emoji_pattern.sub(r'', text)

def remove_extra_spaces(text):
    if isinstance(text, str):
        return re.sub(r'\s+', ' ', text).strip()

def remove_numbers(text):
    if isinstance(text, str):
        return re.sub(r'\d+', '', text)

def remove_users(text):
    if isinstance(text, str):
        return re.sub(r'@\S+', '', text)

def remove_hastags(text):
    if isinstance(text, str):
        return re.sub(r'#\S+', '', text)

def remove_links(text):
    if isinstance(text, str):
        return re.sub(r'http\S+', '', text)

def tokenize_text(text):
    return word_tokenize(text)

# def preprocess_text(text):
#     if text_lematizacion:
#         text = lematizacion_text(text)
#     if text_stemming:
#         text = stemming_text(text)
#     if remove_links_flag:
#         text = remove_links(text)
#     if remove_hastags_flag:
#         text = remove_hastags(text)
#     if remove_characters_flag:
#         text = remove_characters(text)
#     if remove_stopwords_flag:
#         text = remove_stopwords(text.split())
#     if convert_to_lowercase_flag:
#         text = convert_to_lowercase(text)
#     if remove_emojis_flag:
#         text = remove_emojis(text)
#     if remove_numbers_flag:
#         text = remove_numbers(text)
#     return text


