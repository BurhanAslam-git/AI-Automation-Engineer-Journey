# ============================================================
# Journey: AI Automation Engineer — 90 Days
# Day 02 | 27-March-2026 | Friday
# Topic: Conditional statements, loops.
# Resource: CS50P Harvard - Lecture 1
# ============================================================

x = int(input("What's x ? "))
y = int(input("What's y ? "))

if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to y")


Now using elif to make it more efficient
x = int(input("What's x ? "))
y = int(input("What's y ? "))

# elif is short for else if.
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")

# More intuitive programing.
x = int(input("What's x ? "))
y = int(input("What's y ? "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else: 
    print("x is equal to y")
 

Using or keyword
x = int(input("What's x ? "))
y = int(input("What's y ? "))

if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# Both ways to do the same thing
x = int(input("What's x ? "))
y = int(input("What's y ? "))

if x != y:
    print("x is not equal to y")
else: 
    print("x is equal to y")

and keyword
score = int(input("What's your score ? "))
if score >= 90 and score <= 100:
    print("Your grade is A")
elif score >= 80 and score < 90:
    print("Your grade is B")
elif score >= 70 and score < 80:
    print("Your grade is C")
elif score >= 60 and score < 70:
    print("Your grad e is D")
else:
    print("Your grade is F")

score = int(input("What's your score ? "))
if 90 <= score <= 100:
    print("Your grade is A")
elif 80 <= score < 90:
    print("Your grade is B")
elif 70 <= score < 80:
    print("Your grade is C")
elif 60 <= score < 70:
    print("Your grade is D")
else:
    print("Your grade is F")

score = int(input("What's your score ? "))
if score >= 90:
    print("Your grade is A")
elif score >= 80:
    print("Your grade is B")
elif score >= 70:
    print("Your grade is C")
elif score >= 60:
    print("Your grade is D")
else:
    print("Your grade is F")

Use of % operator
x = int(input("What's x ? "))
if x % 2 == 0:
    print("x is even")
else:
    print("x is odd")

# Making our own functions
def main():
    x = int(input("What's x ? "))
    if is_even(x):
        print("x is even")
    else:
        print("x is odd")

def is_even(n):
    if n % 2 == 0:
         return True
    else: 
        return False

# # Condenserd version
def is_even(n):
    return True if n % 2 == 0 else False

def is_even(n):
    return n % 2 == 0

main()

# Use of match 

name = input("What's your name ? ")
match name:
    case "Harry":
        print("Hello Harry")
    case "Ron":
        print("Hello Ron")
    case "Hermione":
        print("Hello Hermione")
    case _:
        print("Hello Stranger")


name = input("What's your name ? ")
match name: 
    case "Harry" | "Ron" | "Hermione":
        print(f"Hello, {name}")
    case _:
        print("Hello Stranger")


# Mini-Task
name = input("What's your name ? ")
mood = input("How are you feeling today ? ").lower()
task = input("What do you want to do today ? ").lower()

if mood == "happy" and task == "work":
      print(f"Hello, {name} Great energy! This is the perfect time to do focused work.")
elif mood == "sad" and task == "work":
        print(f"Hello, {name} You're feeling sad, but starting small with study might help you feel better.")
elif mood == "happy" and task == "play":
        print(f"Hello, {name} You're feeling happy, and playing is a great way to enjoy your day!")
elif mood == "sad" and task == "play":
        print(f"Hello, {name} You're feeling sad, but playing can be a great way to lift your spirits!")
else:
        print(f"Hello, {name} It seems like you have a unique mood and task combination. Embrace it and make the most of your day!")


Loops in Python
for i in range(5):
    print(i)

for i in [0,1,2]:
    print("meow")

for _ in range(3):
    print("meow")

print("meow\n" * 3)


i = 3
while i != 0:
    print(i)
#    i -= 1
    i = i - 1 

while True:
    n = int(input("What's n ? "))
    if n > 0:
        break

for i in range(n):
    print("meow")


def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n ? "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")

main()

students = ["Harry", "Ron", "Hermione"]
print(students[0])
print(students[1])
print(students[2])


for x in students:
    print(x)

# Another way to do the same thing
for i in range(len(students)):
    print(i+1, "--> ", students[i])


# Dictonary in Python
students = {
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Hermione": "Gryffindor",
    "Draco": "Slytherin"
}

for student in students:
    print(student, "is in", students[student])

print(students["Harry"])

students = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"}
]

for student in students:
    print(student["name"], "is in", student["house"])

def main():
    print_row(4)

def print_row(n):
    print("X" * n)

main()

def main():
   print("X" * 4)

main()


def main():
    print_square(4)

def print_square(size):
    # For each row in the square
    for i in range(size):
        # For each brick in the row
        for j in range(size):
            # Print Brick
            print("X", end="")
        print()

main()

def main():
    print_square(4)

def print_square(size):
    # For each row in the square
    for i in range(size):
        # Print a row of bricks
        print_row(size)
       

def print_row(size):
    print("X" * size)

main()