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



box_plot = sns.boxplot(x="day",y="total_bill",data=tips)

medians = tips.groupby(['day'])['total_bill'].median()
vertical_offset = tips['total_bill'].median() * 0.05 # offset from median for display

for xtick in box_plot.get_xticks():
    box_plot.text(xtick,medians[xtick] + vertical_offset,medians[xtick], 
            horizontalalignment='center',size='x-small',color='w',weight='semibold')
    
    
    

import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects


def add_median_labels(ax, fmt='.1f'):
    lines = ax.get_lines()
    boxes = [c for c in ax.get_children() if type(c).__name__ == 'PathPatch']
    lines_per_box = int(len(lines) / len(boxes))
    for median in lines[4:len(lines):lines_per_box]:
        x, y = (data.mean() for data in median.get_data())
        # choose value depending on horizontal or vertical plot orientation
        value = x if (median.get_xdata()[1] - median.get_xdata()[0]) == 0 else y
        text = ax.text(x, y, f'{value:{fmt}}', ha='center', va='center',
                       fontweight='bold', color='white')
        # create median-colored border around white text for contrast
        text.set_path_effects([
            path_effects.Stroke(linewidth=3, foreground=median.get_color()),
            path_effects.Normal(),
        ])


tips = sns.load_dataset("tips")

ax = sns.boxplot(data=tips, x='day', y='total_bill', hue="sex")
add_median_labels(ax)
plt.show()




print(tips.columns)










