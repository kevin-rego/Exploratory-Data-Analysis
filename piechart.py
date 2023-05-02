import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

tips = sns.load_dataset("tips")
smoker = tips.smoker.value_counts()[0]
nonsmoker = tips.smoker.value_counts()[1]

print(smoker,nonsmoker)

plt.pie(x = [smoker, nonsmoker], labels  = ["Smoker","Non Smoker"], 
	autopct = lambda x: f"{x:.2f}%\n({x*(smoker+ nonsmoker) /100:.0f})", 
	wedgeprops = {"edgecolor": "black" }, shadow = "True")
plt.legend(loc = 'upper right')
plt.show()






