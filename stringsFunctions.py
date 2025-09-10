# function, you can pass 1 to some inputs to exec to get one output
# ex : func_name()
# example for function
type("hello")
# help("int")


# The String Length function
# Only can use for strings
word = "Chicken Banana"
output = word + " , Length : " + str(len(word))
print(output)

# Input
age = input("How old are you?")
print(type(age))
print("Your age is " + age)

# Cast Types
# Change value type to other one
print(int("12"))
print(float("3.3"))
print(str(44.5))

age2 = input("How old are you? (in days)?")
# input is string type
print(age2 * 365)
print(int(age2) * 365)

# f strings only in Python3
# you can put some calculate with {} in the string or variable
fstirng = f"there are ${4*67.99}"
print(fstirng)
age2 = input("How old are you? (in days)?")
fstring2 = f"You are {int(age2)*365} days old"
print(fstring2)