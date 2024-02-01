import matplotlib.pyplot as plt
from collections import Counter
import re

# Texto de entrada
texto = "La inteligencia artificial es una rama de la informática que busca desarrollar algoritmos, modelos y técnicas que permitan a las máquinas aprender y, en consecuencia, realizar tareas que normalmente requerirían de la inteligencia humana. Estas tareas incluyen el reconocimiento de voz, el aprendizaje, la planificación y el razonamiento, entre otras."

# Limpiar el texto y dividirlo en palabras
palabras = re.findall(r'\b\w+\b', texto.lower())

# Contar la frecuencia de cada palabra
frecuencia = Counter(palabras)
print(frecuencia, type(frecuencia))
# Crear un gráfico de barras de la frecuencia de las palabras
plt.bar(frecuencia.keys(), frecuencia.values())
plt.show()
