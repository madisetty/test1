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
emp3 = employee("suresh",500000)
emp1.age = 30
emp2.age = 40
print emp1.empcount
print emp1.name
print emp1.salary
print emp2.empcount
print emp3.name
