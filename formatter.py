def clean_number(text):
    return text.strip().replace("-", "").replace(" ","")

def format_number(number):
    return f"{number[0:3]}-{number[3:6]}-{number[6:10]}"

def hide_number(number):
    return f"{number[0:3]}-xxx-{number[6:10]}"

def is_valid(number):
    return len(number) == 10 and number.isnumeric() and number[0] == "0"

def digit_sum(number):
    a = 0
    for n in number:
        a += int(n)
    return a

raw = input("Phone number: ")
number = clean_number(raw)
if is_valid(number):
    print(f"Formatted {format_number(number)}")
    print(f"Hidden: {hide_number(number)}")
    print(f"Digit sum: {digit_sum(number)}")
else:
    print("Invalid phone number")