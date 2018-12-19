#!/usr/bin/env python3

class Person(object):
	'''
	Return a Person object with specific name
	'''

	def __init__(self, name):
		self.name = name

	def get_details(self):
		'''
		return a string which contains person name
		'''
		return self.name


class Student(Person):
	'''
	Return a Student object, with 3 parameter: name, branch, year
	'''

	def __init__(self, name, branch, year):
		Person.__init__(self, name)
		self.branch = branch
		self.year = year

	def get_details(self):
		'''
		return a string which contains students' information
		'''
		return "{} studies {} and is in {} year.".format(self.name, self.branch, self.year)


class  Teacher(Person):
	"""docstring for  Teacher"""
	def __init__(self, name, papers):
		Person.__init__(self, name)
		self.papers = papers
		
	def get_details(self):
		return "{} teaches {}".format(self.name, ','.join(self.papers))


person1 = Person("Alan")	
student1 = Student("Ella", "CSE", "2018")
teacher1 = Teacher("Jobs", ['Python', 'C++'])

print(person1.get_details())
print(student1.get_details())
print(teacher1.get_details())