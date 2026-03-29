# ============================================================
# Journey: AI Automation Engineer — 90 Days
# Day 04 | 29-March-2026 | Sunday
# Topic: Libraries in Python.
# Resource: CS50P Harvard - Lecture 4
# ============================================================

import random
print("Hello, I am learning now libraries in python, I amn very excited for this too")
coin = random.choice(["heads", "tails"])
print(coin)


# We can use this way to import only the choice function from the random library
from random import choice
coin = choice(["heads", "tails"])
print(coin)

 
# Inclusively, we can import all the functions from the random library using the * symbol
import random
number = random.randint(1, 10)
print(number)


# Shuffle
import random
cards = ["Jack", "Queen", "King"]
random.shuffle(cards)
print(cards)


# Using this as well.
import random
cards = ["Jack", "Queen", "King"]
random.shuffle(cards)
for card in cards:
    print(card)


# Stastics Library
import statistics

statistics.mean([1, 2, 3, 4, 5])
statistics.median([1, 2, 3, 4, 5])
statistics.stdev([1, 2, 3, 4, 5])
print(statistics.mean([1, 2, 3, 4, 5]))
print(statistics.median([1, 2, 3, 4, 5]))


# Sys
import sys

print("Hello, my name is", sys.argv[1])


import sys
try:
   print("Hello, my name is", sys.argv[1])
except IndexError:
    print("Usage: python script.py <name>")


import sys
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("Hello, my name is", sys.argv[1])

import sys
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")

print("Hello, my name is", sys.argv[1])


import sys
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("Hello, my name is", sys.argv[1])


import sys
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1]:
    print("Hello, my name is", arg)
    

# Use Slices
import sys
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("Hello, my name is", arg)

# 1: means start at 1 goes till the end this is called as slicing


# slicing from the end
import sys
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:-1]:
    print("Hello, my name is", arg)

# Packages PyPi cowsay pip

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("Hello, " + sys.argv[1])


import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex("Hello, " + sys.argv[1])


# API (Application Programming Interface)
# Third party API
import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://api.github.com/users/" + sys.argv[1])

o = response.json()
for result in o:
    print(result, ":", o[result])


# Making our own libray that we can use

import sys
from Day42 import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])


# for this i made another file called Day42.py and i have defined the hello function in that file and then i am importing that function here and using it here. This is how we can make our own library and use it in our code.
def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"Hello, {name}!")

def goodbye(name):
    print(f"Goodbye, {name}!")

if __name__ == "__main__":
    main()
