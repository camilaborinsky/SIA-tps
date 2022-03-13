
import unittest

from config_parser import import_config


class TestConfigParser(unittest.TestCase):

    def test_find_path(self):
        existing_file_path = "test/mock_config_files/config_correct.json"
        import_config(existing_file_path)
        

if __name__ == '__main__':
    unittest.main()