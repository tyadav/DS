import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#Load the Penguins dataset from seaborn
penguins = sns.load_dataset('penguins')

# Create a binomial variable for 'species'
penguins['is_adelie'] = np.where(penguins['species'] == 'Adelie', 1, 0)

# Plot the distribution of 'is_adelie'
sns.histplot(data=penguins, x='is_adelie', bins=2, discrete=True)
plt.title('Binomial Distribution of Species')
plt.xticks([0, 1], ['Not Adelie', 'Adelie'])
plt.show()
