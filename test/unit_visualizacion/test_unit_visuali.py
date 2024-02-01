#import practica1 as p1
import procesar as p1
import pytest
import pytest
from collections import Counter
from wordcloud import WordCloud

@pytest.mark.parametrize("input_text", [
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    "Python is a powerful programming language.",
    "Testing with pytest is fun!"
])
def test_cloud_words(input_text):
    # Llama a la función cloud_words con diferentes textos
    result = p1.cloud_words(input_text)
    # Verifica que el resultado sea una instancia de Counter
    assert isinstance(result, WordCloud)

def test_cloud_words_with_valid_input():
    # Caso válido (cadena de texto)
    valid_text = "texto creado para la realizacion del test."
    result = p1.cloud_words(valid_text)
    assert result is not None

def test_cloud_words_with_invalid_input():
    # Caso inválido (no es una cadena)
    with pytest.raises(ValueError, match="Error en cloud_words: La entrada debe ser una cadena."):
        invalid_text = [1, 2, 3]  # Es una lista, no una cadena
        p1.cloud_words(invalid_text)

def test_frecuencia_words():
    # Caso válido (cadena de texto)
    valid_text = "texte creado para la realizacion del test."
    result = p1.frec_words(valid_text)
    assert result is not None
def test_frecuencia_words_with_valid_input():
    # Caso válido (cadena de texto)
    valid_text = "texto creado para la realizacion del test."
    result = p1.frec_words(valid_text)
    assert isinstance(result, Counter)

def test_frecuencia_words_with_invalid_input():
    # Caso inválido (no es una cadena)
    with pytest.raises(ValueError, match="Error en frec_words: La entrada debe ser una cadena."):
        invalid_text = [1, 2, 3]  # Es una lista, no una cadena
        p1.frec_words(invalid_text)
