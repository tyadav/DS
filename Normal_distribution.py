import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set the mean and standard deviation
mu, sigma = 0, 0.1 

# Generate a normally distributed variable
var = np.random.normal(mu, sigma, 1000)

# Create a histogram of the variable using seaborn's histplot
sns.histplot(var, bins=30, kde=True)

# Add title and labels
plt.title('Histogram of Normally Distributed Variable')
plt.xlabel('Value')

plt.ylabel('Frequency')

# Show the plot
plt.show()