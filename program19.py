import string

def remove_punctuation(input_string):
    
    translator = str.maketrans('', '', string.punctuation)
    
    cleaned_string = input_string.translate(translator)
    return cleaned_string

user_input = input("Enter a string with punctuation: ")
cleaned_string = remove_punctuation(user_input)
print(f"The string without punctuation is: {cleaned_string}")
