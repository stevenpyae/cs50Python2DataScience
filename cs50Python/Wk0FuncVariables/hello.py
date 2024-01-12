"""Functions

defaulting
def hello(to = "world") will print hello, world if no input"""


def main():
    name = input('What is your name? : ')
    hello()


def hello(to='world'):
    print("hello,", to)


'''Scope, Remember the scopes'''
main()
