import statistics

import matplotlib.pyplot as plt
import numpy as np
labels = ['Corinthias', 'Palmeiras', 'Santos', 'São Paulo']
titulos = [27, 22, 22, 22]
cores = ['lightblue', 'green', 'white', 'red']
explode = (0.1, 0, 0, 0)  # somente explode primeiro pedaço
total = sum(titulos)
plt.pie(titulos, explode=explode, labels=labels, colors=cores, autopct=lambda p: '{:.0f}'.format(p * total / 100), shadow=True, startangle=90)

# Determina que as proporções sejam iguais ('equal') de modo a desenhar o círculo
plt.axis('equal')
plt.show()
plt.legend(labels, loc=3)
print(sum(titulos)) #soma
media = statistics.mean([11, 2, 13, 14, 44])
mediana = statistics.median([11, 2, 13, 14, 44])
moda = statistics.mode([11,22,11,21,11,45,11])
print(media)
print(mediana)
print(moda)


# returns 16.8

