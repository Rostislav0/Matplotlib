import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


df = pd.read_csv('dota_hero_stats (3).csv')
df['cnt'] = df.roles.str.count(',')+1
print(df.groupby(['cnt'])['cnt'].count())
sns.histplot([x.count(',')+1 for x in df.roles], bins=15)
plt.show()
