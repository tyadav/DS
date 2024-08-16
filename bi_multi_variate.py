import matplotlib.pyplot as plt
import numpy as np

# Sample data
np.random.seed(0)  # for reproducibility
house_sizes = np.random.randint(1000, 3000, size=50)  # Size of houses in square feet
house_prices = house_sizes * 100 + np.random.normal(0, 20000, size=50)  # Price of houses in dollars

# Create scatter plot
plt.scatter(house_sizes, house_prices)

# Set plot title and labels
plt.title('House Prices vs Size')
plt.xlabel('Size (sqt)')
plt.ylabel('Price ($)')

# Display the plot
plt.show()