# ============================================================
# Journey: AI Automation Engineer — 90 Days
# Day 05 | 30-March-2026 | Monday
# Topic: Unit Testing in Python.
# Resource: CS50P Harvard - Lecture 5
# ============================================================


#Test the code you wrote yourself
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n+n

if __name__ == "__main__":
        main()


# test_calculator.py created another file that assists me through unit testing in python
from Day05 import square

def main():
    test_square()

# # use of assert statement for testing
def test_square():
    if square(2) != 4:
        print("Test failed: square(2) should be 4")
    if square(3) != 9:
        print("Test failed: square(-3) should be 9")
    try:
        assert square(2) == 4
    except AssertionError:
        print("Test failed! 2 squared should be 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("Test failed! 3 squared should be 9")

    try:
        assert square(-2) == 4
    except AssertionError:
        print("Test failed! -2 squared should be 4")

    try:
        assert square(-3) == 9
    except AssertionError:
        print("Test failed! -3 squared should be 9")

    try:
        assert square(0) == 0
    except AssertionError:
        print("Test failed! 0 squared should be 0")

if __name__ == "__main__":
    main()

# Pytest automate the testing to help you not do testing alot manually

from Day05 import square

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0

Making more functions

def test_positive():
        assert square(2) == 4
        assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
     assert square(0) == 0


def main():
    name = input("What's your name? ")
    print(hello(name))

def hello(to="world"):
    return f"hello, {to}"

if __name__ == "__main__":
    main()