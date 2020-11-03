import unittest
from algorithm import hash_text


class TestHashText(unittest.TestCase):
    def setUp(self):
        self.avail_func_array = ['md5', 'sha1', 'sha256']
        self.avail_func_array2 = ['sha256', 'sha224']
        self.text = "hello"
        self.hello_pass_1 = {'sha1': 'aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d',
                             'sha256': '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824',
                             'md5': '5d41402abc4b2a76b9719d911017c592'}
        self.hello_pass_100 = {'sha1': '3005a7cebc1edda34127c87c7bc79074e113015d',
                               'sha256': '0c7e20c4751943a4cf4ec6a2d17a520c8aaf1d2a714e2af1ad6667fd06c056de',
                               'md5': '3b8ca2de573942e58426494e9fcf8766'}

    def test_successful(self):
        self.assertEqual(self.hello_pass_1, hash_text(self.avail_func_array, self.text, 1)[1],
                         "Correct hash values for one (1) pass of given hash algorithms")
        self.assertCountEqual(self.hello_pass_100, hash_text(self.avail_func_array, self.text, 100)[1],
                              "Correct hash values for hundred (100) pass of given hash algorithms")

    def test_empty_function_array(self):
        self.assertFalse(hash_text([], self.text, 1)[0], "One should not use empty array for the hash algorithm list.")

    def test_none_function_array_type(self):
        self.assertFalse(hash_text(None, self.text, 1)[0], "Incorrect type for hash algorithms list.")

    def test_diferent_function_array(self):
        self.assertNotEqual(self.hello_pass_1, hash_text(self.avail_func_array2, self.text, 1),
                            "Incorrect list of results, different hash algorithms used.")

    def test_none_text_type(self):
        self.assertFalse(hash_text(self.avail_func_array, None, 1)[0], "Incorrect type for text to be hashed.")

    def test_incorrect_text_type(self):
        self.assertFalse(hash_text(self.avail_func_array, 9999, 1)[0],
                         "Incorrect type for the text parameter; should be of string type.")

    def test_none_pass_count_type(self):
        self.assertFalse(hash_text(self.avail_func_array, self.text, None)[0], "Incorrect type for pass count.")

    def test_different_pass_count(self):
        self.assertNotEqual(self.hello_pass_1, hash_text(self.avail_func_array, self.text, 9999),
                            "Incorrect list of results, different hash algorithms used.")

    def test_incorrect_pass_count_type(self):
        self.assertFalse(hash_text(self.avail_func_array, self.text, self.text)[0],
                         "Incorrect type for the pass count parameter; should be of integer type.")

    def test_pass_count_value(self):
        self.assertFalse(hash_text(self.avail_func_array, self.text, 0)[0],
                         "Incorrect value for the pass count parameter; should be larger than zero.")
        self.assertFalse(hash_text(self.avail_func_array, self.text, -9999)[0],
                         "Incorrect value for the pass count parameter; should be larger than zero.")
        self.assertFalse(hash_text(self.avail_func_array, self.text, 99999999)[0],
                         "Incorrect value for the pass count parameter; should be smaller than 1000000.")


if __name__ == '__main__':
    unittest.main()
