import numpy as np
import matplotlib.pyplot as plt
produtos = ['Arroz','Feijão','macarrao ']
qts = [10,20,30]
plt.barh(produtos, qts, color='green')
plt.ylabel("Produtos Agrículas")
plt.xlabel("Participação dos Produtos (em %)")
plt.title("Produtos de maiores participação da indústria agrículas ")
plt.show()