
# general class
class Human:

	# class attribute (static and shared among all instances)
	number_of_humans = 0

	def __init__(self, name, age):
		self.name = name
		self.age = age

		# could use the line below but through a class method is more professional
		# Human.number_of_humans +=1 # incremeting every time a new instance is created
		Human.add_human()

	def show(self):
		print(f"I am {self.name} and I am {self.age} years old")

	def get_name(self):
		return self.name
	
	def get_age(self):
		return self.age

	# creating a class method. It does not act for one instance. 
	# it works by acting on the class itself instead of "self" (object)
	# underscore added at the end so that the method won't have the same name as the attribute
	@classmethod
	def number_of_humans_(cls):
		return cls.number_of_humans

	@classmethod
	def add_human(cls):
		cls.number_of_humans += 1

	# static method don't change anything - don't access anything
	# it will act as a simple function inside the class
	@staticmethod
	def show_student_name_upper(student_name):
		return student_name.upper()

# specialized class (specific) inheriting from Human
class Student(Human):
	def __init__(self, name, age, grade):
		super().__init__(name, age) # reference the super class constructor method
		self.grade = grade # 0 - 100

	def get_grade(self):
		return self.grade

	# if this method exists, it will overwrite the super class show method
	def show(self):
		print(f"I am a student and my name is {self.name} and my age is {self.age}")

class Course:
	def __init__(self, name, max_students):
		self.name = name
		self.max_students = max_students
		self.students = []

	def add_students(self, student):
		if len(self.students) < self.max_students:
			self.students.append(student)
			return True
		return False

	def get_average_grade(self):
		value = 0
		for student in self.students:
			value += student.get_grade()
			
		return value / len(self.students)

# creating students
s1 = Student("Tim", 19, 95)
s2 = Student("Mike", 34, 68)
s3 = Student("Havana", 22, 88)
s4 = Student("Dayana", 21, 44)

# max 2 students per course
course = Course("Science", 2)

course.add_students(s1)
course.add_students(s2)

# print(course.students[1].name)
# print(course.get_average_grade())

s1.show()
s2.show()

# accessing a class attribute directly since it does not belong to any instance
print(Human.number_of_humans)

# accessing a class attribute through an instance
print(s2.number_of_humans)

# using the static method defined just to perform an action
# not tied to any instance
print(Human.show_student_name_upper(s1.get_name()))


