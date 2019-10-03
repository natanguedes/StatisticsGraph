


import matplotlib.pyplot as plt

# Definindo variáveis
x = ["doce"]
y = ["nenhum","doce"]

x2 = ["salgado"]
y2 = ["salgado"]

# Criando um gráfico
plt.bar(x, y, label='doce', color='r')
plt.bar(x2, y2, label='salgado', color='y')
plt.legend(loc=9)

plt.show()