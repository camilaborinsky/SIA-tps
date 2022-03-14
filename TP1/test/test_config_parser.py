
import unittest
from constants import ConfigParams, SearchAlgorithm

from config_parser import Config, import_config


class TestConfigParser(unittest.TestCase):

    def test_find_path(self):
        existing_file_path = "test/mock_config_files/config_correct.json"
        import_config(existing_file_path)

    def test_path_not_found(self):
        non_existing_file_path = "/test/mock_config_files/config_incorrect.json"
        self.assertRaises(FileNotFoundError, lambda :import_config(non_existing_file_path))

    def test_valid_config(self):
        existing_file_path = "test/mock_config_files/config_correct.json"
        config = import_config(existing_file_path)
        self.assertEqual(SearchAlgorithm.BFS.value, config.algorithm)
        self.assertTrue(len(config.board.positions)==9)
               

if __name__ == '__main__':
    unittest.main()