import pandas as pd


estudo = [8, 8, 10, 11, 11, 14] # cria uma lista
salario = [1000, 1000, 1100, 1100, 1300, 2000] # cria outra lista

dados = pd.DataFrame({'estudo':estudo, 'salario':salario}) # transforma as listas em um dataframe
dados2 = dados.plot.scatter('estudo', 'salario', s=100);
print(pd.show())
