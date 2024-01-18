"""42 forty-two, forty-two case-insensitive"""

def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? : ")
    clean_answer = answer.strip().lower()
    match clean_answer:
        case "42" | "forty two" | "forty-two":
            print("Yes")
        case _:
            print("No")


'''Bank say Hello, pay 0, H, pay 20, anything else pay 100 Concept: lower(), strip, startswith'''

def main():
    words = input("Greetings: ")
    cleaned_words = words.lower().strip()

    if cleaned_words.startswith("hello"):
        print("$0")
    elif cleaned_words.startswith("h"):
        print("$20")
    else:
        print("$100")


'''File Extensions check .jpg etc. Concept: endswith'''
def main():
    filename = input("File name: ").lower().strip()

    if filename.endswith(".gif"):
        print("image/gif")
    elif filename.endswith(".jpg") or filename.endswith(".jpeg"):
        print("image/jpeg")
    elif filename.endswith(".png"):
        print("image/png")
    elif filename.endswith(".pdf"):
        print("application/pdf")
    elif filename.endswith(".txt"):
        print("text/plain")
    elif filename.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")

'''Math Intepreter Concept: Match Case and "{:.1f}".format()'''
def main():
    x, y, z = input("Expression: ").strip().split(" ")
    x = int(x)
    z = int(z)

    match y:
        case "+":
            print("{:.1f}".format(x + z))
        case "-":
            print("{:.1f}".format(x - z))
        case "*":
            print("{:.1f}".format(x * z))
        case "/":
            print("{:.1f}".format(x / z))

'''Meal Time: 6-7am 12-1pm 6-7pm concept 6<time<7
Convert condept: float casting and adding'''
def main():
    ...
    time = input("What time is it?").strip()
    converted_time = convert(time)
    if 7.00 <= converted_time < 8.00:
        print("breakfast time")
    elif 12.00 <= converted_time <= 13.00:
        print ("lunch time")
    elif 18.00 <= converted_time < 19.00:
        print ("dinner time" )


def convert(time):
    # split time str into hour and minutes
    h, m = time.split(":")
    # if a.m. p.m.
    if time.endswith("a.m."):
        return int(h) + float(m)/60.0
    elif time.endswith("p.m."):
        return int(h) + 12 + float(m)/60.0
    else:
        return int(h) + float(m)/60.0
