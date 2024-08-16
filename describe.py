import pandas as pd

df = pd.DataFrame({
    'Height_in_cm': [170, 180, 175, 185, 178],
    'Weight_in_kg': [65, 75, 70, 80, 72],
    'Age_in_years': [25, 30, 28, 35, 32]
})

desc_stats = df.describe()
print(desc_stats)