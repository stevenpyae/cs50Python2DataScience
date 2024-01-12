# indoor <- Make all lower case
print(input().lower())

# playback <-- Replace Space with ...
print(input().replace(" ", "..."))

# Faces <- teach you functions chaining
print(input().replace(":)", "😊").replace(":(", "🙁"))

# einstein <-- Teach you arithematic
print(int(input("m: ")) * 300000000 * 30000000)


# Tip Calculator <-- Teach you float conversion

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")  # <---- 2 decimal palces


def dollars_to_float(d):
    return float(d)


def percent_to_float(p):
    return float(p) / 100
