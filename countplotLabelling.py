import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


tips = sns.load_dataset("tips")
smoker = tips.smoker.value_counts()[0]
nonsmoker = tips.smoker.value_counts()[1]

data = tips['day'].value_counts(ascending = True).values

ax = sns.countplot(x = tips['day'], order = tips['day'].value_counts(ascending = True).index)
plt.xlabel('Day')
ax.bar_label(container = ax.containers[0], labels = data)
plt.tight_layout()
plt.show()




print(tips.columns)










