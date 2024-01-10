from procesamiento.procesamiento_texto import *
# llamamos a la clase
texto = "This code, treats each word"
print("texto:", texto, len(texto))
clase1 = TextPreprocessor(remove_links=True, 
                                remove_hastags=True,
                                remove_characters=True, 
                                convert_to_lowercase=True, 
                                remove_emojis=True,
                                remove_numbers=True,
                                remove_stopwords_flag= True)
# lematizacion
doc_lema = clase1.lematizacion_text(texto)
print("doc_lema:\n",doc_lema)

# stemming
doc_stem = clase1.stemming_text(texto)
print("doc_stem:\n",doc_stem)
#remove characters
# doc_remove = clase1.remove_characters("This is an example/()=?")
# print("doc_remove caracteres:\n",doc_remove)

""" # remove stopwords
doc_stopwords = clase1.remove_stopwords(texto)
print("doc_stopwords:\n", doc_stopwords)

# convert to lowercase
doc_lowercase = clase1.convert_to_lowercase(texto)
print("doc_lowercase:\n", doc_lowercase) """

""" # remove emojis
doc_emojis = clase1.remove_emojis(texto)
print("doc_emojis:\n", doc_emojis)

# remove extra spaces
doc_extra_spaces = clase1.remove_extra_spaces(texto)
print("doc_extra_spaces:\n", doc_extra_spaces)
 """
""" # remove numbers
doc_numbers = clase1.remove_numbers(texto)
print("doc_numbers:\n", doc_numbers)

# remove emails
doc_emails = clase1.remove_emails(texto)
print("doc_emails:\n", doc_emails)

# remove hastags
doc_hastags = clase1.remove_hastags(texto)
print("doc_hastags:\n", doc_hastags)

# remove links
doc_links = clase1.remove_links(texto)
print("doc_links:\n", doc_links)
 """