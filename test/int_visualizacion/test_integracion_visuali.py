import procesar as p1
import pytest
import pytest
from collections import Counter
from wordcloud import WordCloud

@pytest.mark.parametrize("text, expected", [
    ("This code treats each word 15353", "this code treats each word ")
])  
def test_convert_to_lowercase(text, expected):
    text_lowercase = p1.convert_to_lowercase(text)
    assert p1.remove_numbers(text_lowercase) == expected
 