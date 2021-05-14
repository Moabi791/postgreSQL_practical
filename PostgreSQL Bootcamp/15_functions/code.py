#01 Example
def hello():
	print("Hello!")

hello()

#02 Example
def user_age_in_seconds():
	user_age = int(input("Enter your age: "))
	age_seconds = user_age * 365 * 24 * 60 * 60
	print(f"Your age in seconds is {age_seconds}.")


print("Welcome to the age in seconds program!")
user_age_in_seconds()

print("Goodbye!")

#05 Example
friends = []

def add_friend():
	friends.append("Rolf")


add_friend()
add_friend()
add_friend()


print(friends)  #Rolf