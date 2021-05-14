#01 Example 
student = {"name":"Bokang", "grades": (89, 90, 93, 78, 90)}


def average(sequence):
	return sum(sequence) / len(sequence)


print(average(student["grades"]))


class Student:
	def __init__(self):
		self.name = "Bokang"
		self.grades = (90, 90, 93, 78, 90)

	def average_grade(self):
		return sum(self.grades) / len(self.grades)


student = Student("Bob", (100, 100, 93, 78, 90))
student2 = Student("Bokang", (90, 90, 93, 78, 90))

print(student.name)
print(student.average_grade())
print(student2.average_grade(student2))


///Unfinished///