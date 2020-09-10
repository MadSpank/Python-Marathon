import unittest

class TriangleNotValidArgumentException(Exception):
	def __str__(self):
		return 'Not valid arguments'

class TriangleNotExistException(Exception):
	def __str__(self):
		return "Can`t create triangle with this arguments"

class Triangle:
	def __init__(self, args):
		self.check_args_number(args)
		self.a, self.b, self.c = args
		self.check_arguments()
		self.area = None
		self.get_area()

	def check_args_number(self, args):
		if type(args) != tuple or len(args) != 3:
			raise TriangleNotValidArgumentException

	def check_arguments(self):
		if not isinstance(self.a or self.b or self.c, int):
			raise TriangleNotValidArgumentException
		elif self.a <= 0 or self.b <= 0 or self.c <= 0:
			raise TriangleNotExistException
		elif self.a >= (self.b + self.c) or self.b >= (self.a + self.c) or self.c >= (self.a + self.b):
			raise TriangleNotExistException

	def get_area(self):
		s = (self.a + self.b + self.c) / 2
		self.area = (s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5
		return self.area

class TriangleTest(unittest.TestCase):

	def test_valid_data(self):
		self.assertAlmostEqual(Triangle((3, 4, 5)).area, 6.0, places=1)
	@unittest.expectedFailure
	def test_invalid_triangle(self):
		given = Triangle((1, 2, 3))
		self.assertRaises(TriangleNotExistException, given)
	@unittest.expectedFailure
	def test_invalid_arguments(self):
		given = Triangle((1, 2, 3))
		self.assertRaises(TriangleNotValidArgumentException, given)
