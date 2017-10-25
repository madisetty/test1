class istring():
	def __init__(self):
		self.str1 = ""
	def get_str(self):
		self.str1 = input()
	def print_string(self):
		print (self.str1.upper())
str1 = istring()
str1.get_str()
str1.print_string()
