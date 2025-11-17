import unittest
import os
import pandas as pd
import numpy as np
from generate_and_plot_random_linear_data import generate_random_data, plot_random_data


class TestLinearFit(unittest.TestCase):

    def setUp(self):
        # Setup file paths
        self.data_file = 'Data-Pipeline-CI-activity/test_random_linear_data1.csv'
        self.plot_file = 'Data-Pipeline-CI-activity/test_random_linear_plot1.png'
        self.m_true = 2
        self.b_true = 1

        # Generate fresh random data before each test
        generate_random_data(self.m_true, self.b_true, 50, 0, 10, self.data_file)

    def tearDown(self):
        # Clean up files after tests
        if os.path.exists(self.data_file):
            os.remove(self.data_file)
        if os.path.exists(self.plot_file):
            os.remove(self.plot_file)

    def test_csv_contains_only_numeric(self):
        df = pd.read_csv(self.data_file)
        # Check all values are numeric
        self.assertTrue(np.issubdtype(df['x'].dtype, np.number))
        self.assertTrue(np.issubdtype(df['y'].dtype, np.number))

    
    def test_best_fit_line_close_to_true(self):
        # Run the plotting/fitting function
        m_fit, b_fit = plot_random_data(self.m_true, self.b_true, self.data_file, self.plot_file)

        # Check slope is within 0.2
        self.assertAlmostEqual(m_fit, self.m_true, delta=0.2)

        # Check intercept is within 0.5
        self.assertAlmostEqual(b_fit, self.b_true, delta=0.5)

class TestFileCreation(unittest.TestCase):

    def setUp(self):
        self.data_file = "Data-Pipeline-CI-activity/test_random_linear_data1.csv"
        self.plot_file = "Data-Pipeline-CI-activity/test_random_linear_plot1.png"

        # Ensure clean slate before each test
        if os.path.exists(self.data_file):
            os.remove(self.data_file)
        if os.path.exists(self.plot_file):
            os.remove(self.plot_file)

    def test_csv_file_saved(self):
        # Run the function that should create the file
        generate_random_data(2, 1, 50, 0, 10, self.data_file)

        # Check the file now exists
        self.assertTrue(os.path.exists(self.data_file))

    def test_plot_file_saved(self):
        generate_random_data(2, 1, 50, 0, 10, self.data_file)
        plot_random_data(2, 1, self.data_file, self.plot_file)

        self.assertTrue(os.path.exists(self.plot_file))

    def tearDown(self):
        # Clean up after test
        if os.path.exists(self.data_file):
            os.remove(self.data_file)
        if os.path.exists(self.plot_file):
            os.remove(self.plot_file)

if __name__ == '__main__':
    unittest.main()