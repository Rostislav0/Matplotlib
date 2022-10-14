import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

s = pd.read_csv('genome_matrix.csv', index_col=0)
print(s)
g = sns.heatmap(data=s, cmap='viridis')

g.xaxis.set_ticks_position('top')
g.xaxis.set_tick_params(rotation=90)
# plt.show()
