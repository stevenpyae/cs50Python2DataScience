# Asking user for name
name = input("What is your name?: ").strip().title()

# Say Hello to the user's input
print("Hello ", end="")
print(name)

# Separater
print("Hello," , name, sep = ":::")

'''String Methods'''
# Remove whitespaces and capitalise user's name
first, last = name.split(" ") #will return a sequence of values

# Formatted
print(f'Fromatted: Hello, {first}')

'''

print(*object, sep = '', end = '\n', 
Functions: print
Arguments: variables inside the ()
Side Effects: Visual, Audios
Return Value
Variables: 
Comments : 
Paseudocode
Parameters: positional parameters, 
named parameters -> sep, end <- Optional
'''


'''
Syntax Error: 
Run the program without Terminal Window -> 
Ship the software -> Write program and 
Graphical User Interface.                               
'''

'''Escape Characters'''
print('Hello, \"dog\"')

