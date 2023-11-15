import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


df = pd.read_csv('Exercise_data.csv')

"""plt.figure(figsize=(10,10))
sns.scatterplot(data=df, x='time', y='avg_rss12', hue='Label', palette='viridis')
plt.show()
sns.countplot(data=df, x="Label")
plt.show()"""

print(df.describe().T)

def scree_plot(df):
    df = df[["avg_rss12", "var_rss12", "avg_rss13", "var_rss13", "avg_rss23", "var_rss23"]]
    #df = df.astype(float)
    df_copy = df.copy()
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df_copy)
    pca = PCA()
    pca.fit_transform(scaled_data)
    plt.figure(figsize=(10,10))
    plt.plot(np.cumsum(pca.explained_variance_ratio_))
    plt.show()
    scaled_df = pd.DataFrame(scaled_data, columns=df.columns)
    return scaled_df

if __name__ == "__main__":
    scaled_df = scree_plot(df)
    print(scaled_df.head(3))
