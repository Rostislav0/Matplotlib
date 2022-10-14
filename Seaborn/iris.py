import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


df = pd.read_csv('iris.csv', index_col=0)
# check modes
# for i in df.columns:
#     sns.kdeplot(df[i])
#     plt.show()

# get correlation
sns.pairplot(df, hue="species")
plt.show()