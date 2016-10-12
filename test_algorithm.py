import unittest
from algorithm import hash_text

class TestHashText(unittest.TestCase):
	def setUp(self):
		self.avail_func_array = ['md5', 'sha1', 'sha256']
