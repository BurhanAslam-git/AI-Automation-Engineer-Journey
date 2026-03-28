# ============================================================
# Journey: AI Automation Engineer — 90 Days
# Day 02 | 28-March-2026 | Saturday
# Topic: Exceptions.
# Resource: CS50P Harvard - Lecture 3
# ============================================================

# Exceptions are errors that occur during the execution of a program.
# print("Hello, world) # SyntaxError: EOL while scanning string literal


x = int(input("What's x? " ))
print(f"x is {x}")


# Using try & except to handle exceptions
try:
    x = int(input("What's x? " ))
    print(f"x is {x}")

except ValueError:
    print("x is NOT an integer")

#Name error
try:
    print(f"Hello, {name}")
except NameError:
    print("name is not defined")


try:
    x = int(input("What's x? " ))
except ValueError:
    print("x is NOT an integer")
else:
    print(f"x is {x}")


while True:
    try:
        x = int(input("What's x? " ))
    except ValueError:
        print("x is NOT an integer")
    else:
        break

print(f"x is {x}")


while True:
    try:
        x = int(input("What's x? " ))
        break
    except ValueError:
        print("x is NOT an integer")

print(f"x is {x}")



# Now using functions to do the same thing
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What's x? " ))
        except ValueError:
            print("x is NOT an integer")
        else:
            break

    return x

main()

# More intuitive
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What's x? " ))
        except ValueError:
            print("x is NOT an integer")
        else:
            return x

main()


#More compact
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("What's x? " ))

        except ValueError:
            print("x is NOT an integer")
    

main()


#If we want we can pass also
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try: 
           return int(input("What's x? "))
        except ValueError:
            pass

main()


def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try: 
           return int(input(prompt))
        except ValueError:
            pass

main()
