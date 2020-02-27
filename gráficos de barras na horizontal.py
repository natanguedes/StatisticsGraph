
import matplotlib.pyplot as plt

Produtos = ['trigo','farinha','arroz','macarrao','mandioca']
qtdade = [40,22,33,40,70]

plt.barh(Produtos,qtdade, color='purple')
plt.ylabel("Produtos agriculas")
plt.xlabel("Produtos em %")
plt.title("Gráfico de barras na horizontal \nProduto com maior participação na industria agricola")
plt.show()

