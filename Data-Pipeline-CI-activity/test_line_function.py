import csv
import numpy as np

def generate_random_data(m, b, n, min_x, max_x, filename='random_linear_data.csv'):
    # Generate n random x values between min_x and max_x
    x_values = np.random.uniform(low=min_x, high=max_x, size=n)
    
    # Calculate corresponding y values using y = mx + b
    y_values = m * x_values + b

    # Write to CSV
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['x', 'y'])  # Header
        for x, y in zip(x_values, y_values):
            writer.writerow([x, y])

    print(f"CSV file '{filename}' created with {n} random data points.")

# Example usage
generate_random_data(m=2, b=1, n=50, min_x=0, max_x=10)