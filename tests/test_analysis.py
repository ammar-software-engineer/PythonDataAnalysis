import unittest
import pandas as pd
from src.analysis import load_data, calculate_mean

class TestDataAnalysis(unittest.TestCase):
    def setUp(self):
        self.sample_data = pd.DataFrame({
            'id': [1, 2, 3],
            'value': [10, 20, 30]
        })
        self.sample_file_path = 'test_data.csv'
        self.sample_data.to_csv(self.sample_file_path, index=False)

    def tearDown(self):
        import os
        if os.path.exists(self.sample_file_path):
            os.remove(self.sample_file_path)

    def test_load_data(self):
        df = load_data(self.sample_file_path)
        pd.testing.assert_frame_equal(df, self.sample_data)

    def test_calculate_mean(self):
        mean_value = calculate_mean(self.sample_data, 'value')
        self.assertEqual(mean_value, 20.0)

if __name__ == '__main__':
    unittest.main()
