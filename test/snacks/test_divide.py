import unittest
import divide

class TestDivideFunction(unittest.TestCase):
	def test_that_function_exists(self):
		divide.get_divide(8, 23)
		
	def test_that_function_returns_correct_value(self):
		actual = divide.get_divide(22, 24)
		expected = 1
		self.assertEqual(actual, expected)
		
	def test_that_divide_function_raise_exception_with_invalid_input(self):
		self.assertRaises(TypeError, divide.get_divide, "name")

if __name__ ==("__main__"):
	unittest.main()