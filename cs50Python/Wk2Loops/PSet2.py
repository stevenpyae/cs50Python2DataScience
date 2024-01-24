"""Snake case Camel Case"""
def main():
    s = input("camelCase: ")
    snakes = ""
    for c in s:
        if c.isupper():
            s = s.replace(c, ("_" + c.lower()))

    print("snake_case", s)


"""Coke Machine"""
def main():
    price_of_coke = 50
    while price_of_coke > 0:
        print(f"Amount Due: {price_of_coke}")
        inserted_coin = int(input("Insert Coin: "))
        match inserted_coin:
            case 25 | 10 | 5:
                #minus inserted coins
                price_of_coke -= inserted_coin
            case _:
                # Insert other coins, do nothing return back to the loop
                continue
    # handle negative numbers and change
    if price_of_coke == 0:
        print("Change Owed:", price_of_coke)
    else:
        print("Change Owed:", price_of_coke* -1)


"""Twitter"""
def main():
    s = input("Input: ")
    for c in s:
        match c.lower():
            case "a" | "e" | "i" | "o" | "u":
                # if vowels then replace the string with the removed string.
                s = s.replace(c, "")
            case _:
                continue
    print(s)


"""VANITY PLATES a lot of BOOLEAN"""
def is_valid(s):
    #
    #“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    #
    first_digit_index = 0
    for c in s:
        if c.isnumeric():
            first_number = c
            break
        else:
            first_digit_index+=1

    #Numbers cannot be used in the middle of a plat
    for c in s[first_digit_index:]:
        if c.isalpha():
            return False
    #All vanity plates must start with at least two letters.”

    if 2 <= len(s) <= 6 and s[0:2].isalpha():
        #Edge case where its all ALPHA
        if s.isalpha():
            return True
        else:
            if s[-1].isdigit() and int(first_number) != 0: #The first number used cannot be a ‘0’.”
                for c in s:
                    if not c.isalnum():
                        return False
                    else:
                        continue
                return True
            else:
                return False
    else:
        return False

"""Fruits Dictionary"""
def main():

    fruits = {"Apple": "130",
              "Avocado": "50",
              "Banana": "110",
              "Cantaloupe": "50",
              "Grapefruit": "60",
              "Grapes": "90",
              "Honeydew Melon": "50",
              "Kiwifruit": "90",
              "Lemon": "15",
              "Lime": "20",
              "Nectarine": "60",
              "Orange": "80",
              "Peach": "60",
              "Pear": "100",
              "Pineapple": "50",
              "Plums": "70",
              "Strawberries": "50",
              "Sweet Cherries": "100",
              "Tangerine": "50",
              "Watermelon": "80"}

    fruit_to_search = input("Item: ")
    #iterate over the dictionary
    for fruit in fruits:
        #if match is found then print out the calories
        if fruit.lower() == fruit_to_search.lower():
            print("Calories:", fruits[fruit])
        else:
            #if not ignore
            continue

main()
