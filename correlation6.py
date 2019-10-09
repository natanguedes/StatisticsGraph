import pandas as pd

# 1000 random integers between 0 and 50
from plotly.figure_factory import np
import matplotlib.pyplot as plt



df = pd.DataFrame({'a': np.random.randint(0, 50, 1000)})
df['b'] = 100 - df['a'] + np.random.normal(0, 50, 1000) # negatively correlated with 'a'
df['c'] = 100 - df['a'] + np.random.normal(0, 50, 1000) # negatively correlated with 'a'
df['d'] = 100 - df['a'] + np.random.normal(0, 50, 1000) # negatively correlated with 'a'
plt.matshow(df.corr())
plt.title("exemplo de correlação\n\n")

plt.xticks(range(len(df.columns)), df.columns)
plt.yticks(range(len(df.columns)), df.columns)
plt.colorbar()

plt.show()
s= df.corr()
print(s)
