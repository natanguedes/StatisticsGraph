from numpy import mean
from numpy import std
from numpy import correlate
from numpy.random import randn
from numpy.random import seed
from matplotlib import pyplot


data1 = 20 * randn(1000) + 100
data2 = data1 + (10 * randn(1000) + 50)

print('média de data1:' '', str(round(mean(data1),2)))
print('desvio padrão de data1:' '', str(round(std(data1),2)))


print('média de data2:' '', str(round(mean(data2),2)))
print('desvio padrão de data1:' '', str(round(std(data2),2)))
pyplot.scatter(data1, data2)
pyplot.title('Gráfico de Dispersão entre data1 e data2')
pyplot.show()