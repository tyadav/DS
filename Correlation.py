import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the penguins dataset
penguins = pd.read_csv('https://raw.githubusercontent.com/MicrosoftLearning/dp-data/main/penguins.csv')

# Calculate the correlation matrix
corr = penguins.corr()

# Create a heatmap
sns.heatmap(corr, annot=True)
plt.show()