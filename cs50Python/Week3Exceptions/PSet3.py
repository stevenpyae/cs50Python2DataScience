# How to exept multiple errors -> except (ValueError, ZeroDivisionError)

def get_fraction():
    while True:
        try:
            x, y = input("Fraction: ").split("/")
            if int(x) > int(y):
                pass
            else:
                return int(x) / int(y) * 100.0
        except (ValueError, ZeroDivisionError):
            pass


def main():
    answer = get_fraction()
    if answer >= 99.0:
        print("F")
    elif answer <= 1.0:
        print("E")
    else:
        print(str(int(round(answer))) + "%")


''''GROCERIES use of Library
'''

grocery_list = {}

while True:
    try:
        grocery_item = input()
        # if grocery_item is inside the list, add 1
        if grocery_item in grocery_list:
            grocery_list[grocery_item] += 1
        else:
            # add the new grocery_item to the list
            grocery_list[grocery_item] = 1
    except EOFError:
        break

# apply a sorted function to sort the list
for key, value in enumerate(sorted(grocery_list)):
    print(grocery_list[value], value.upper())

'''Dates from 1/3/2002 -> 2002-03-01'''

months = ["January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "December"]


# print(f"{n:02}"
def valid_date(month, day):
    return (int(month) > 12) or (int(day) > 31)


while True:
    try:
        # process 9/8/1636
        input_date = input("Date: ").strip()
        month, day, year = input_date.split("/")
        # Check for valid date
        try:
            if valid_date(month, day):
                pass
            else:
                print(year + f"-{int(month):02}" + f"-{int(day):02}")
                break
        except ValueError:
            # not valid date, reprompt
            pass
    except ValueError:
        # to process September 8, 1636, can be 8 September,
        # check if there is comma
        if "," in input_date:
            input_date = input_date.replace(",", "")
            month, day, year = input_date.split(" ")
            try:
                # check for valid date
                if valid_date((int(months.index(month)) + 1), day):
                    pass
                else:
                    # format and print according to leading zeros
                    print(year + f"-{int(months.index(month) + 1):02}" + f"-{int(day):02}")
                    break
            except ValueError:
                pass
        else:
            # no comma pass
            pass

'''Menu items with Try Except'''
# Format String, EOFError if Ctrl+D is pressed, KeyError if no item is found
menu_items = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# Control D is EOFError
# if cannot find key then how
cost = 0.00
while True:
    try:
        item = input("Item: ").title()
        cost+= menu_items[item]
        print(f"Total: ${cost:.2f}")
    except EOFError: # if ctrl+d is pressed
        print("\n")
        break
    except KeyError: # if key error is occurred. let's restart from the loop
        pass
