import pandas as pd
import pyspark as pk

df = pd.DataFrame({
  'A': [1, 2, 3, 4],
  'B': [10, 20, 30, 40]
})

print(df.summary())