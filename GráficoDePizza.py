

import matplotlib.pyplot as plt

porc = [10,50,20,20]
nomes = ['Brasil','China','Eua','França']
col = ['aqua','red','green','yellow']
explode = (0, 0, 0, 0)
plt.pie(porc, colors=col, labels=nomes, explode=explode,  autopct='%1.1f%%', counterclock=False, shadow=True)
plt.title('Gráfico de setores\nPopulação que mais utiliza as redes sociais')
plt.legend(nomes, loc='lower right')
plt.show()