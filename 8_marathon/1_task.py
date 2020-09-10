import unittest

class Product:
	def __init__(self, name, price, count):
		self.name = name 
		self.price = price
		self.count = count 
		self.sum = 0

	def discount(self):
# 		try:	
		if self.count > 0 and self.count <= 2:
			self.sum = self.price * self.count 
		elif self.count > 2 and self.count <= 5:
			self.sum = self.price * 0.95 * self.count
		elif self.count > 5 and self.count <= 7:
			self.sum = self.price * 0.9 * self.count
		elif self.count > 7 and self.count <= 10:
			self.sum = self.price * 0.8 * self.count
		elif self.count > 10 and self.count <= 20:
			self.sum = self.price * 0.7 * self.count
		elif self.count > 20:
			self.sum = self.price * 0.5 * self.count
		elif self.count <= 0:
			raise Exception("Count can't be negative number or zero!")
		return self.sum

class Cart:
	total = 0
	def __init__(self):
		self.total = 0
		
	def add(self, item):
		self.total += item.discount()		
		print(f'total cost is ${self.total}')

class CartTest(unittest.TestCase):

	def test_discount(self):
		self.assertEqual(Product('cheese', 13, 2).discount(), 26)
		self.assertAlmostEqual(Product('cheese', 13, 6).discount(), 70.2)
		self.assertAlmostEqual(Product('cheese', 13, 9).discount(), 93.600000)
		self.assertAlmostEqual(Product('cheese', 13, 12).discount(), 109.199999999)
		self.assertAlmostEqual(Product('cheese', 13, 21).discount(), 136.5)
	def test_second_discount_range(self):
		self.assertAlmostEqual(Product('cheese', 13, 4).discount(), 49.4)