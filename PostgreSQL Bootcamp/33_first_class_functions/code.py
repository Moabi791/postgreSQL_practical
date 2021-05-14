#01 Example
def divide(dividend, divisor):
	if divisor == 0:
		raise ZeroDivisionError("Division cannot be 0.")

	return dividend / divisor


def calculate(*values, operator):
	return operator(*values)


result = calculate(20, 4, operator=divide)
print(result)


#02 Example
from operator import itemgetter

def search(sequence, expected, finder):
	for elem in sequence:
		if finder(elem) == expected:
			return elem
	raise RuntimeError(f"Could not find an element with {expected}.")


friends = [
	{"name": "Rolf Smith", "age":24},
	{"name": "Boity Thulo", "age":29},
	{"name": "Kagisho Senatle", "age":30},
]

def get_friend_name(friend):
	return friend["name"]


print(search(friends, "Boity Thulo", itemgetter("name")))