# TextPreprocessor

## Overview
The TextPreprocessor is a Python class designed for comprehensive text preprocessing.
This library can perform the following tasks:
```
1. Text lematization    --> text_lematizacion()
2. Text stemming        --> text_stemming()
3. Remove links         --> remove_links()
4. Remove hastags       --> remove_hastags()
5. Remove characters    --> remove_characters()
6. Convert to lowercase --> convert_to_lowercase()
7. Remove emojis        --> remove_emojis()
8. Remove numbers       --> remove_numbers()
9. Remove stopwords     --> remove_stopwords()
10. Cloud words         --> cloudwords()
11. Frequency words     --> frecwords()
```

## Installation
Ensure you have NLTK installed. You can install NLTK via pip:

pip install nltk




## Usage
```python
### Import the TextPreprocessor class
from text_preprocessor import TextPreprocessor
# Initialize the preprocessor with default settings
preprocessor = TextPreprocessor()

# Customize the preprocessor by setting flags
preprocessor = TextPreprocessor(
    text_lematizacion_flag =True, 
    text_stemming_flag=True, 
    remove_links=True, 
    remove_hastags=True,
    remove_characters=True,
    convert_to_lowercase=True, 
    remove_emojis=True, 
    remove_numbers=True,
    remove_stopwords_flag= True, 
    cloudwords =True,
    frecwords = True
)


text = "Your text goes here..."
processed_text = preprocessor.preprocess_text(text)

```
## Available Methods
1. preprocess_text(text): Preprocesses the input text based on the initialized flags.
2. Other methods in the class can be used individually for specific preprocessing steps (e.g., remove_links, remove_stopwords, etc.).
# Examples
```python

text = "Hello! This is an example text with #hashtags and links: https://example.com"
# Initialize preprocessor
preprocessor = TextPreprocessor(remove_links=True, remove_hashtags=True)

# Preprocess text
processed_text = preprocessor.preprocess_text(text)
print(processed_text)
Output: "Hello This is an example text with and links"

```
```python

texto = "If you need to tokenize the text before removing stopwords, you might want to incorporate a tokenization function such as word_tokenize from NLTK."
# lematizacion
p1 = pt.TextPreprocessor()
doc = p1.lematizacion_text(texto)
Output: "if you need to tokenize the text before remove stopword , you might want to incorporate a tokenization function such as word_tokenize from NLTK ."

```
```python

texto = "If you need to tokenize the text before removing stopwords, you might want to incorporate a tokenization function such as word_tokenize from NLTK."
# stemming
p1 = pt.TextPreprocessor()
doc = p1.stemming_text(texto)
Output: "if you need to token the text befor remov stopword , you might want to incorpor a token function such as word_token from nltk ."
```
# License

This project is licensed under the MIT License - see the LICENSE file for details.



