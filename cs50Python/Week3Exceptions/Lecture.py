# SyntaxError < for you to solve
"""Error Handling, Programming Defensively

ValueError: value entered is invalid
NameError: name is not defined"""

"""ABSTRACTION of the process of putting the function"""


def main():
    x = get_int("What's x?")
    print(f"X is {x}")


def get_int(prompt):
    # Start the loop
    while True:
        try:
            x = int(input(prompt))  # <<<< this is working fine
            # x is not assigned the value because valueError is happening too soon
            # make it neater
            return int(input('What\'s x?: '))
        except ValueError:
            # print('X is not an integer')
            # Catch and pass
            pass
        # else:  # <-- this will execute if try is successful
        #    return x # <--- return is stronger than break


main()
