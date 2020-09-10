import unittest

class Worker:
	def __init__(self, name, salary=0.0):
		self.name = name
		self.salary = salary

	def get_tax_value(self):
		if type(self.name) != str:
			raise ValueError()
		if self.salary < 0:
			raise ValueError()
		if self.salary in range(0,1001):
			return 0.0
		if self.salary in range(1001,3000):
			return (0.1 * (self.salary - 1000))
		if self.salary in range(3001, 5000):
			return (0.15 * (self.salary - 3000)) + (0.1 * (3000 - 1000))
		if self.salary in range(5001,1000):
			return (0.21 * (self.salary - 5000)) + (0.15 * (5000 - 3000)) + (0.1 * (3000 - 1000))
		if self.salary in range(10001,20000):
			return (0.3 * (self.salary - 10000)) + (0.21 * (10000 - 5000)) + (0.15 * (5000 - 3000)) + (0.1 * (3000 - 1000)) 
		if self.salary in range(20001,50000):
			return (0.4 * (self.salary - 20000)) + (0.3 * (20000 - 10000)) + (0.21 * (10000 - 5000)) + (0.15 * (5000 - 3000)) + (0.1 * (3000 - 1000))       
		if self.salary > 50000:
			return (0.47 * (self.salary - 50000)) + (0.4 * (50000 - 20000)) + (0.3 * (20000 - 10000)) + (0.21 * (10000 - 5000)) + (0.15 * (5000 - 3000)) + (0.1 * (3000 - 1000))
 
class WorkerTest(unittest.TestCase):
	def setUp(self):
		self.billy = Worker('Billy', 777)
		self.dilly = Worker('Billy', -26000)
		self.no_name = Worker(222000)

	@unittest.expectedFailure
	def test_valid_tax(self):
		expected_tax = 0.0
		self.assertAlmostEqual(self.billy.get_tax_value(), expected_tax)
	
	@unittest.expectedFailure
	def test_exception(self):
		self.dilly.get_tax_value()
	
	def tearDown(self):
		self.billy = None
		self.dilly = None
		self.no_name = None

# Create class Worker with fields name and salary. If salary negative raise ValueError

# Create a method get_tax_value() that calculate tax from salary . Tax must be calculate like "progressive tax" with next step:

# less then 1000 - 0%
# 1001 - 3000 - 10%
# 3001 - 5000 - 15%
# 5001 - 10000 - 21%
# 10001 - 20000 - 30%
# 20001 - 50000 - 40%
# more than 50000 - 47%

