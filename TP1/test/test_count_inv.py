import unittest

from utils import count_inversions




class TestInversionCount(unittest.TestCase):


    def test_basic(self):
        arr = [2, 1]
        self.assertEqual(1, count_inversions(arr, len(arr)))
    
    def test_no_inversions(self):
        arr = [1, 2]
        self.assertEqual(0, count_inversions(arr, len(arr)))
        arr = [1, 2, 3, 4]
        self.assertEqual(0, count_inversions(arr, len(arr)))
        arr = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(0, count_inversions(arr, len(arr)))
    
    def test_count_inv(self):
        arr = [2, 3, 1, 5, 4]
        self.assertEqual(3, count_inversions(arr, len(arr)))
        arr = [3, 1, 2]
        self.assertEqual(2, count_inversions(arr, len(arr)))
        arr = [5, 8, 4, 2, 1, 7, 3, 6]
        self.assertEqual(16,count_inversions(arr, len(arr)))



if __name__ == '__main__':
    unittest.main()