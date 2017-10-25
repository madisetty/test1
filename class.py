class Employee:
	empcount = 0
	def __init__(self,name,salary):
		self.name = name
		self.salary = salary
		employee.empcount += 1
	def displaycount(self):
		print employee.empcount
	def displayemployee(self):
		print self.name,self.salary
emp1 = employee("nitesh",20000)
emp2 = employee("sathish",30000)
emp1.age = 7
emp2.age = 8
print emp1.empcount
print emp1.name
print emp1.salary
print emp2.empcount
