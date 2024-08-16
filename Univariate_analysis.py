import numpy as np
import matplotlib.pyplot as plt

# Let's assume these are the heights of a group in inches
heights_in_inches = [63, 64, 66, 67, 68, 69, 71, 72, 73, 55, 75]

fig, axs = plt.subplots(1, 2, figsize=(10, 5))

# Boxplot
axs[0].boxplot(heights_in_inches, whis=0.5)
axs[0].set_title('Box plot of heights')

# Histogram
bins = range(min(heights_in_inches), max(heights_in_inches) + 5, 5)
axs[1].hist(heights_in_inches, bins=bins, alpha=0.5)
axs[1].set_title('Frequency distribution of heights')
axs[1].set_xlabel('Height (in)')
axs[1].set_ylabel('Frequency')

plt.tight_layout()
plt.show()