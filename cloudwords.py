from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Texto de entrada
#texto = "La inteligencia artificial es una rama de la informática que busca desarrollar algoritmos, modelos y técnicas que permitan a las máquinas aprender y, en consecuencia, realizar tareas que normalmente requerirían de la inteligencia humana. Estas tareas incluyen el reconocimiento de voz, el aprendizaje, la planificación y el razonamiento, entre otras."
texto = "Mi mi mi do re fa mi"
# Crear la nube de palabras
if isinstance(texto, str):
    wordcloud = WordCloud(width = 800, height = 800, # ancho y alto de la nube de palabras
                background_color ='white', 
                stopwords = None, 
                min_font_size = 10).generate(texto)
    print(wordcloud)

print(type(wordcloud))
# Mostrar la nube de palabras
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 

plt.show()
