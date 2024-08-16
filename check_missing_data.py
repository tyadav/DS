import pandas as pd
import numpy as np

# Create a sample DataFrame with some missing values
data = {
    'A': [1, 2, np.nan],
    'B': [4, np.nan, np.nan],
    'C': [7, 8, 9]
}
df = pd.DataFrame(data)

# Check for missing data
print(df.isnull())