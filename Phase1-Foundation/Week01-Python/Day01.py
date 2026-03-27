# ============================================================
# Journey: AI Automation Engineer — 90 Days
# Day 01 | 26-March-2026 | Thursday
# Topic: Variables, data types, print statements, user input, functions.
# Resource: CS50P Harvard - Lecture 0
# ============================================================


print("Hello, World!")  
input("What is your name? ")
name = input("What is your name? ")
print(f"Hello, {name}")


name = name.strip()
print(f"Hello, {name}")

name = name.title()
print(f"Hello, {name}")

name = name.capitalize()
print(f"Hello, {name}")


x = 1
y = 2

z = x + y
print(z)

x = input("What's x ? ")
y = input("What's y ? ")

z = int(x) + int(y) # this will concatenate the strings instead of adding the numbers, because input() returns a string
print(f"The value of z is : {z}")


x = int(input("What's x ? "))
y = int(input("What's y ? "))
print(f"The value of z is : {x + y}")


print(int(input("What's x ? ")) + int(input("What's y ? "))) # this will work but it's not recommended because it's not readable and it's hard to debug if there's an error. It's better to use variables to store the input values and then perform the addition.

x = float(input("What's x ? "))
y = float(input("What's y ? "))
print(f"The value of z is : {x + y}")

# round(number[, ndigits]) # this is a built-in function that rounds a number to a specified number of decimal places. The first argument is the number to be rounded and the second argument is the number of decimal places to round to. If the second argument is not provided, it will round to the nearest integer.

x = float(input("What's x ? "))
y = float(input("What's y ? "))

z = round(x + y, 2) # this will round the result to 2 decimal places
print(f"The value of z is : {z}")

print(f"{z:,}")

x = float(input("What's x ? "))
y = float(input("What's y ? "))

z = round(x/y,2) # this will round the result to 2 decimal places
print(f"The value of z is : {z}")

print(f"{z:.2f}") # this will format the result to 2 decimal places without rounding, it will just cut off the extra decimal places. It's useful when you want to display a number with a specific number of decimal places without changing the actual value of the number.

# Functions.
def hello():
    print("Hello, World!")


name = input("What's your name ? ")
hello()
print(name)

# Passing parameters to functions.
name = input("What's your name ? ")
def hello(name="Burhan"):
    print(f"Hello, {name}!")

hello(name)


# Function scope
hello()
name = "Burhan"
hello(name)


def hello(name):
    print(f"Hello, {name}!")





def main():
    name = input("What's your name ? ")
    hello(name)

def hello(to="Rehan"):
    print(f"Hello, {to}")

main()
