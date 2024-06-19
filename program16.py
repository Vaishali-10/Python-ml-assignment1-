def count_character_frequency(input_string):
    # Initialize an empty dictionary to store character frequencies
    frequency_dict = {}

    # Iterate through each character in the string
    for char in input_string:
        # Increment the count of each character in the dictionary
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1

    return frequency_dict

# Example usage:
user_input = input("Enter a string: ")
frequency = count_character_frequency(user_input)

print("Character frequencies:")
for char, count in frequency.items():
    print(f"Character '{char}' occurs {count} times.")
