import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
df_tips = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')
df_tips.head()
sns.set(font_scale=1.4)
df_tips['total_bill'].plot(kind='hist', figsize=(10, 10));
plt.xlabel("Total Bill Amount ($)", labelpad=14)
plt.ylabel("Frequency", labelpad=14)
plt.title("Distribution of Tip Bill Amounts ($)", y=1.015, fontsize=22);
plt.show()