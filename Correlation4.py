
import numpy as np
import matplotlib.pyplot as plt
import csv

plt.plot([10,20,30,40], [15, 40, 75, 90],   linestyle='dotted', color='r', marker='s',
         linewidth=3.0, )
plt.axis([0,50,0,100])
plt.xlabel("peso")
plt.ylabel("quantidade ofertada")
plt.title("exemplo de correlação")
plt.show()