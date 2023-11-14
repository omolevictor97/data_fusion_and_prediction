import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


df = pd.read_csv('Exercise_data.csv')

plt.figure(figsize=(10,10))
sns.scatterplot(data=df, x='time', y='avg_rss12', hue='Label', palette='viridis')
plt.show()
sns.countplot(data=df, x="Label")
plt.show()

print(df.describe().T)
