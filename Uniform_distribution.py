import numpy as np
import matplotlib.pyplot as plt

# Generate a uniform distribution
uniform_data = np.random.uniform(-1, 1, 1000)

# Plot the distribution
plt.hist(uniform_data, bins=20, density=True)
plt.title('Uniform Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()