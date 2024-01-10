#import practica1 as p1
import procesar as p1
import pytest


@pytest.mark.parametrize("text, expected", [
    ("This code, treats each word", "this code , treat each word")
])
def test_lematizacion_text(text, expected):
    assert p1.lematizacion_text(text) == expected

@pytest.mark.parametrize("text, expected", 
    [
        ("()#Primer comentario", "Primer comentario"),
        ("Codigo () de prueba/", "Codigo  de prueba"),
    ])
def test_remove_characters(text, expected):
    assert p1.remove_characters(text) == expected

@pytest.mark.parametrize("text, expected",
                         [
                             (['This', 'code', 'treats', 'each', 'word'],'code treats word'),
                         ])
def test_stopwords(text, expected):
    assert p1.remove_stopwords(text) == expected

## lowercase
@pytest.mark.parametrize("text, expected",
                         [
                             ("THE SOFTWARE IS PROVIDED AS IS", "the software is provided as is"),
                             ("This code, treats each word", "this code, treats each word"),
                             ("Cars", "cars")
                         ])
def test_convert_to_lowercase(text, expected):
    assert p1.convert_to_lowercase(text) == expected

## remove emojis
@pytest.mark.parametrize("text, expected",
                         [
                             ("This code treats each word😂😂😂", "This code treats each word"),
                             ("Cars😂😂😂", "Cars")
                         ])
def test_remove_emojis(text, expected):
    assert p1.remove_emojis(text) == expected

# remove extra spaces
@pytest.mark.parametrize("text, expected",
                         [
                             ("This code treats each word", "This code treats each word"),
                             ("This code  treats each word", "This code treats each word"),
                             ("This code   treats each word", "This code treats each word"),
                             ("This code    treats each word", "This code treats each word")
                         ])
def test_remove_extra_spaces(text, expected):
    assert p1.remove_extra_spaces(text) == expected

# remove numbers
@pytest.mark.parametrize("text, expected",
                         [
                             ("This code treats each word", "This code treats each word"),
                             ("This code treats each word 123", "This code treats each word "),
                             ("This code treats each word 123 456", "This code treats each word  "),
                             ("This code treats each word 123 456 789", "This code treats each word   ")
                         ])
def test_remove_numbers(text, expected):
    assert p1.remove_numbers(text) == expected

# remove_users
@pytest.mark.parametrize("text, expected",
                         [
                             ("This code treats each word", "This code treats each word"),
                             ("This code treats each word @user", "This code treats each word "),
                             ("This code treats each word @user @user2", "This code treats each word  "),
                             ("This code treats each word @user @user2 @user3", "This code treats each word   ")
                         ])
def test_remove_users(text, expected):
    assert p1.remove_users(text) == expected

# remove_hastags
@pytest.mark.parametrize("text, expected",
                         [
                             ("This code treats each word", "This code treats each word"),
                             ("This code treats each word #hashtag", "This code treats each word "),
                             ("This code treats each word #hashtag #hashtag2", "This code treats each word  "),
                             ("This code treats each word #hashtag #hashtag2 #hashtag3", "This code treats each word   ")
                         ])
def test_remove_hastags(text, expected):
    assert p1.remove_hastags(text) == expected

# remove_links
@pytest.mark.parametrize("text, expected",
                         [
                             ("This code treats each word", "This code treats each word"),
                             ("This code treats each word http://www.google.com", "This code treats each word "),
                             ("This code treats each word http://www.google.com http://www.google.com", "This code treats each word  "),
                             ("This code treats each word http://www.google.com http://www.google.com http://www.google.com", "This code treats each word   ")
                         ])
def test_remove_links(text, expected):
    assert p1.remove_links(text) == expected








