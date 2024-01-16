"""Questions and Answers"""
# > >= < <= == != Symbols
# If: else:

'''Comparing'''

x = int(input("What's X? : "))
y = int(input("What's Y? : "))

# just greater or less than
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")

#
if x == y:
    print("x is equal to y")
else:
    print("x is not equal to y")


'''and or'''
'''90 <= score <= 100'''
score = int(input("Score: "))

if 90 <= score <= 100:
    print("Grade A")
elif 80 <= score < 90:
    print("Grade B")
elif 70 <= score < 80:
    print("Grade C")
elif 60 <= score < 70:
    print("Grade D")
else:
    print("Grade F")

'''Even or Odd'''


def is_even(x):
    # return True if x%2 == 0 else False
    return x%2 == 0

def main():
    x = int(input("What's x?: "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


'''match'''
name = input("What's your name ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
