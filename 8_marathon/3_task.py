import unittest
import cmath

def quadratic_equation(a,b,c):
	d = (b ** 2) - (4 * a * c)	
	if a == 0:
		raise ValueError

	if d < 0:
		return None 
	x1 = (-b - d**0.5) / (2 * a)
	x2 = (-b + d**0.5) / (2 * a)
	if d == 0:
		return x2
	return x2,x1


class QuadraticEquationTest(unittest.TestCase):
	
	def test_negative_discriminant(self):
		given = quadratic_equation(2, 1, -1)
		expected = (0.5, -1.0)
		self.assertEqual(given, expected)

	def test_positive_discriminant(self):
		given = quadratic_equation(1, -4, 4)
		expected = (2.0)
		self.assertEqual(given, expected)

	def test_zero_discriminant(self):
		self.assertRaises(ValueError, quadratic_equation, 0, 6, 3)

	def test_quadratic(self):
		given = quadratic_equation(4, 6, 2)
		expected = (-0.5, -1.0)        
		self.assertEqual(given, expected)

