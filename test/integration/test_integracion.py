#import practica1 as p1
import procesar as p1
import pytest
from wordcloud import WordCloud
from collections import Counter

@pytest.mark.parametrize("text, expected", [
    ("This code treats each word 15353", WordCloud)
])  
def test_convert_to_lowercase(text, expected):
    text_lowercase = p1.convert_to_lowercase(text)
    result = p1.cloud_words(text_lowercase)
    assert isinstance(result, expected)

@pytest.mark.parametrize("text, expected", [
    ("This code treats each word 15353", Counter)
])  
def test_convert_to_lowercase(text, expected):
    text_lowercase = p1.convert_to_lowercase(text)
    result = p1.frec_words(text_lowercase)
    assert isinstance(result, expected)
    