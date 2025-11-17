import unittest
import os
from generate_and_plot_random_linear_data import generate_random_data, plot_random_data

class TestLinearFit(unittest.TestCase):

    def setUp(self):
        # Setup file paths
        self.data_file = 'Data-Pipeline-CI-activity/test_random_linear_data.csv'
        self.plot_file = 'Data-Pipeline-CI-activity/test_random_linear_plot.png'
        self.m_true = 2
        self.b_true = 1

        # Generate fresh random data before each test
        generate_random_data(self.m_true, self.b_true, 50, 0, 10, self.data_file)

    def cleanUp(self):
        # Clean up files after tests
        if os.path.exists(self.data_file):
            os.remove(self.data_file)
        if os.path.exists(self.plot_file):
            os.remove(self.plot_file)

    def test_best_fit_line_close_to_true(self):
        # Run the plotting/fitting function
        m_fit, b_fit = plot_random_data(self.m_true, self.b_true, self.data_file, self.plot_file)

        # Check slope is within 0.2
        self.assertAlmostEqual(m_fit, self.m_true, delta=0.2)

        # Check intercept is within 0.5
        self.assertAlmostEqual(b_fit, self.b_true, delta=0.5)

if __name__ == '__main__':
    unittest.main()