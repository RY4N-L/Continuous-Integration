import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load CSV file
df = pd.read_csv('Data-Pipeline-CI-activity/random_linear_data.csv')

# Obtain x and y values
x = df['x']
y = df['y']

# Fit line and find y_fit values
m, b = np.polyfit(x, y, 1)
y_fit = m * x + b

# Plot data and fitted line
plt.figure(figsize=(8, 5))
plt.scatter(x, y, label='Data Points', alpha=0.7)
plt.plot(x, y_fit, color='red', label=f'Line of Best Fit: y={m:.2f}x+{b:.2f}', linewidth=2, linestyle='--')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Random Linear Data with Line of Best Fit')
plt.legend()

plt.grid(True)
plt.tight_layout()
plt.show()