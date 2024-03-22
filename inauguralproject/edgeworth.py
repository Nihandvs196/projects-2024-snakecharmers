import numpy as np
import matplotlib.pyplot as plt

# Set the total quantities for two goods
total_good1 = 1
total_good2 = 1

# Create a figure and an axis
fig, ax = plt.subplots(figsize=(6, 6))

# Set limits for the Edgeworth Box
ax.set_xlim(0, total_good1)
ax.set_ylim(0, total_good2)

# Label axes
ax.set_xlabel('Good 1')
ax.set_ylabel('Good 2')
ax.set_title('Edgeworth Box')

# Plot the origin for both consumers
# Consumer A's origin is at (0, 0)
ax.plot(0, 0, 'o', color='blue', label='Consumer A Origin')

# Consumer B's origin is at (total_good1, total_good2)
ax.plot(total_good1, total_good2, 'o', color='red', label='Consumer B Origin')

# Optionally, draw a diagonal line representing perfect equality in distribution
ax.plot([0, total_good1], [0, total_good2], '--', color='gray', label='Line of Equality')

x = [0.2,0.3, 0.4]
y = [0.8, 0.7, 0.6]
ax.plot(x, y, marker='o', markersize=10, color='red')

ax.legend()

plt.show()
