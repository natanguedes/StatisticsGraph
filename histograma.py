

# df = pd.read_csv('C:/Users/Natanael/PycharmProjects/untitled3/questionario.csv')
# print(df.head())
# corr = df['Turma'].corr(df['Idade'],method="pearson", min_periods=1)
#  # """
import pandas
import numpy as np

data = pandas.DataFrame({'Numb':[1,2,3],'a':[7,8,9]})
corr1 = data['Numb'].corr(data['a'],method='pearson', min_periods=1)
print(corr1)
# Criando um diagrama de barras para os totais de cada idade
# """
# idade = df['Idade']
# idade_sum = idade.value_counts()
# idade_sum = idade_sum.sort_index()
#
# x = idade_sum.index
# y = idade_sum
#
# plt.figure(figsize=(8, 6))
#
#
# plt.bar(x, y)
#
# plt.title('Distribuição de Idades')
# plt.xlabel('Idade')
# plt.ylabel('Alunos')
# plt.xticks(x) # obriga a mostrar todos os números no eixo x
# plt.show()
# plt.savefig('C:/Users/Natanael/PycharmProjects/untitled3/diagrama-barras.png')
# plt.close()