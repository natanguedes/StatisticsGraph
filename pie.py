
import matplotlib.pyplot as plt
# fatias = [90, 5]
# atividades = ['F','M']
# colunas = ['c','k']
#
# plt.pie(fatias, labels = atividades, colors = colunas, startangle = 90, shadow = True, explode = (0,0.1))
# plt.show()
# # F,F,M,M,F,M,F,F,F,F,F,F,F,M,F,F,F,M,F,F,F,F,F,F,F

values = [90, 10]
colors = ['b', 'g']
labels = ['Feminino', 'Masculino']
xplode = (0.2, 0)
plt.pie(values, colors=colors, labels=values  , explode=xplode, counterclock=False, shadow=True)
plt.title('Relacao entre feminino e masculino')
plt.legend(labels, loc=3)
plt.show()