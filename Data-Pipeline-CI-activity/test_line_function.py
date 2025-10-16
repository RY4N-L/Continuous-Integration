import csv
import numpy as np

def generate_random_data(m, b, n_values, min_x, max_x, filename='Data-Pipeline-CI-activity/random_linear_data.csv'):
    # Generate n random x values between min_x and max_x
    x_values = np.random.uniform(low=min_x, high=max_x, size=n_values)

    noise = np.random.normal(0, 2, n_values)  # Random values to add noise
    
    # Calculate corresponding y values using y = mx + b
    y_values = m * x_values + b
    y_values += noise  # Add noise to y values
    
    # Write to CSV
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['x', 'y'])  # Header
        for x, y in zip(x_values, y_values):
            writer.writerow([x, y])

    print(f"CSV file '{filename}' created with {n_values} random data points.")

# Example usage
generate_random_data(m=2, b=1, n_values=50, min_x=0, max_x=10)