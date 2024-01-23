"""Loop Syntax"""


def main():
    i = 0
    while i < 3:
        print("Meow")
        i += 1


"""LIST [0, 1, 2] and FOR loops goes well together"""
# range 3 means it will return 0,1,2
for _ in range(3):  # Pythonic way of writing for _ in range(3)
    print("meow")

# to meow 3 times
print("meow\n" * 3, end="")


def meow(n):
    for _ in range(n):
        print("Meow")


def get_number():
    while True:
        n = int(input("What's N? "))
        if n > 0:
            break
    return n


def main():
    number = get_number()
    meow(number)


"""LIST indexing"""
students = ["Tom", "Dick", "Harry"]

for student in students:
    print(student)

for i in range(len(students)):
    print(students[i])

"""Dictionary dict words and definition, keys and values
if you Iterate over a dictionary, it iterates all the keys"""
students = {"Hermione": "Gryffindor",
            "Harry": "Gryffindor",
            "Ron": "Gryffindor",
            "Draco": "Slytherin"
            }
# Index using Keys
print(students["Hermione"])
# Print everything
for student in students:
    print(student, students[student], sep=",")

"""List of DICTIONARIES collection of keys and value pairs
Make sure: Name of the keys are the same"""
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel Terrier"},
    {"name": "Drago", "house": "Slytherin", "patronus": None},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")


def print_columns(height):
    for _ in range(height):
        print("#")


def print_row(width):
    print("?" * width)


def print_square(size):
    # for each row in square
    for i in range(size):
        # for each brick in row
        # print("#" * size)
        for j in range(size):
            # print brick
            print("#", end="")
    print()


def main():
    print_row(3)
    print_columns(3)

