import os
import matplotlib.pyplot as plt
import seaborn as sns

# create folder automatically
os.makedirs("outputs/plots", exist_ok=True)

def plot_content_type(df):
    sns.countplot(x='type', data=df)
    plt.title("Movies vs TV Shows")
    plt.savefig("outputs/plots/movies_vs_tv.png")
    plt.close()

def plot_yearly_trend(df):
    df['year_added'].value_counts().sort_index().plot()
    plt.title("Content Over Years")
    plt.savefig("outputs/plots/yearly_trend.png")
    plt.close()