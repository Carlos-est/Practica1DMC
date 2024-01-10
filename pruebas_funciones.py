from procesar import *
texto = "THE SOFTWARE IS PROVIDED AS IS"

doc_lematizado = lematizacion_text(texto)
print(doc_lematizado)

# steming
doc_stemming = stemming_text(texto)
print(doc_stemming)

#stopwords
doc_stopwords = remove_stopwords(['This', 'code', 'treats', 'each', 'word'])
print(doc_stopwords)

#lowercase
doc_lowercase = convert_to_lowercase(texto)
print(doc_lowercase)
# emojis
texto = "This code treats each word😂😂😂"
doc_emojis = remove_emojis(texto)
print(doc_emojis)
# 
# remove links
texto = "Variables de prueba #3455 http://example.com"
doc_links = remove_links(texto)
print(doc_links)
# remove hastags
doc_hastags = remove_hastags(doc_links)
print("doc_hastags:", doc_hastags)