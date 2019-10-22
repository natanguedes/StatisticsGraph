

import matplotlib.pyplot as plt

porc = [10,50,20,20]
nomes = ['Brasil','China','Eua','Fança']
col = ['aqua','red','green','yellow']
explode = (0, 0, 0, 0)
plt.pie(porc, colors=col, labels=nomes, explode=explode,  autopct='%1.1f%%', counterclock=False, shadow=True)
plt.title('População nas redes sociais')
plt.legend(nomes, loc='lower right')
plt.show()