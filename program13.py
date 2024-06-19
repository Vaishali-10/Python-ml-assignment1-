import datetime

def calculate_age(birth_year):
    current_year = datetime.datetime.now().year
    age = current_year - birth_year
    return age

# Example usage:
try:
    birth_year = int(input("Enter your birth year: "))
    if birth_year < 0 or birth_year > datetime.datetime.now().year:
        print("Invalid birth year entered.")
    else:
        age = calculate_age(birth_year)
        print(f"You are {age} years old.")
except ValueError:
    print("Invalid input. Please enter a valid year.")
