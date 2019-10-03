import pandas as pd

# 1000 random integers between 0 and 50
from plotly.figure_factory import np
import matplotlib.pyplot as plt

x = np.random.randint(0, 50, 1000)

# Negative Correlation with some noise
y = 100 - x + np.random.normal(0, 5, 1000)

a= np.corrcoef(x, y)
print(a)
plt.xlabel("teste")
plt.ylabel("teste2")
plt.title("exemplo de correlação")
plt.scatter(x, y)
# plt.show()

df = pd.DataFrame({'a': np.random.randint(0, 50, 1000)})
df['b'] = 100 - df['a'] + np.random.normal(0, 50, 1000) # negatively correlated with 'a'
df['c'] = 100 - df['a'] + np.random.normal(0, 50, 1000) # negatively correlated with 'a'
df['d'] = 100 - df['a'] + np.random.normal(0, 50, 1000) # negatively correlated with 'a'
plt.matshow(df.corr())
plt.xticks(range(len(df.columns)), df.columns)
plt.yticks(range(len(df.columns)), df.columns)
plt.colorbar()
plt.show()
s= df.corr()
print(s)

plt.title("exemplo de correlação")
