#01 Example
t = 5 , 11
x, y = t

print(x, y)

#02 Example
student_attendance = {"Rolf": 96, "Bob": 80, "Anne":100}

print(list(student_attendance.items()))

for student, attendance in student_attendance.items():
	print(f"{student}: {attendance}")


#03 Example
people =[("Bob", 42, "Mechanic"),("James", 24, "Artist"), ("Harry", 32, "Lecturer")]

for person  in people:
	print(f"Name: {person[0]}, Age: {person[1]}, Profession: {person[2]}")

#04 Example
person = ("Bob", 42, "Mechanic")
name, _, Profession = person

print(name, Profession)


#05 Example
*head, tail = [1, 2, 3, 4, 5]
print(head)
print(tail)