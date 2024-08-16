import pandas as pd
import seaborn as sns
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Load the penguins dataset
penguins = pd.read_csv('https://raw.githubusercontent.com/MicrosoftLearning/dp-data/main/penguins.csv')

# Remove missing values
penguins = penguins.dropna()

# Prepare the data and target
X = penguins.drop('Species', axis=1)
y = penguins['Species']

# Initialize and apply PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Plot the data
plt.figure(figsize=(8, 6))
for color, target in zip(['navy', 'turquoise', 'darkorange'], penguins['Species'].unique()):
    plt.scatter(X_pca[y == target, 0], X_pca[y == target, 1], color=color, alpha=.8, lw=2,
                label=target)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('PCA of Penguins dataset')
plt.show()