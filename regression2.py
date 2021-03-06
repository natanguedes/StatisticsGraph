import numpy as np
import pandas as pd

# 1000 random integers between 0 and 50


import matplotlib.pyplot as plt

x = np.random.randint(0, 50, 1000)

# Negative Correlation with some noise
y = 100 - x + np.random.normal(0, 5, 1000)

a= np.corrcoef(x, y)
print(a)
plt.xlabel("Velocidade")
plt.ylabel("Consumo de  combustível")
plt.title("Gráfico de regressão\n"
          "Correlação entre velocidade e combustível")
plt.scatter(x, y)
plt.show()
