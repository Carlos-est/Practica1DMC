import pandas as pd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from collections import Counter
import re
class DataVisualization:
    def __init__(self, text):
        self.text = text

    def cloud_words(self, text):
        wordcloud = WordCloud(width = 800, height = 800, # ancho y alto de la nube de palabras
                    background_color ='white', 
                    stopwords = None, 
                    min_font_size = 10).generate(text)
        plt.figure(figsize = (8, 8), facecolor = None) #definimos tamaño y el color de fondo 
        plt.imshow(wordcloud) #mostramos la imagen
        plt.axis("off") # desactivamos los ejes
        plt.tight_layout(pad = 0) # subtrama se ajuste a la figura
        plt.show()
    def frec_words(self, text):
        palabras = re.findall(r'\b\w+\b', text.lower())
        # Contar la frecuencia de cada palabra
        frecuencia = Counter(palabras)
        # Crear un gráfico de barras de la frecuencia de las palabras
        plt.bar(frecuencia.keys(), frecuencia.values())
        plt.show()
