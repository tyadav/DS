import seaborn as sns
import pandas as pd

# Sample data
data = {
    'Size': [1000, 2000, 3000, 1500, 1200],
    'Bedrooms': [2, 4, 3, 2, 1],
    'Age': [5, 10, 2, 6, 4],
    'Price': [200000, 400000, 350000, 220000, 150000]
}

df = pd.DataFrame(data)

# Create a pair plot
sns.pairplot(df)