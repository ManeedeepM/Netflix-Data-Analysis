from src.data_cleaning import load_and_clean_data
from src.analysis import content_count, top_genres
from src.visualization import plot_content_type, plot_yearly_trend

# Load data
df = load_and_clean_data("data/netflix_titles.csv")

# Analysis
print(content_count(df))
print(top_genres(df))

# Visualization
plot_content_type(df)
plot_yearly_trend(df)

print("Project executed successfully!")