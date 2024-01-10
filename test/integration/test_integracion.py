#import practica1 as p1
import procesar as p1
import pytest
import pytest

@pytest.mark.parametrize("text, expected", [
    ("This code treats each word 15353", "this code treats each word ")
])  
def test_convert_to_lowercase(text, expected):
    text_lowercase = p1.convert_to_lowercase(text)
    assert p1.remove_numbers(text_lowercase) == expected
 
@pytest.mark.parametrize(
    "text, expected",
    [
        ("#Variables http://example.com dos", "  dos"),
        ("Variables de prueba #3455 http://example.com", "Variables de prueba  ")
    ],
)
def test_remove_hashtags_and_links(text, expected):
    processed_text = p1.remove_links(text)
    assert p1.remove_hastags(processed_text) == expected
    
    