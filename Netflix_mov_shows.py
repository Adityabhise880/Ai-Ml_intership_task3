import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv(r'C:\Users\adity\OneDrive\Desktop\labE\task3\netflix_titles.csv')
df.hist(figsize=(10,8))
plt.show()

# Plot 1: Movies vs TV Shows
plt.figure(figsize=(6, 4))
sns.countplot(x='type', data=df)
plt.title('Count of Movies vs TV Shows')
plt.show()

# Plot 2: Ratings (TV-MA, PG-13, etc.)
plt.figure(figsize=(12, 6))
sns.countplot(x='rating', data=df, order=df['rating'].value_counts().index)
plt.title('Count of Ratings')
plt.xticks(rotation=45) # Rotates text so it doesn't overlap
plt.show()


# Plot 2: Ratings (TV-MA, PG-13, etc.)
plt.figure(figsize=(12, 6))
sns.countplot(x='rating', data=df, order=df['rating'].value_counts().index)
plt.title('Count of Ratings')
plt.xticks(rotation=45) # Rotates text so it doesn't overlap
plt.show()