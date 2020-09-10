import unittest

def file_parser(*args):
	counter = 0
	if len(args) == 2:
		with open(args[0], 'r') as file:
			for line in file:
				if args[1] in line:
					counter += 1
		return f'Found {counter} strings'
	elif len(args) == 3:
		with open(args[0], 'r') as file:
			for line in file:
				line.replace(args[1], args[2])
	else:
		raise ValueError
class ParserTest(unittest.TestCase):
	@unittest.expectedFailure
	def test_raise(self):
		file_parser(1)
	def test_valid(self):
		self.assertEqual(file_parser('parser.txt', 'better'), 'Found 8 strings')

# Create function file_parser. If function called with 2 arguments programm must count the number of occurrences string in a file, if 3 arguments programm must replace string in a file to new string

# first argument - path to file

# second argument - find string

# third argument - replace string

# Function must returned string with count of occurrences or count of replaced strings

# Example:

# file_parser("file.txt", 'x', 'o')-> Replaced 8 strings
# file_parser("file.txt", 'o') -> Found 8 strings
# Please, create class ParsesTest and write unittest for file_parser function uses mock object