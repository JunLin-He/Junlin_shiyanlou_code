import unittest
from factorial import fact, div

class TestFactorial(unittest.TestCase):
	"""
	Basic Test Class
	"""
	def test_fact(self):
		'''
		Real test
		Any method with `test_` prefix will be considered as test cases
		'''
		res = fact(5)
		self.assertEqual(res, 120)

	def test_error(self):
		'''
		test exception that triggered from runtime error
		'''
		self.assertRaises(ZeroDivisionError, div, 0)


if __name__ == '__main__':
	unittest.main()


		