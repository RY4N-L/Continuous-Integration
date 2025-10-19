#!/usr/bin/env python3
"""
Plot random linear data (reads random_linear_data.csv if present, else generates data),
fits a linear regression line, and saves the plot to random_linear_plot.png.
"""
import os
import csv
import sys

try:
    import numpy as np
except Exception:
    print("This script requires numpy and matplotlib. Install with: pip install numpy matplotlib")
    sys.exit(1)

try:
    import matplotlib.pyplot as plt
except Exception:
    print("This script requires matplotlib. Install with: pip install matplotlib")
    sys.exit(1)


def read_csv(path):
    if os.path.exists(path):
        # Prefer pandas if available for robustness
        try:
            import pandas as pd
            df = pd.read_csv(path)
            x = df['x'].values
            y = df['y'].values
            return x, y
        except Exception:
            xs, ys = [], []
            with open(path, 'r', newline='') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    try:
                        xs.append(float(row['x']))
                        ys.append(float(row['y']))
                    except Exception:
                        continue
            return np.array(xs), np.array(ys)
    return None


def generate_and_save(path, n=50, a=2.0, b=1.0, noise=1.0, seed=0):
    rng = np.random.RandomState(seed)
    x = rng.uniform(0, 10, size=n)
    y = a * x + b + rng.normal(scale=noise, size=n)
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['x', 'y'])
        for xi, yi in zip(x, y):
            writer.writerow([xi, yi])
    return x, y


def fit_and_plot(x, y, outfile='random_linear_plot.png', show=False):
    # Fit a straight line y = m*x + c
    m, c = np.polyfit(x, y, 1)
    xs = np.linspace(np.min(x), np.max(x), 200)
    ys = m * xs + c

    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, alpha=0.8, label='data')
    plt.plot()
    plt.plot(xs, ys, color='red', linewidth=2, label=f'fit: y={m:.3f}x+{c:.3f}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Random linear data with linear fit')
    plt.legend()
    plt.tight_layout()
    plt.savefig(outfile)
    print(f"Saved plot to {outfile}")
    if show:
        plt.show()


def main(show=False):
    root = os.path.dirname(__file__)
    csv_path = os.path.join(root, 'random_linear_data.csv')
    data = read_csv(csv_path)
    if data is None or len(data[0]) == 0:
        x, y = generate_and_save(csv_path)
        print(f"Generated {len(x)} rows and saved to {csv_path}")
    else:
        x, y = data
        print(f"Loaded {len(x)} rows from {csv_path}")

    outpath = os.path.join(root, 'random_linear_plot.png')
    
    fit_and_plot(x, y, outfile=outpath, show=show)


if __name__ == '__main__':
    # Allow a simple CLI: pass 'show' to open the plot window (if available)
    show_flag = len(sys.argv) > 1 and sys.argv[1].lower() == 'show'
    main(show=show_flag)
