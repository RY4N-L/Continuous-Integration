import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

random_linear_data_file = 'Data-Pipeline-CI-activity/random_linear_data.csv'
plot_image_file = 'Data-Pipeline-CI-activity/random_linear_plot.png'
m = 2  # slope
b = 1  # intercept
values = 50  # number of data points
min_x = 0
max_x = 10

def generate_random_data(m_value, b_value, n_values, min_x_value, max_x_value, file_name):
    
    # Generate n random x values between min_x_value and max_x_value
    x_values = np.random.uniform(low = min_x_value, high = max_x_value, size = n_values)

    noise = np.random.normal(0, 2, n_values)  # Random values to add noise
    
    # Calculate corresponding y values using y = mx + b
    y_values = m_value * x_values + b_value
    y_values += noise  # Add noise to y values
    
    # Write to CSV
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['x', 'y'])  # Header
        for x, y in zip(x_values, y_values):
            writer.writerow([x, y])

    print(f"CSV file '{file_name}' created with {n_values} random data points.")

def plot_random_data(m_value, b_value, file_name, plot_image_file_name):

    # Load CSV file
    df = pd.read_csv(file_name)

    # Obtain x and y values
    x = df['x']
    y = df['y']

    # Fit line and find y_fit values
    m, b = np.polyfit(x, y, 1)
    y_fit = m * x + b
    y_true = m_value * x + b_value

    # Plot data and fitted line
    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, label='Data Points', alpha=0.7)
    plt.plot(x, y_fit, color='red', linewidth=1, label=f'Line of Best Fit: y={m:.2f}x+{b:.2f}', linestyle=':')
    plt.plot(x, y_true, color='green', linewidth=1, label='Original Line: y=2x+1', linestyle='-')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Random Linear Data with Line of Best Fit')
    plt.legend()

    plt.grid(True)
    plt.tight_layout()
    plt.savefig(plot_image_file_name)
    plt.show()

    #Save data to a png file
    print(f"Plot saved as '{plot_image_file_name}'.")

    # Return slope and intercept for unit tests
    return m, b

# Generate data with specified parameters
generate_random_data(m, b, values, min_x, max_x, random_linear_data_file)

# Plot the generated data
plot_random_data(m, b, random_linear_data_file, plot_image_file)