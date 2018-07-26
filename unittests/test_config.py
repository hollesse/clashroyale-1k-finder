import configparser
import unittest

from config import Config


class TestConfig(unittest.TestCase):

    def test_init__should_throw_exception__when_option_api_key_not_in_config(self):
        with self.assertRaises(configparser.NoOptionError):
            Config('init__should_throw_exception__when_option_api_key_not_in_config.cfg', True)

    def test_init__should_throw_exception__when_config_file_does_not_exist(self):
        with self.assertRaises(FileNotFoundError):
            Config('does_not_exist.cfg', True)

    def test_init__should_throw_exception__when_section_clashroyale_not_in_config(self):
        with self.assertRaises(configparser.NoSectionError):
            Config('test_init__should_throw_exception__when_section_clashroyale_not_in_config.cfg', True)


if __name__ == '__main__':
    unittest.main()
