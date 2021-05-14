#01 Example
a = 8597
b = 8597


print(id(a))
print(id(b))

a = 8598

print(id(a))
print(id(b))

#02 Example
a = "hello"
b = a

print(id(a))
print(id(b))

a += "world"

