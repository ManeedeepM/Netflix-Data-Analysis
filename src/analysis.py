def content_count(df):
    return df['type'].value_counts()

def top_genres(df):
    df['listed_in'] = df['listed_in'].str.split(',')
    genre_df = df.explode('listed_in')
    return genre_df['listed_in'].value_counts().head(10)