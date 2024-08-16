import pandas as pd
import numpy as np

# Set the seed
np.random.seed(0)

# Define the size of the dataset
size = 500

# Generate random data
data = {
    'Size': np.random.randint(1000, 4001, size, dtype=int) // 10 * 10, # any integer value between 1000 and 4000, with multiple of 10
    'Bedrooms': np.random.choice([2, 4, 3, 2, 1], size),
    'YearBuilt': np.random.randint(1980, 2021, size), # any integer value between 1980 and 2020
    'Price': np.random.normal(loc=110000, scale=20000, size=size), # normally distributed prices
    'Type': np.random.choice(['Single Family', 'Townhouse', 'Condo', 'Duplex'], size) # type of the house
}

# Create a DataFrame
df = pd.DataFrame(data)